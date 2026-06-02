from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elevation_costs import ElevationCosts
from ..models.mode import Mode
from ..models.pedestrian_profile import PedestrianProfile
from ..types import UNSET, Unset

T = TypeVar("T", bound="OneToManyIntermodalParams")


@_attrs_define
class OneToManyIntermodalParams:
    r"""
    Attributes:
        one (str): \`latitude,longitude[,level]\` tuple with
            - latitude and longitude in degrees
            - (optional) level: the OSM level (default: 0)

            OR

            stop id
        many (list[str]): array of:

            \`latitude,longitude[,level]\` tuple with
            - latitude and longitude in degrees
            - (optional) level: the OSM level (default: 0)

            OR

            stop id

            The number of accepted locations is limited by server config variable `onetomany_max_many`.
        time (datetime.datetime | Unset): Optional. Defaults to the current time.

            Departure time ($arriveBy=false) / arrival date ($arriveBy=true),
        max_travel_time (int | Unset): The maximum travel time in minutes.
            If not provided, the routing uses the value
            hardcoded in the server which is usually quite high.

            *Warning*: Use with care. Setting this too low can lead to
            optimal (e.g. the least transfers) journeys not being found.
            If this value is too low to reach the destination at all,
            it can lead to slow routing performance.
        max_matching_distance (float | Unset): maximum matching distance in meters to match geo coordinates to the
            street network Default: 25.0.
        arrive_by (bool | Unset): Optional. Defaults to false, i.e. one to many search

            true = many to one
            false = one to many
             Default: False.
        max_transfers (int | Unset): The maximum number of allowed transfers (i.e. interchanges between transit legs,
            pre- and postTransit do not count as transfers).
            `maxTransfers=0` searches for direct transit connections without any transfers.
            If you want to search only for non-transit connections (`FOOT`, `CAR`, etc.),
            send an empty `transitModes` parameter instead.

            If not provided, the routing uses the server-side default value
            which is hardcoded and very high to cover all use cases.

            *Warning*: Use with care. Setting this too low can lead to
            optimal (e.g. the fastest) journeys not being found.
            If this value is too low to reach the destination at all,
            it can lead to slow routing performance.
        min_transfer_time (int | Unset): Optional. Default is 0 minutes.

            Minimum transfer time for each transfer in minutes.
             Default: 0.
        additional_transfer_time (int | Unset): Optional. Default is 0 minutes.

            Additional transfer time reserved for each transfer in minutes.
             Default: 0.
        transfer_time_factor (float | Unset): Optional. Default is 1.0

            Factor to multiply minimum required transfer times with.
            Values smaller than 1.0 are not supported.
             Default: 1.0.
        use_routed_transfers (bool | Unset): Optional. Default is `false`.

            Whether to use transfers routed on OpenStreetMap data.
             Default: False.
        pedestrian_profile (PedestrianProfile | Unset): Different accessibility profiles for pedestrians.
        pedestrian_speed (float | Unset): Average speed for pedestrian routing in meters per second
        cycling_speed (float | Unset): Average speed for bike routing in meters per second
        elevation_costs (ElevationCosts | Unset): Different elevation cost profiles for street routing.
            Using a elevation cost profile will prefer routes with a smaller incline and smaller difference in elevation,
            even if the routed way is longer.

            - `NONE`: Ignore elevation data for routing. This is the default behavior
            - `LOW`: Add a low penalty for inclines. This will favor longer paths, if the elevation increase and incline are
            smaller.
            - `HIGH`: Add a high penalty for inclines. This will favor even longer paths, if the elevation increase and
            incline are smaller.
        transit_modes (list[Mode] | Unset): Optional. Default is `TRANSIT` which allows all transit modes (no
            restriction).
            Allowed modes for the transit part. If empty, no transit connections will be computed.
            For example, this can be used to allow only `SUBURBAN,SUBWAY,TRAM`.
        pre_transit_modes (list[Mode] | Unset): Optional. Default is `WALK`. Does not apply to direct connections (see
            `directMode`).

            A list of modes that are allowed to be used for the first mile, i.e. from the coordinates to the first transit
            stop. Example: `WALK,BIKE_SHARING`.
        post_transit_modes (list[Mode] | Unset): Optional. Default is `WALK`. Does not apply to direct connections (see
            `directMode`).

            A list of modes that are allowed to be used for the last mile, i.e. from the last transit stop to the target
            coordinates. Example: `WALK,BIKE_SHARING`.
        direct_mode (Mode | Unset): # Street modes

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
        max_pre_transit_time (int | Unset): Optional. Default is 15min which is `900`.
            Maximum time in seconds for the first street leg.
            Is limited by server config variable `street_routing_max_prepost_transit_seconds`.
             Default: 900.
        max_post_transit_time (int | Unset): Optional. Default is 15min which is `900`.
            Maximum time in seconds for the last street leg.
            Is limited by server config variable `street_routing_max_prepost_transit_seconds`.
             Default: 900.
        max_direct_time (int | Unset): Optional. Default is 30min which is `1800`.
            Maximum time in seconds for direct connections.

            If a value smaller than either `maxPreTransitTime` or
            `maxPostTransitTime` is used, their maximum is set instead.
            Is limited by server config variable `street_routing_max_direct_seconds`.
             Default: 1800.
        with_distance (bool | Unset): If true, the response includes the distance in meters
            for each path. This requires path reconstruction and
            may be slower than duration-only queries.

            `withDistance` is currently limited to street routing.
             Default: False.
        require_bike_transport (bool | Unset): Optional. Default is `false`.

            If set to `true`, all used transit trips are required to allow bike carriage.
             Default: False.
        require_car_transport (bool | Unset): Optional. Default is `false`.

            If set to `true`, all used transit trips are required to allow car carriage.
             Default: False.
    """

    one: str
    many: list[str]
    time: datetime.datetime | Unset = UNSET
    max_travel_time: int | Unset = UNSET
    max_matching_distance: float | Unset = 25.0
    arrive_by: bool | Unset = False
    max_transfers: int | Unset = UNSET
    min_transfer_time: int | Unset = 0
    additional_transfer_time: int | Unset = 0
    transfer_time_factor: float | Unset = 1.0
    use_routed_transfers: bool | Unset = False
    pedestrian_profile: PedestrianProfile | Unset = UNSET
    pedestrian_speed: float | Unset = UNSET
    cycling_speed: float | Unset = UNSET
    elevation_costs: ElevationCosts | Unset = UNSET
    transit_modes: list[Mode] | Unset = UNSET
    pre_transit_modes: list[Mode] | Unset = UNSET
    post_transit_modes: list[Mode] | Unset = UNSET
    direct_mode: Mode | Unset = UNSET
    max_pre_transit_time: int | Unset = 900
    max_post_transit_time: int | Unset = 900
    max_direct_time: int | Unset = 1800
    with_distance: bool | Unset = False
    require_bike_transport: bool | Unset = False
    require_car_transport: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        one = self.one

        many = self.many

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        max_travel_time = self.max_travel_time

        max_matching_distance = self.max_matching_distance

        arrive_by = self.arrive_by

        max_transfers = self.max_transfers

        min_transfer_time = self.min_transfer_time

        additional_transfer_time = self.additional_transfer_time

        transfer_time_factor = self.transfer_time_factor

        use_routed_transfers = self.use_routed_transfers

        pedestrian_profile: str | Unset = UNSET
        if not isinstance(self.pedestrian_profile, Unset):
            pedestrian_profile = self.pedestrian_profile.value

        pedestrian_speed = self.pedestrian_speed

        cycling_speed = self.cycling_speed

        elevation_costs: str | Unset = UNSET
        if not isinstance(self.elevation_costs, Unset):
            elevation_costs = self.elevation_costs.value

        transit_modes: list[str] | Unset = UNSET
        if not isinstance(self.transit_modes, Unset):
            transit_modes = []
            for transit_modes_item_data in self.transit_modes:
                transit_modes_item = transit_modes_item_data.value
                transit_modes.append(transit_modes_item)

        pre_transit_modes: list[str] | Unset = UNSET
        if not isinstance(self.pre_transit_modes, Unset):
            pre_transit_modes = []
            for pre_transit_modes_item_data in self.pre_transit_modes:
                pre_transit_modes_item = pre_transit_modes_item_data.value
                pre_transit_modes.append(pre_transit_modes_item)

        post_transit_modes: list[str] | Unset = UNSET
        if not isinstance(self.post_transit_modes, Unset):
            post_transit_modes = []
            for post_transit_modes_item_data in self.post_transit_modes:
                post_transit_modes_item = post_transit_modes_item_data.value
                post_transit_modes.append(post_transit_modes_item)

        direct_mode: str | Unset = UNSET
        if not isinstance(self.direct_mode, Unset):
            direct_mode = self.direct_mode.value

        max_pre_transit_time = self.max_pre_transit_time

        max_post_transit_time = self.max_post_transit_time

        max_direct_time = self.max_direct_time

        with_distance = self.with_distance

        require_bike_transport = self.require_bike_transport

        require_car_transport = self.require_car_transport

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "one": one,
                "many": many,
            }
        )
        if time is not UNSET:
            field_dict["time"] = time
        if max_travel_time is not UNSET:
            field_dict["maxTravelTime"] = max_travel_time
        if max_matching_distance is not UNSET:
            field_dict["maxMatchingDistance"] = max_matching_distance
        if arrive_by is not UNSET:
            field_dict["arriveBy"] = arrive_by
        if max_transfers is not UNSET:
            field_dict["maxTransfers"] = max_transfers
        if min_transfer_time is not UNSET:
            field_dict["minTransferTime"] = min_transfer_time
        if additional_transfer_time is not UNSET:
            field_dict["additionalTransferTime"] = additional_transfer_time
        if transfer_time_factor is not UNSET:
            field_dict["transferTimeFactor"] = transfer_time_factor
        if use_routed_transfers is not UNSET:
            field_dict["useRoutedTransfers"] = use_routed_transfers
        if pedestrian_profile is not UNSET:
            field_dict["pedestrianProfile"] = pedestrian_profile
        if pedestrian_speed is not UNSET:
            field_dict["pedestrianSpeed"] = pedestrian_speed
        if cycling_speed is not UNSET:
            field_dict["cyclingSpeed"] = cycling_speed
        if elevation_costs is not UNSET:
            field_dict["elevationCosts"] = elevation_costs
        if transit_modes is not UNSET:
            field_dict["transitModes"] = transit_modes
        if pre_transit_modes is not UNSET:
            field_dict["preTransitModes"] = pre_transit_modes
        if post_transit_modes is not UNSET:
            field_dict["postTransitModes"] = post_transit_modes
        if direct_mode is not UNSET:
            field_dict["directMode"] = direct_mode
        if max_pre_transit_time is not UNSET:
            field_dict["maxPreTransitTime"] = max_pre_transit_time
        if max_post_transit_time is not UNSET:
            field_dict["maxPostTransitTime"] = max_post_transit_time
        if max_direct_time is not UNSET:
            field_dict["maxDirectTime"] = max_direct_time
        if with_distance is not UNSET:
            field_dict["withDistance"] = with_distance
        if require_bike_transport is not UNSET:
            field_dict["requireBikeTransport"] = require_bike_transport
        if require_car_transport is not UNSET:
            field_dict["requireCarTransport"] = require_car_transport

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        one = d.pop("one")

        many = cast(list[str], d.pop("many"))

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = datetime.datetime.fromisoformat(_time)

        max_travel_time = d.pop("maxTravelTime", UNSET)

        max_matching_distance = d.pop("maxMatchingDistance", UNSET)

        arrive_by = d.pop("arriveBy", UNSET)

        max_transfers = d.pop("maxTransfers", UNSET)

        min_transfer_time = d.pop("minTransferTime", UNSET)

        additional_transfer_time = d.pop("additionalTransferTime", UNSET)

        transfer_time_factor = d.pop("transferTimeFactor", UNSET)

        use_routed_transfers = d.pop("useRoutedTransfers", UNSET)

        _pedestrian_profile = d.pop("pedestrianProfile", UNSET)
        pedestrian_profile: PedestrianProfile | Unset
        if isinstance(_pedestrian_profile, Unset):
            pedestrian_profile = UNSET
        else:
            pedestrian_profile = PedestrianProfile(_pedestrian_profile)

        pedestrian_speed = d.pop("pedestrianSpeed", UNSET)

        cycling_speed = d.pop("cyclingSpeed", UNSET)

        _elevation_costs = d.pop("elevationCosts", UNSET)
        elevation_costs: ElevationCosts | Unset
        if isinstance(_elevation_costs, Unset):
            elevation_costs = UNSET
        else:
            elevation_costs = ElevationCosts(_elevation_costs)

        _transit_modes = d.pop("transitModes", UNSET)
        transit_modes: list[Mode] | Unset = UNSET
        if _transit_modes is not UNSET:
            transit_modes = []
            for transit_modes_item_data in _transit_modes:
                transit_modes_item = Mode(transit_modes_item_data)

                transit_modes.append(transit_modes_item)

        _pre_transit_modes = d.pop("preTransitModes", UNSET)
        pre_transit_modes: list[Mode] | Unset = UNSET
        if _pre_transit_modes is not UNSET:
            pre_transit_modes = []
            for pre_transit_modes_item_data in _pre_transit_modes:
                pre_transit_modes_item = Mode(pre_transit_modes_item_data)

                pre_transit_modes.append(pre_transit_modes_item)

        _post_transit_modes = d.pop("postTransitModes", UNSET)
        post_transit_modes: list[Mode] | Unset = UNSET
        if _post_transit_modes is not UNSET:
            post_transit_modes = []
            for post_transit_modes_item_data in _post_transit_modes:
                post_transit_modes_item = Mode(post_transit_modes_item_data)

                post_transit_modes.append(post_transit_modes_item)

        _direct_mode = d.pop("directMode", UNSET)
        direct_mode: Mode | Unset
        if isinstance(_direct_mode, Unset):
            direct_mode = UNSET
        else:
            direct_mode = Mode(_direct_mode)

        max_pre_transit_time = d.pop("maxPreTransitTime", UNSET)

        max_post_transit_time = d.pop("maxPostTransitTime", UNSET)

        max_direct_time = d.pop("maxDirectTime", UNSET)

        with_distance = d.pop("withDistance", UNSET)

        require_bike_transport = d.pop("requireBikeTransport", UNSET)

        require_car_transport = d.pop("requireCarTransport", UNSET)

        one_to_many_intermodal_params = cls(
            one=one,
            many=many,
            time=time,
            max_travel_time=max_travel_time,
            max_matching_distance=max_matching_distance,
            arrive_by=arrive_by,
            max_transfers=max_transfers,
            min_transfer_time=min_transfer_time,
            additional_transfer_time=additional_transfer_time,
            transfer_time_factor=transfer_time_factor,
            use_routed_transfers=use_routed_transfers,
            pedestrian_profile=pedestrian_profile,
            pedestrian_speed=pedestrian_speed,
            cycling_speed=cycling_speed,
            elevation_costs=elevation_costs,
            transit_modes=transit_modes,
            pre_transit_modes=pre_transit_modes,
            post_transit_modes=post_transit_modes,
            direct_mode=direct_mode,
            max_pre_transit_time=max_pre_transit_time,
            max_post_transit_time=max_post_transit_time,
            max_direct_time=max_direct_time,
            with_distance=with_distance,
            require_bike_transport=require_bike_transport,
            require_car_transport=require_car_transport,
        )

        one_to_many_intermodal_params.additional_properties = d
        return one_to_many_intermodal_params

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
