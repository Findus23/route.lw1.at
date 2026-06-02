from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mode import Mode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place import Place
    from ..models.trip_info import TripInfo


T = TypeVar("T", bound="TripSegment")


@_attrs_define
class TripSegment:
    """trip segment between two stops to show a trip on a map

    Attributes:
        trips (list[TripInfo]):
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
        distance (float): distance in meters
        from_ (Place):
        to (Place):
        departure (datetime.datetime): departure time
        arrival (datetime.datetime): arrival time
        scheduled_departure (datetime.datetime): scheduled departure time
        scheduled_arrival (datetime.datetime): scheduled arrival time
        real_time (bool): Whether there is real-time data about this leg
        polyline (str): Google polyline encoded coordinate sequence (with precision 5) where the trip travels on this
            segment.
        route_color (str | Unset):
    """

    trips: list[TripInfo]
    mode: Mode
    distance: float
    from_: Place
    to: Place
    departure: datetime.datetime
    arrival: datetime.datetime
    scheduled_departure: datetime.datetime
    scheduled_arrival: datetime.datetime
    real_time: bool
    polyline: str
    route_color: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trips = []
        for trips_item_data in self.trips:
            trips_item = trips_item_data.to_dict()
            trips.append(trips_item)

        mode = self.mode.value

        distance = self.distance

        from_ = self.from_.to_dict()

        to = self.to.to_dict()

        departure = self.departure.isoformat()

        arrival = self.arrival.isoformat()

        scheduled_departure = self.scheduled_departure.isoformat()

        scheduled_arrival = self.scheduled_arrival.isoformat()

        real_time = self.real_time

        polyline = self.polyline

        route_color = self.route_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trips": trips,
                "mode": mode,
                "distance": distance,
                "from": from_,
                "to": to,
                "departure": departure,
                "arrival": arrival,
                "scheduledDeparture": scheduled_departure,
                "scheduledArrival": scheduled_arrival,
                "realTime": real_time,
                "polyline": polyline,
            }
        )
        if route_color is not UNSET:
            field_dict["routeColor"] = route_color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place import Place
        from ..models.trip_info import TripInfo

        d = dict(src_dict)
        trips = []
        _trips = d.pop("trips")
        for trips_item_data in _trips:
            trips_item = TripInfo.from_dict(trips_item_data)

            trips.append(trips_item)

        mode = Mode(d.pop("mode"))

        distance = d.pop("distance")

        from_ = Place.from_dict(d.pop("from"))

        to = Place.from_dict(d.pop("to"))

        departure = datetime.datetime.fromisoformat(d.pop("departure"))

        arrival = datetime.datetime.fromisoformat(d.pop("arrival"))

        scheduled_departure = datetime.datetime.fromisoformat(d.pop("scheduledDeparture"))

        scheduled_arrival = datetime.datetime.fromisoformat(d.pop("scheduledArrival"))

        real_time = d.pop("realTime")

        polyline = d.pop("polyline")

        route_color = d.pop("routeColor", UNSET)

        trip_segment = cls(
            trips=trips,
            mode=mode,
            distance=distance,
            from_=from_,
            to=to,
            departure=departure,
            arrival=arrival,
            scheduled_departure=scheduled_departure,
            scheduled_arrival=scheduled_arrival,
            real_time=real_time,
            polyline=polyline,
            route_color=route_color,
        )

        trip_segment.additional_properties = d
        return trip_segment

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
