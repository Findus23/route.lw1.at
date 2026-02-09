import json
from datetime import date, datetime, time
from typing import Literal

from pydantic import BaseModel, Field, ConfigDict

from other_data import RouteType


class MyBaseModel(BaseModel):
    model_config = ConfigDict(extra='forbid')


Days = Literal["weekday", "weekend", "weekend_ph", "daily","frsasoph"]
IntBool = Literal[0, 1]


### Input Data Scheme

class Agency(MyBaseModel):
    agency_name: str
    agency_url: str
    agency_timezone: str = "Europe/Vienna"
    agency_lang: str = "DE"
    agency_phone: str | None = None


class TimeWindow(MyBaseModel):
    start: time
    end: time

    @property
    def start_datetime(self) -> datetime:
        return datetime.combine(date.today(), self.start)

    @property
    def end_datetime(self) -> datetime:
        return datetime.combine(date.today(), self.end)


class ServiceRule(MyBaseModel):
    service_id: str | None
    days: Days
    start_date: date
    end_date: date
    windows: list[TimeWindow]


class Postion(MyBaseModel):
    lat: float = Field(ge=48, lt=49)
    lon: float = Field(ge=15, lt=17)
    level: int = Field(ge=-8, lt=8, default=0)


class Endpoint(MyBaseModel):
    stop_id: str | None
    stop_name: str
    location_name: str
    position: Postion
    platform_code: str | None = None
    stop_desc: str | None = None


class FerryConfig(MyBaseModel):
    year: int
    route_id: str
    route_short_name: str
    route_long_name: str
    bikes_allowed: bool
    cars_allowed: bool
    headway_minutes: int
    travel_time_minutes: int
    agency: Agency
    route_type: RouteType
    services: list[ServiceRule]
    endpoints: list[Endpoint] = Field(min_length=2, max_length=2)


### GTFS Data Scheme

class GTFSAgency(Agency):
    agency_id: str


class GTFSStop(MyBaseModel):
    # stops.txt
    stop_id: str
    stop_name: str
    stop_desc: str | None = None
    stop_lat: float
    stop_lon: float
    level_id: int
    platform_code: str | None = None


class GTFSService(MyBaseModel):
    # calendar.txt
    service_id: str
    monday: IntBool
    tuesday: IntBool
    wednesday: IntBool
    thursday: IntBool
    friday: IntBool
    saturday: IntBool
    sunday: IntBool
    start_date: str
    end_date: str

    @classmethod
    def from_days(cls, days: Days, service_id: str, start_date: str, end_date: str):
        weekdays: IntBool = 1 if days in {"weekday", "daily"} else 0
        friday: IntBool = 1 if days in {"weekday", "daily","frsasoph"} else 0
        weekend: IntBool = 1 if days in {"weekend", "weekend_ph", "daily","frsasoph"} else 0

        return cls(
            service_id=service_id,
            start_date=start_date,
            end_date=end_date,
            monday=weekdays,
            tuesday=weekdays,
            wednesday=weekdays,
            thursday=weekdays,
            friday=friday,
            saturday=weekend,
            sunday=weekend,
        )


class GTFSTrip(MyBaseModel):
    # trips.txt
    route_id: str
    service_id: str
    trip_id: str
    trip_headsign: str
    direction_id: IntBool
    bikes_allowed: IntBool
    cars_allowed: IntBool


class GTFSRoute(MyBaseModel):
    route_id: str
    agency_id: str
    route_short_name: str
    route_long_name: str
    route_type: int


class GTFSStopTime(MyBaseModel):
    trip_id: str
    stop_id: str
    arrival_time: str
    departure_time: str
    stop_sequence: int


class GTFSFrequency(MyBaseModel):
    trip_id: str
    start_time: str
    end_time: str
    headway_secs: int
    exact_times: IntBool

class GTFSLevels(MyBaseModel):
    level_id: int
    level_index:float


class GTFS(MyBaseModel):
    agency: list[GTFSAgency] = Field(default_factory=list)
    stops: list[GTFSStop] = Field(default_factory=list)
    calendar: list[GTFSService] = Field(default_factory=list)
    trips: list[GTFSTrip] = Field(default_factory=list)
    routes: list[GTFSRoute] = Field(default_factory=list)
    stop_times: list[GTFSStopTime] = Field(default_factory=list)
    frequencies: list[GTFSFrequency] = Field(default_factory=list)
    levels: list[GTFSLevels] = Field(default_factory=list)

    def extend(self, other: "GTFS"):
        self.agency.extend(other.agency)
        self.stops.extend(other.stops)
        self.calendar.extend(other.calendar)
        self.trips.extend(other.trips)
        self.routes.extend(other.routes)
        self.stop_times.extend(other.stop_times)
        self.frequencies.extend(other.frequencies)
        self.levels.extend(other.levels)


def dump_schema():
    main_model_schema = FerryConfig.model_json_schema()
    with open("schema.json", "w") as f:
        json.dump(main_model_schema, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    dump_schema()
