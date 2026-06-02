from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mode import Mode
from ..models.pickup_dropoff_type import PickupDropoffType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place import Place


T = TypeVar("T", bound="StopTime")


@_attrs_define
class StopTime:
    """departure or arrival event at a stop

    Attributes:
        place (Place):
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
        real_time (bool): Whether there is real-time data about this leg
        headsign (str): The headsign of the bus or train being used.
            For non-transit legs, null
        trip_from (Place):
        trip_to (Place):
        agency_id (str):
        agency_name (str):
        agency_url (str):
        route_id (str):
        direction_id (str):
        trip_id (str):
        route_short_name (str):
        route_long_name (str):
        trip_short_name (str):
        display_name (str):
        pickup_dropoff_type (PickupDropoffType): - `NORMAL` - entry/exit is possible normally
            - `NOT_ALLOWED` - entry/exit is not allowed
        cancelled (bool): Whether the departure/arrival is cancelled due to the realtime situation (either because the
            stop is skipped or because the entire trip is cancelled).
        trip_cancelled (bool): Whether the entire trip is cancelled due to the realtime situation.
        source (str): Filename and line number where this trip is from
        route_url (str | Unset):
        route_color (str | Unset):
        route_text_color (str | Unset):
        route_type (int | Unset):
        previous_stops (list[Place] | Unset): Experimental. Expect unannounced breaking changes (without version bumps).

            Stops on the trips before this stop. Returned only if `fetchStop` and `arriveBy` are `true`.
        next_stops (list[Place] | Unset): Experimental. Expect unannounced breaking changes (without version bumps).

            Stops on the trips after this stop. Returned only if `fetchStop` is `true` and `arriveBy` is `false`.
    """

    place: Place
    mode: Mode
    real_time: bool
    headsign: str
    trip_from: Place
    trip_to: Place
    agency_id: str
    agency_name: str
    agency_url: str
    route_id: str
    direction_id: str
    trip_id: str
    route_short_name: str
    route_long_name: str
    trip_short_name: str
    display_name: str
    pickup_dropoff_type: PickupDropoffType
    cancelled: bool
    trip_cancelled: bool
    source: str
    route_url: str | Unset = UNSET
    route_color: str | Unset = UNSET
    route_text_color: str | Unset = UNSET
    route_type: int | Unset = UNSET
    previous_stops: list[Place] | Unset = UNSET
    next_stops: list[Place] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        place = self.place.to_dict()

        mode = self.mode.value

        real_time = self.real_time

        headsign = self.headsign

        trip_from = self.trip_from.to_dict()

        trip_to = self.trip_to.to_dict()

        agency_id = self.agency_id

        agency_name = self.agency_name

        agency_url = self.agency_url

        route_id = self.route_id

        direction_id = self.direction_id

        trip_id = self.trip_id

        route_short_name = self.route_short_name

        route_long_name = self.route_long_name

        trip_short_name = self.trip_short_name

        display_name = self.display_name

        pickup_dropoff_type = self.pickup_dropoff_type.value

        cancelled = self.cancelled

        trip_cancelled = self.trip_cancelled

        source = self.source

        route_url = self.route_url

        route_color = self.route_color

        route_text_color = self.route_text_color

        route_type = self.route_type

        previous_stops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.previous_stops, Unset):
            previous_stops = []
            for previous_stops_item_data in self.previous_stops:
                previous_stops_item = previous_stops_item_data.to_dict()
                previous_stops.append(previous_stops_item)

        next_stops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.next_stops, Unset):
            next_stops = []
            for next_stops_item_data in self.next_stops:
                next_stops_item = next_stops_item_data.to_dict()
                next_stops.append(next_stops_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "place": place,
                "mode": mode,
                "realTime": real_time,
                "headsign": headsign,
                "tripFrom": trip_from,
                "tripTo": trip_to,
                "agencyId": agency_id,
                "agencyName": agency_name,
                "agencyUrl": agency_url,
                "routeId": route_id,
                "directionId": direction_id,
                "tripId": trip_id,
                "routeShortName": route_short_name,
                "routeLongName": route_long_name,
                "tripShortName": trip_short_name,
                "displayName": display_name,
                "pickupDropoffType": pickup_dropoff_type,
                "cancelled": cancelled,
                "tripCancelled": trip_cancelled,
                "source": source,
            }
        )
        if route_url is not UNSET:
            field_dict["routeUrl"] = route_url
        if route_color is not UNSET:
            field_dict["routeColor"] = route_color
        if route_text_color is not UNSET:
            field_dict["routeTextColor"] = route_text_color
        if route_type is not UNSET:
            field_dict["routeType"] = route_type
        if previous_stops is not UNSET:
            field_dict["previousStops"] = previous_stops
        if next_stops is not UNSET:
            field_dict["nextStops"] = next_stops

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place import Place

        d = dict(src_dict)
        place = Place.from_dict(d.pop("place"))

        mode = Mode(d.pop("mode"))

        real_time = d.pop("realTime")

        headsign = d.pop("headsign")

        trip_from = Place.from_dict(d.pop("tripFrom"))

        trip_to = Place.from_dict(d.pop("tripTo"))

        agency_id = d.pop("agencyId")

        agency_name = d.pop("agencyName")

        agency_url = d.pop("agencyUrl")

        route_id = d.pop("routeId")

        direction_id = d.pop("directionId")

        trip_id = d.pop("tripId")

        route_short_name = d.pop("routeShortName")

        route_long_name = d.pop("routeLongName")

        trip_short_name = d.pop("tripShortName")

        display_name = d.pop("displayName")

        pickup_dropoff_type = PickupDropoffType(d.pop("pickupDropoffType"))

        cancelled = d.pop("cancelled")

        trip_cancelled = d.pop("tripCancelled")

        source = d.pop("source")

        route_url = d.pop("routeUrl", UNSET)

        route_color = d.pop("routeColor", UNSET)

        route_text_color = d.pop("routeTextColor", UNSET)

        route_type = d.pop("routeType", UNSET)

        _previous_stops = d.pop("previousStops", UNSET)
        previous_stops: list[Place] | Unset = UNSET
        if _previous_stops is not UNSET:
            previous_stops = []
            for previous_stops_item_data in _previous_stops:
                previous_stops_item = Place.from_dict(previous_stops_item_data)

                previous_stops.append(previous_stops_item)

        _next_stops = d.pop("nextStops", UNSET)
        next_stops: list[Place] | Unset = UNSET
        if _next_stops is not UNSET:
            next_stops = []
            for next_stops_item_data in _next_stops:
                next_stops_item = Place.from_dict(next_stops_item_data)

                next_stops.append(next_stops_item)

        stop_time = cls(
            place=place,
            mode=mode,
            real_time=real_time,
            headsign=headsign,
            trip_from=trip_from,
            trip_to=trip_to,
            agency_id=agency_id,
            agency_name=agency_name,
            agency_url=agency_url,
            route_id=route_id,
            direction_id=direction_id,
            trip_id=trip_id,
            route_short_name=route_short_name,
            route_long_name=route_long_name,
            trip_short_name=trip_short_name,
            display_name=display_name,
            pickup_dropoff_type=pickup_dropoff_type,
            cancelled=cancelled,
            trip_cancelled=trip_cancelled,
            source=source,
            route_url=route_url,
            route_color=route_color,
            route_text_color=route_text_color,
            route_type=route_type,
            previous_stops=previous_stops,
            next_stops=next_stops,
        )

        stop_time.additional_properties = d
        return stop_time

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
