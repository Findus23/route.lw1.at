from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mode import Mode
from ..models.route_path_source import RoutePathSource

if TYPE_CHECKING:
    from ..models.route_segment import RouteSegment
    from ..models.transit_route_info import TransitRouteInfo


T = TypeVar("T", bound="RouteInfo")


@_attrs_define
class RouteInfo:
    """
    Attributes:
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
        transit_routes (list[TransitRouteInfo]):
        num_stops (int): Number of stops along this route
        route_idx (int): Internal route index for debugging purposes
        path_source (RoutePathSource):
        segments (list[RouteSegment]):
    """

    mode: Mode
    transit_routes: list[TransitRouteInfo]
    num_stops: int
    route_idx: int
    path_source: RoutePathSource
    segments: list[RouteSegment]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        transit_routes = []
        for transit_routes_item_data in self.transit_routes:
            transit_routes_item = transit_routes_item_data.to_dict()
            transit_routes.append(transit_routes_item)

        num_stops = self.num_stops

        route_idx = self.route_idx

        path_source = self.path_source.value

        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "transitRoutes": transit_routes,
                "numStops": num_stops,
                "routeIdx": route_idx,
                "pathSource": path_source,
                "segments": segments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.route_segment import RouteSegment
        from ..models.transit_route_info import TransitRouteInfo

        d = dict(src_dict)
        mode = Mode(d.pop("mode"))

        transit_routes = []
        _transit_routes = d.pop("transitRoutes")
        for transit_routes_item_data in _transit_routes:
            transit_routes_item = TransitRouteInfo.from_dict(transit_routes_item_data)

            transit_routes.append(transit_routes_item)

        num_stops = d.pop("numStops")

        route_idx = d.pop("routeIdx")

        path_source = RoutePathSource(d.pop("pathSource"))

        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = RouteSegment.from_dict(segments_item_data)

            segments.append(segments_item)

        route_info = cls(
            mode=mode,
            transit_routes=transit_routes,
            num_stops=num_stops,
            route_idx=route_idx,
            path_source=path_source,
            segments=segments,
        )

        route_info.additional_properties = d
        return route_info

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
