import csv
import shutil
import subprocess
from datetime import date, time, timedelta, datetime
from pathlib import Path
from typing import cast
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

import yaml
from pydantic import BaseModel

from gtfs_data import FerryConfig, GTFSAgency, GTFSStop, GTFSService, GTFSTrip, IntBool, GTFS, GTFSRoute, GTFSStopTime, \
    GTFSFrequency, GTFSLevels
from other_data import ROUTE_TYPES_GTFS


def gtfs_datestring(d: date) -> str:
    return d.strftime("%Y%m%d")


def gtfs_timestring(t: date | time) -> str:
    return t.strftime("%H:%M:%S")


def convert(ferry: FerryConfig):
    prefix = lambda val: ferry.route_id + ":" + val

    gtfs = GTFS()
    ag = GTFSAgency(**ferry.agency.__dict__, agency_id=ferry.route_id)
    gtfs.agency.append(ag)

    for s in ferry.endpoints:
        stop = GTFSStop(
            stop_id=prefix(s.stop_id),
            stop_name=s.stop_name,
            stop_desc=s.stop_desc,
            stop_lat=s.position.lat,
            stop_lon=s.position.lon,
            level_id=s.position.level,
        )
        if s.platform_code is not None:
            stop.platform_code = s.platform_code
        gtfs.stops.append(stop)

    start = ferry.endpoints[0]
    end = ferry.endpoints[1]

    route = GTFSRoute(
        route_id=ferry.route_id,
        agency_id=ag.agency_id,
        route_short_name=ferry.route_short_name,
        route_long_name=ferry.route_long_name,
        route_type=ROUTE_TYPES_GTFS[ferry.route_type],
    )
    gtfs.routes.append(route)
    travel_time_delta = timedelta(minutes=ferry.travel_time_minutes)

    for serv_data in ferry.services:
        service = GTFSService.from_days(
            days=serv_data.days,
            service_id=prefix(serv_data.service_id),
            start_date=gtfs_datestring(serv_data.start_date),
            end_date=gtfs_datestring(serv_data.end_date),
        )
        gtfs.calendar.append(service)

        both_directions = {
            "bikes_allowed": ferry.bikes_allowed,
            "cars_allowed": ferry.cars_allowed,
        }
        permutations = [
            (start, end),
            (end, start)
        ]
        for i, (stop0, stop1) in enumerate(permutations):
            name = "AB" if i == 0 else "BA"
            trip = GTFSTrip(
                route_id=ferry.route_id,  # TODO
                service_id=service.service_id,
                trip_id=f"{service.service_id}:{name}",
                trip_headsign=f"Richtung {stop1.location_name}",
                direction_id=cast(IntBool, i),
                **both_directions
            )
            gtfs.trips.append(trip)

            stop_time0 = GTFSStopTime(
                trip_id=trip.trip_id,
                stop_id=prefix(stop0.stop_id),
                arrival_time="00:00:00",
                departure_time="00:00:00",
                stop_sequence=1
            )
            gtfs.stop_times.append(stop_time0)

            travel_time = f"00:{ferry.travel_time_minutes:02d}:00"
            stop_time1 = GTFSStopTime(
                trip_id=trip.trip_id,
                stop_id=prefix(stop1.stop_id),
                arrival_time=travel_time,
                departure_time=travel_time,
                stop_sequence=2
            )
            gtfs.stop_times.append(stop_time1)

        for w in serv_data.windows:
            frequency_forward = GTFSFrequency(
                trip_id=gtfs.trips[-2].trip_id,
                start_time=gtfs_timestring(w.start),
                end_time=gtfs_timestring(w.end),
                headway_secs=ferry.headway_minutes * 60,
                exact_times=0
            )
            gtfs.frequencies.append(frequency_forward)
            frequency_backwards = GTFSFrequency(
                trip_id=gtfs.trips[-1].trip_id,
                start_time=gtfs_timestring(w.start_datetime + travel_time_delta),
                end_time=gtfs_timestring(w.end_datetime + travel_time_delta),
                headway_secs=ferry.headway_minutes * 60,
                exact_times=0
            )
            gtfs.frequencies.append(frequency_backwards)


    return gtfs


def model_to_file(rows: list[BaseModel], file: Path):
    first_entry = rows[0]
    fieldnames = list(first_entry.__class__.model_fields.keys())
    with file.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows([row.model_dump() for row in rows])


def git_time(dir: Path):
    out = subprocess.run([
        "git", "log", "-1", "--pretty=%ct", "."
    ], cwd=dir, capture_output=True, check=True)
    return datetime.fromtimestamp(int(out.stdout.decode().strip()))


def main():
    data_dir = Path(__file__).parent / "gtfs_data"
    output_path = Path(__file__).parent / "gtfs_output"
    for input_dir in data_dir.glob("*"):
        if not input_dir.is_dir():
            continue
        mod_time = git_time(input_dir)
        dir_name = input_dir.name
        outdir = output_path / dir_name
        outdir.mkdir(exist_ok=True, parents=True)
        input_files = sorted(input_dir.glob("*.yaml"))
        gtfs = GTFS()

        for input_file in input_files:
            with input_file.open() as f:
                data = yaml.safe_load(f)
            ferry = FerryConfig.model_validate(data)

            gtfs_new = convert(ferry)
            gtfs.extend(gtfs_new)

        gtfs.levels.append(GTFSLevels(level_id=0, level_index=0.0))

        model_to_file(gtfs.agency, outdir / "agency.txt")
        model_to_file(gtfs.stops, outdir / "stops.txt")
        model_to_file(gtfs.calendar, outdir / "calendar.txt")
        model_to_file(gtfs.routes, outdir / "routes.txt")
        model_to_file(gtfs.trips, outdir / "trips.txt")
        model_to_file(gtfs.stop_times, outdir / "stop_times.txt")
        model_to_file(gtfs.frequencies, outdir / "frequencies.txt")
        model_to_file(gtfs.levels, outdir / "levels.txt")

        tmp_file = outdir / "tmp.zip"
        outzip = outdir.with_suffix(".zip")
        outfiles = sorted(outdir.glob("*.txt"))
        with ZipFile(tmp_file, compression=ZIP_DEFLATED, compresslevel=9, mode="w") as zf:

            # zf.write()
            for file in outfiles:
                # make ZIP file reproducable
                # based on zf.write()
                # and https://github.com/drivendataorg/repro-zipfile
                zinfo = ZipInfo.from_file(file, file.name,
                                          strict_timestamps=False)

                zinfo.date_time = mod_time.timetuple()
                zinfo.compress_type=zf.compression
                zinfo.compress_level=zf.compresslevel
                zinfo.external_attr = 0o644 << 16
                with file.open("rb") as src, zf.open(zinfo, 'w') as dest:
                    shutil.copyfileobj(src, dest, 1024*8)
        tmp_file.rename(outzip)
        subprocess.run(["sha256sum", f"{outzip}"])


if __name__ == '__main__':
    main()
