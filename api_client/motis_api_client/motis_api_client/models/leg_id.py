from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mode import Mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="LegId")


@_attrs_define
class LegId:
    """
    Attributes:
        display_name (str):
        trip_id (str):
        from_id (str): from stop stopId
        from_lat (float): latitude of the leg's from endpoint
        from_lon (float): longitude of the leg's from endpoint
        to_id (str): to stop stopId
        to_lat (float): latitude of the leg's to endpoint
        to_lon (float): longitude of the leg's to endpoint
        sched_start (int): Scheduled departure time as a Unix timestamp in seconds.
        sched_end (int): Scheduled arrival time as a Unix timestamp in seconds.
        mode (Mode): # Street modes

              - `WALK`
              - `BIKE`
              - `RENTAL` Experimental. Expect unannounced breaking changes (without version bumps) for all parameters and
            returned structs.
              - `CAR`
              - `CAR_PARKING` Experimental. Expect unannounced breaking changes (without version bumps) for all parameters
            and returned structs.
              - `CAR_DROPOFF` Experimental. Expect unannounced breaking changes (without version bumps) for all perameters
            and returned structs.
              - `ODM` on-demand taxis from the Prima+ÖV Project
              - `RIDE_SHARING` ride sharing from the Prima+ÖV Project
              - `FLEX` flexible transports

            # Transit modes

              - `TRANSIT`: translates to `TRAM,FERRY,AIRPLANE,BUS,COACH,RAIL,ODM,RIDE_SHARING,FUNICULAR,AERIAL_LIFT,OTHER`
              - `TRAM`: trams
              - `SUBWAY`: subway trains (Paris Metro, London Underground, but also NYC Subway, Hamburger Hochbahn, and other
            non-underground services)
              - `FERRY`: ferries
              - `AIRPLANE`: airline flights
              - `BUS`: short distance buses (does not include `COACH`)
              - `COACH`: long distance buses (does not include `BUS`)
              - `RAIL`: translates to `HIGHSPEED_RAIL,LONG_DISTANCE,NIGHT_RAIL,REGIONAL_RAIL,SUBURBAN,SUBWAY`
              - `HIGHSPEED_RAIL`: long distance high speed trains (e.g. TGV)
              - `LONG_DISTANCE`: long distance inter city trains
              - `NIGHT_RAIL`: long distance night trains
              - `REGIONAL_FAST_RAIL`: deprecated, `REGIONAL_RAIL` will be used
              - `REGIONAL_RAIL`: regional train
              - `SUBURBAN`: suburban trains (e.g. S-Bahn, RER, Elizabeth Line, ...)
              - `ODM`: demand responsive transport
              - `RIDE_SHARING`: ride sharing
              - `FUNICULAR`: Funicular. Any rail system designed for steep inclines.
              - `AERIAL_LIFT`: Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). Cable transport where
            cabins, cars, gondolas or open chairs are suspended by means of one or more cables.
              - `AREAL_LIFT`: deprecated
              - `METRO`: deprecated
              - `CABLE_CAR`: deprecated
        scheduled (bool):
        from_level (float | Unset): Optional level (floor) of the leg's from endpoint for indoor routing.
        to_level (float | Unset): Optional level (floor) of the leg's to endpoint for indoor routing.
    """

    display_name: str
    trip_id: str
    from_id: str
    from_lat: float
    from_lon: float
    to_id: str
    to_lat: float
    to_lon: float
    sched_start: int
    sched_end: int
    mode: Mode
    scheduled: bool
    from_level: float | Unset = UNSET
    to_level: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        trip_id = self.trip_id

        from_id = self.from_id

        from_lat = self.from_lat

        from_lon = self.from_lon

        to_id = self.to_id

        to_lat = self.to_lat

        to_lon = self.to_lon

        sched_start = self.sched_start

        sched_end = self.sched_end

        mode = self.mode.value

        scheduled = self.scheduled

        from_level = self.from_level

        to_level = self.to_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "tripId": trip_id,
                "fromId": from_id,
                "fromLat": from_lat,
                "fromLon": from_lon,
                "toId": to_id,
                "toLat": to_lat,
                "toLon": to_lon,
                "schedStart": sched_start,
                "schedEnd": sched_end,
                "mode": mode,
                "scheduled": scheduled,
            }
        )
        if from_level is not UNSET:
            field_dict["fromLevel"] = from_level
        if to_level is not UNSET:
            field_dict["toLevel"] = to_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName")

        trip_id = d.pop("tripId")

        from_id = d.pop("fromId")

        from_lat = d.pop("fromLat")

        from_lon = d.pop("fromLon")

        to_id = d.pop("toId")

        to_lat = d.pop("toLat")

        to_lon = d.pop("toLon")

        sched_start = d.pop("schedStart")

        sched_end = d.pop("schedEnd")

        mode = Mode(d.pop("mode"))

        scheduled = d.pop("scheduled")

        from_level = d.pop("fromLevel", UNSET)

        to_level = d.pop("toLevel", UNSET)

        leg_id = cls(
            display_name=display_name,
            trip_id=trip_id,
            from_id=from_id,
            from_lat=from_lat,
            from_lon=from_lon,
            to_id=to_id,
            to_lat=to_lat,
            to_lon=to_lon,
            sched_start=sched_start,
            sched_end=sched_end,
            mode=mode,
            scheduled=scheduled,
            from_level=from_level,
            to_level=to_level,
        )

        leg_id.additional_properties = d
        return leg_id

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
