from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elevation_costs import ElevationCosts
from ..models.mode import Mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="OneToManyParams")


@_attrs_define
class OneToManyParams:
    """
    Attributes:
        one (str): geo location as latitude;longitude
        many (list[str]): geo locations as latitude;longitude,latitude;longitude,...

            The number of accepted locations is limited by server config variable `onetomany_max_many`.
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
        max_ (float): maximum travel time in seconds. Is limited by server config variable
            `street_routing_max_direct_seconds`.
        max_matching_distance (float): maximum matching distance in meters to match geo coordinates to the street
            network
        arrive_by (bool): true = many to one
            false = one to many
        elevation_costs (ElevationCosts | Unset): Different elevation cost profiles for street routing.
            Using a elevation cost profile will prefer routes with a smaller incline and smaller difference in elevation,
            even if the routed way is longer.

            - `NONE`: Ignore elevation data for routing. This is the default behavior
            - `LOW`: Add a low penalty for inclines. This will favor longer paths, if the elevation increase and incline are
            smaller.
            - `HIGH`: Add a high penalty for inclines. This will favor even longer paths, if the elevation increase and
            incline are smaller.
        with_distance (bool | Unset): If true, the response includes the distance in meters
            for each path. This requires path reconstruction and
            may be slower than duration-only queries.
             Default: False.
    """

    one: str
    many: list[str]
    mode: Mode
    max_: float
    max_matching_distance: float
    arrive_by: bool
    elevation_costs: ElevationCosts | Unset = UNSET
    with_distance: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        one = self.one

        many = self.many

        mode = self.mode.value

        max_ = self.max_

        max_matching_distance = self.max_matching_distance

        arrive_by = self.arrive_by

        elevation_costs: str | Unset = UNSET
        if not isinstance(self.elevation_costs, Unset):
            elevation_costs = self.elevation_costs.value

        with_distance = self.with_distance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "one": one,
                "many": many,
                "mode": mode,
                "max": max_,
                "maxMatchingDistance": max_matching_distance,
                "arriveBy": arrive_by,
            }
        )
        if elevation_costs is not UNSET:
            field_dict["elevationCosts"] = elevation_costs
        if with_distance is not UNSET:
            field_dict["withDistance"] = with_distance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        one = d.pop("one")

        many = cast(list[str], d.pop("many"))

        mode = Mode(d.pop("mode"))

        max_ = d.pop("max")

        max_matching_distance = d.pop("maxMatchingDistance")

        arrive_by = d.pop("arriveBy")

        _elevation_costs = d.pop("elevationCosts", UNSET)
        elevation_costs: ElevationCosts | Unset
        if isinstance(_elevation_costs, Unset):
            elevation_costs = UNSET
        else:
            elevation_costs = ElevationCosts(_elevation_costs)

        with_distance = d.pop("withDistance", UNSET)

        one_to_many_params = cls(
            one=one,
            many=many,
            mode=mode,
            max_=max_,
            max_matching_distance=max_matching_distance,
            arrive_by=arrive_by,
            elevation_costs=elevation_costs,
            with_distance=with_distance,
        )

        one_to_many_params.additional_properties = d
        return one_to_many_params

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
