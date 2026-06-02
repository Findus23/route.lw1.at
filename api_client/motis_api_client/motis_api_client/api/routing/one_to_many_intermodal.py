import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.elevation_costs import ElevationCosts
from ...models.error import Error
from ...models.mode import Mode
from ...models.one_to_many_intermodal_response import OneToManyIntermodalResponse
from ...models.pedestrian_profile import PedestrianProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    one: str,
    many: list[str],
    time: datetime.datetime | Unset = UNSET,
    max_travel_time: int | Unset = UNSET,
    max_matching_distance: float | Unset = 25.0,
    arrive_by: bool | Unset = False,
    max_transfers: int | Unset = UNSET,
    min_transfer_time: int | Unset = 0,
    additional_transfer_time: int | Unset = 0,
    transfer_time_factor: float | Unset = 1.0,
    use_routed_transfers: bool | Unset = False,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    pedestrian_speed: float | Unset = UNSET,
    cycling_speed: float | Unset = UNSET,
    elevation_costs: ElevationCosts | Unset = UNSET,
    transit_modes: list[Mode] | Unset = UNSET,
    pre_transit_modes: list[Mode] | Unset = UNSET,
    post_transit_modes: list[Mode] | Unset = UNSET,
    direct_mode: Mode | Unset = UNSET,
    max_pre_transit_time: int | Unset = 900,
    max_post_transit_time: int | Unset = 900,
    max_direct_time: int | Unset = 1800,
    with_distance: bool | Unset = False,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["one"] = one

    json_many = many

    params["many"] = json_many

    json_time: str | Unset = UNSET
    if not isinstance(time, Unset):
        json_time = time.isoformat()
    params["time"] = json_time

    params["maxTravelTime"] = max_travel_time

    params["maxMatchingDistance"] = max_matching_distance

    params["arriveBy"] = arrive_by

    params["maxTransfers"] = max_transfers

    params["minTransferTime"] = min_transfer_time

    params["additionalTransferTime"] = additional_transfer_time

    params["transferTimeFactor"] = transfer_time_factor

    params["useRoutedTransfers"] = use_routed_transfers

    json_pedestrian_profile: str | Unset = UNSET
    if not isinstance(pedestrian_profile, Unset):
        json_pedestrian_profile = pedestrian_profile.value

    params["pedestrianProfile"] = json_pedestrian_profile

    params["pedestrianSpeed"] = pedestrian_speed

    params["cyclingSpeed"] = cycling_speed

    json_elevation_costs: str | Unset = UNSET
    if not isinstance(elevation_costs, Unset):
        json_elevation_costs = elevation_costs.value

    params["elevationCosts"] = json_elevation_costs

    json_transit_modes: list[str] | Unset = UNSET
    if not isinstance(transit_modes, Unset):
        json_transit_modes = []
        for transit_modes_item_data in transit_modes:
            transit_modes_item = transit_modes_item_data.value
            json_transit_modes.append(transit_modes_item)

    params["transitModes"] = json_transit_modes

    json_pre_transit_modes: list[str] | Unset = UNSET
    if not isinstance(pre_transit_modes, Unset):
        json_pre_transit_modes = []
        for pre_transit_modes_item_data in pre_transit_modes:
            pre_transit_modes_item = pre_transit_modes_item_data.value
            json_pre_transit_modes.append(pre_transit_modes_item)

    params["preTransitModes"] = json_pre_transit_modes

    json_post_transit_modes: list[str] | Unset = UNSET
    if not isinstance(post_transit_modes, Unset):
        json_post_transit_modes = []
        for post_transit_modes_item_data in post_transit_modes:
            post_transit_modes_item = post_transit_modes_item_data.value
            json_post_transit_modes.append(post_transit_modes_item)

    params["postTransitModes"] = json_post_transit_modes

    json_direct_mode: str | Unset = UNSET
    if not isinstance(direct_mode, Unset):
        json_direct_mode = direct_mode.value

    params["directMode"] = json_direct_mode

    params["maxPreTransitTime"] = max_pre_transit_time

    params["maxPostTransitTime"] = max_post_transit_time

    params["maxDirectTime"] = max_direct_time

    params["withDistance"] = with_distance

    params["requireBikeTransport"] = require_bike_transport

    params["requireCarTransport"] = require_car_transport

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/experimental/one-to-many-intermodal",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | OneToManyIntermodalResponse | None:
    if response.status_code == 200:
        response_200 = OneToManyIntermodalResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | OneToManyIntermodalResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    one: str,
    many: list[str],
    time: datetime.datetime | Unset = UNSET,
    max_travel_time: int | Unset = UNSET,
    max_matching_distance: float | Unset = 25.0,
    arrive_by: bool | Unset = False,
    max_transfers: int | Unset = UNSET,
    min_transfer_time: int | Unset = 0,
    additional_transfer_time: int | Unset = 0,
    transfer_time_factor: float | Unset = 1.0,
    use_routed_transfers: bool | Unset = False,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    pedestrian_speed: float | Unset = UNSET,
    cycling_speed: float | Unset = UNSET,
    elevation_costs: ElevationCosts | Unset = UNSET,
    transit_modes: list[Mode] | Unset = UNSET,
    pre_transit_modes: list[Mode] | Unset = UNSET,
    post_transit_modes: list[Mode] | Unset = UNSET,
    direct_mode: Mode | Unset = UNSET,
    max_pre_transit_time: int | Unset = 900,
    max_post_transit_time: int | Unset = 900,
    max_direct_time: int | Unset = 1800,
    with_distance: bool | Unset = False,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
) -> Response[Error | OneToManyIntermodalResponse]:
    r"""One to many routing
    Computes the minimal duration from one place to many or vice versa.
    The order in the response array corresponds to the order of coordinates of the \`many\` parameter in
    the query.

    Args:
        one (str):
        many (list[str]):
        time (datetime.datetime | Unset):
        max_travel_time (int | Unset):
        max_matching_distance (float | Unset):  Default: 25.0.
        arrive_by (bool | Unset):  Default: False.
        max_transfers (int | Unset):
        min_transfer_time (int | Unset):  Default: 0.
        additional_transfer_time (int | Unset):  Default: 0.
        transfer_time_factor (float | Unset):  Default: 1.0.
        use_routed_transfers (bool | Unset):  Default: False.
        pedestrian_profile (PedestrianProfile | Unset): Different accessibility profiles for
            pedestrians.
        pedestrian_speed (float | Unset): Average speed for pedestrian routing in meters per
            second
        cycling_speed (float | Unset): Average speed for bike routing in meters per second
        elevation_costs (ElevationCosts | Unset): Different elevation cost profiles for street
            routing.
            Using a elevation cost profile will prefer routes with a smaller incline and smaller
            difference in elevation, even if the routed way is longer.

            - `NONE`: Ignore elevation data for routing. This is the default behavior
            - `LOW`: Add a low penalty for inclines. This will favor longer paths, if the elevation
            increase and incline are smaller.
            - `HIGH`: Add a high penalty for inclines. This will favor even longer paths, if the
            elevation increase and incline are smaller.
        transit_modes (list[Mode] | Unset):
        pre_transit_modes (list[Mode] | Unset):
        post_transit_modes (list[Mode] | Unset):
        direct_mode (Mode | Unset): # Street modes

              - `WALK`
              - `BIKE`
              - `RENTAL` Experimental. Expect unannounced breaking changes (without version bumps) for
            all parameters and returned structs.
              - `CAR`
              - `CAR_PARKING` Experimental. Expect unannounced breaking changes (without version
            bumps) for all parameters and returned structs.
              - `CAR_DROPOFF` Experimental. Expect unannounced breaking changes (without version
            bumps) for all perameters and returned structs.
              - `ODM` on-demand taxis from the Prima+ÖV Project
              - `RIDE_SHARING` ride sharing from the Prima+ÖV Project
              - `FLEX` flexible transports

            # Transit modes

              - `TRANSIT`: translates to
            `TRAM,FERRY,AIRPLANE,BUS,COACH,RAIL,ODM,RIDE_SHARING,FUNICULAR,AERIAL_LIFT,OTHER`
              - `TRAM`: trams
              - `SUBWAY`: subway trains (Paris Metro, London Underground, but also NYC Subway,
            Hamburger Hochbahn, and other non-underground services)
              - `FERRY`: ferries
              - `AIRPLANE`: airline flights
              - `BUS`: short distance buses (does not include `COACH`)
              - `COACH`: long distance buses (does not include `BUS`)
              - `RAIL`: translates to
            `HIGHSPEED_RAIL,LONG_DISTANCE,NIGHT_RAIL,REGIONAL_RAIL,SUBURBAN,SUBWAY`
              - `HIGHSPEED_RAIL`: long distance high speed trains (e.g. TGV)
              - `LONG_DISTANCE`: long distance inter city trains
              - `NIGHT_RAIL`: long distance night trains
              - `REGIONAL_FAST_RAIL`: deprecated, `REGIONAL_RAIL` will be used
              - `REGIONAL_RAIL`: regional train
              - `SUBURBAN`: suburban trains (e.g. S-Bahn, RER, Elizabeth Line, ...)
              - `ODM`: demand responsive transport
              - `RIDE_SHARING`: ride sharing
              - `FUNICULAR`: Funicular. Any rail system designed for steep inclines.
              - `AERIAL_LIFT`: Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway).
            Cable transport where cabins, cars, gondolas or open chairs are suspended by means of one
            or more cables.
              - `AREAL_LIFT`: deprecated
              - `METRO`: deprecated
              - `CABLE_CAR`: deprecated
        max_pre_transit_time (int | Unset):  Default: 900.
        max_post_transit_time (int | Unset):  Default: 900.
        max_direct_time (int | Unset):  Default: 1800.
        with_distance (bool | Unset):  Default: False.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OneToManyIntermodalResponse]
    """

    kwargs = _get_kwargs(
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

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    one: str,
    many: list[str],
    time: datetime.datetime | Unset = UNSET,
    max_travel_time: int | Unset = UNSET,
    max_matching_distance: float | Unset = 25.0,
    arrive_by: bool | Unset = False,
    max_transfers: int | Unset = UNSET,
    min_transfer_time: int | Unset = 0,
    additional_transfer_time: int | Unset = 0,
    transfer_time_factor: float | Unset = 1.0,
    use_routed_transfers: bool | Unset = False,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    pedestrian_speed: float | Unset = UNSET,
    cycling_speed: float | Unset = UNSET,
    elevation_costs: ElevationCosts | Unset = UNSET,
    transit_modes: list[Mode] | Unset = UNSET,
    pre_transit_modes: list[Mode] | Unset = UNSET,
    post_transit_modes: list[Mode] | Unset = UNSET,
    direct_mode: Mode | Unset = UNSET,
    max_pre_transit_time: int | Unset = 900,
    max_post_transit_time: int | Unset = 900,
    max_direct_time: int | Unset = 1800,
    with_distance: bool | Unset = False,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
) -> Error | OneToManyIntermodalResponse | None:
    r"""One to many routing
    Computes the minimal duration from one place to many or vice versa.
    The order in the response array corresponds to the order of coordinates of the \`many\` parameter in
    the query.

    Args:
        one (str):
        many (list[str]):
        time (datetime.datetime | Unset):
        max_travel_time (int | Unset):
        max_matching_distance (float | Unset):  Default: 25.0.
        arrive_by (bool | Unset):  Default: False.
        max_transfers (int | Unset):
        min_transfer_time (int | Unset):  Default: 0.
        additional_transfer_time (int | Unset):  Default: 0.
        transfer_time_factor (float | Unset):  Default: 1.0.
        use_routed_transfers (bool | Unset):  Default: False.
        pedestrian_profile (PedestrianProfile | Unset): Different accessibility profiles for
            pedestrians.
        pedestrian_speed (float | Unset): Average speed for pedestrian routing in meters per
            second
        cycling_speed (float | Unset): Average speed for bike routing in meters per second
        elevation_costs (ElevationCosts | Unset): Different elevation cost profiles for street
            routing.
            Using a elevation cost profile will prefer routes with a smaller incline and smaller
            difference in elevation, even if the routed way is longer.

            - `NONE`: Ignore elevation data for routing. This is the default behavior
            - `LOW`: Add a low penalty for inclines. This will favor longer paths, if the elevation
            increase and incline are smaller.
            - `HIGH`: Add a high penalty for inclines. This will favor even longer paths, if the
            elevation increase and incline are smaller.
        transit_modes (list[Mode] | Unset):
        pre_transit_modes (list[Mode] | Unset):
        post_transit_modes (list[Mode] | Unset):
        direct_mode (Mode | Unset): # Street modes

              - `WALK`
              - `BIKE`
              - `RENTAL` Experimental. Expect unannounced breaking changes (without version bumps) for
            all parameters and returned structs.
              - `CAR`
              - `CAR_PARKING` Experimental. Expect unannounced breaking changes (without version
            bumps) for all parameters and returned structs.
              - `CAR_DROPOFF` Experimental. Expect unannounced breaking changes (without version
            bumps) for all perameters and returned structs.
              - `ODM` on-demand taxis from the Prima+ÖV Project
              - `RIDE_SHARING` ride sharing from the Prima+ÖV Project
              - `FLEX` flexible transports

            # Transit modes

              - `TRANSIT`: translates to
            `TRAM,FERRY,AIRPLANE,BUS,COACH,RAIL,ODM,RIDE_SHARING,FUNICULAR,AERIAL_LIFT,OTHER`
              - `TRAM`: trams
              - `SUBWAY`: subway trains (Paris Metro, London Underground, but also NYC Subway,
            Hamburger Hochbahn, and other non-underground services)
              - `FERRY`: ferries
              - `AIRPLANE`: airline flights
              - `BUS`: short distance buses (does not include `COACH`)
              - `COACH`: long distance buses (does not include `BUS`)
              - `RAIL`: translates to
            `HIGHSPEED_RAIL,LONG_DISTANCE,NIGHT_RAIL,REGIONAL_RAIL,SUBURBAN,SUBWAY`
              - `HIGHSPEED_RAIL`: long distance high speed trains (e.g. TGV)
              - `LONG_DISTANCE`: long distance inter city trains
              - `NIGHT_RAIL`: long distance night trains
              - `REGIONAL_FAST_RAIL`: deprecated, `REGIONAL_RAIL` will be used
              - `REGIONAL_RAIL`: regional train
              - `SUBURBAN`: suburban trains (e.g. S-Bahn, RER, Elizabeth Line, ...)
              - `ODM`: demand responsive transport
              - `RIDE_SHARING`: ride sharing
              - `FUNICULAR`: Funicular. Any rail system designed for steep inclines.
              - `AERIAL_LIFT`: Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway).
            Cable transport where cabins, cars, gondolas or open chairs are suspended by means of one
            or more cables.
              - `AREAL_LIFT`: deprecated
              - `METRO`: deprecated
              - `CABLE_CAR`: deprecated
        max_pre_transit_time (int | Unset):  Default: 900.
        max_post_transit_time (int | Unset):  Default: 900.
        max_direct_time (int | Unset):  Default: 1800.
        with_distance (bool | Unset):  Default: False.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OneToManyIntermodalResponse
    """

    return sync_detailed(
        client=client,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    one: str,
    many: list[str],
    time: datetime.datetime | Unset = UNSET,
    max_travel_time: int | Unset = UNSET,
    max_matching_distance: float | Unset = 25.0,
    arrive_by: bool | Unset = False,
    max_transfers: int | Unset = UNSET,
    min_transfer_time: int | Unset = 0,
    additional_transfer_time: int | Unset = 0,
    transfer_time_factor: float | Unset = 1.0,
    use_routed_transfers: bool | Unset = False,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    pedestrian_speed: float | Unset = UNSET,
    cycling_speed: float | Unset = UNSET,
    elevation_costs: ElevationCosts | Unset = UNSET,
    transit_modes: list[Mode] | Unset = UNSET,
    pre_transit_modes: list[Mode] | Unset = UNSET,
    post_transit_modes: list[Mode] | Unset = UNSET,
    direct_mode: Mode | Unset = UNSET,
    max_pre_transit_time: int | Unset = 900,
    max_post_transit_time: int | Unset = 900,
    max_direct_time: int | Unset = 1800,
    with_distance: bool | Unset = False,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
) -> Response[Error | OneToManyIntermodalResponse]:
    r"""One to many routing
    Computes the minimal duration from one place to many or vice versa.
    The order in the response array corresponds to the order of coordinates of the \`many\` parameter in
    the query.

    Args:
        one (str):
        many (list[str]):
        time (datetime.datetime | Unset):
        max_travel_time (int | Unset):
        max_matching_distance (float | Unset):  Default: 25.0.
        arrive_by (bool | Unset):  Default: False.
        max_transfers (int | Unset):
        min_transfer_time (int | Unset):  Default: 0.
        additional_transfer_time (int | Unset):  Default: 0.
        transfer_time_factor (float | Unset):  Default: 1.0.
        use_routed_transfers (bool | Unset):  Default: False.
        pedestrian_profile (PedestrianProfile | Unset): Different accessibility profiles for
            pedestrians.
        pedestrian_speed (float | Unset): Average speed for pedestrian routing in meters per
            second
        cycling_speed (float | Unset): Average speed for bike routing in meters per second
        elevation_costs (ElevationCosts | Unset): Different elevation cost profiles for street
            routing.
            Using a elevation cost profile will prefer routes with a smaller incline and smaller
            difference in elevation, even if the routed way is longer.

            - `NONE`: Ignore elevation data for routing. This is the default behavior
            - `LOW`: Add a low penalty for inclines. This will favor longer paths, if the elevation
            increase and incline are smaller.
            - `HIGH`: Add a high penalty for inclines. This will favor even longer paths, if the
            elevation increase and incline are smaller.
        transit_modes (list[Mode] | Unset):
        pre_transit_modes (list[Mode] | Unset):
        post_transit_modes (list[Mode] | Unset):
        direct_mode (Mode | Unset): # Street modes

              - `WALK`
              - `BIKE`
              - `RENTAL` Experimental. Expect unannounced breaking changes (without version bumps) for
            all parameters and returned structs.
              - `CAR`
              - `CAR_PARKING` Experimental. Expect unannounced breaking changes (without version
            bumps) for all parameters and returned structs.
              - `CAR_DROPOFF` Experimental. Expect unannounced breaking changes (without version
            bumps) for all perameters and returned structs.
              - `ODM` on-demand taxis from the Prima+ÖV Project
              - `RIDE_SHARING` ride sharing from the Prima+ÖV Project
              - `FLEX` flexible transports

            # Transit modes

              - `TRANSIT`: translates to
            `TRAM,FERRY,AIRPLANE,BUS,COACH,RAIL,ODM,RIDE_SHARING,FUNICULAR,AERIAL_LIFT,OTHER`
              - `TRAM`: trams
              - `SUBWAY`: subway trains (Paris Metro, London Underground, but also NYC Subway,
            Hamburger Hochbahn, and other non-underground services)
              - `FERRY`: ferries
              - `AIRPLANE`: airline flights
              - `BUS`: short distance buses (does not include `COACH`)
              - `COACH`: long distance buses (does not include `BUS`)
              - `RAIL`: translates to
            `HIGHSPEED_RAIL,LONG_DISTANCE,NIGHT_RAIL,REGIONAL_RAIL,SUBURBAN,SUBWAY`
              - `HIGHSPEED_RAIL`: long distance high speed trains (e.g. TGV)
              - `LONG_DISTANCE`: long distance inter city trains
              - `NIGHT_RAIL`: long distance night trains
              - `REGIONAL_FAST_RAIL`: deprecated, `REGIONAL_RAIL` will be used
              - `REGIONAL_RAIL`: regional train
              - `SUBURBAN`: suburban trains (e.g. S-Bahn, RER, Elizabeth Line, ...)
              - `ODM`: demand responsive transport
              - `RIDE_SHARING`: ride sharing
              - `FUNICULAR`: Funicular. Any rail system designed for steep inclines.
              - `AERIAL_LIFT`: Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway).
            Cable transport where cabins, cars, gondolas or open chairs are suspended by means of one
            or more cables.
              - `AREAL_LIFT`: deprecated
              - `METRO`: deprecated
              - `CABLE_CAR`: deprecated
        max_pre_transit_time (int | Unset):  Default: 900.
        max_post_transit_time (int | Unset):  Default: 900.
        max_direct_time (int | Unset):  Default: 1800.
        with_distance (bool | Unset):  Default: False.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OneToManyIntermodalResponse]
    """

    kwargs = _get_kwargs(
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

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    one: str,
    many: list[str],
    time: datetime.datetime | Unset = UNSET,
    max_travel_time: int | Unset = UNSET,
    max_matching_distance: float | Unset = 25.0,
    arrive_by: bool | Unset = False,
    max_transfers: int | Unset = UNSET,
    min_transfer_time: int | Unset = 0,
    additional_transfer_time: int | Unset = 0,
    transfer_time_factor: float | Unset = 1.0,
    use_routed_transfers: bool | Unset = False,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    pedestrian_speed: float | Unset = UNSET,
    cycling_speed: float | Unset = UNSET,
    elevation_costs: ElevationCosts | Unset = UNSET,
    transit_modes: list[Mode] | Unset = UNSET,
    pre_transit_modes: list[Mode] | Unset = UNSET,
    post_transit_modes: list[Mode] | Unset = UNSET,
    direct_mode: Mode | Unset = UNSET,
    max_pre_transit_time: int | Unset = 900,
    max_post_transit_time: int | Unset = 900,
    max_direct_time: int | Unset = 1800,
    with_distance: bool | Unset = False,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
) -> Error | OneToManyIntermodalResponse | None:
    r"""One to many routing
    Computes the minimal duration from one place to many or vice versa.
    The order in the response array corresponds to the order of coordinates of the \`many\` parameter in
    the query.

    Args:
        one (str):
        many (list[str]):
        time (datetime.datetime | Unset):
        max_travel_time (int | Unset):
        max_matching_distance (float | Unset):  Default: 25.0.
        arrive_by (bool | Unset):  Default: False.
        max_transfers (int | Unset):
        min_transfer_time (int | Unset):  Default: 0.
        additional_transfer_time (int | Unset):  Default: 0.
        transfer_time_factor (float | Unset):  Default: 1.0.
        use_routed_transfers (bool | Unset):  Default: False.
        pedestrian_profile (PedestrianProfile | Unset): Different accessibility profiles for
            pedestrians.
        pedestrian_speed (float | Unset): Average speed for pedestrian routing in meters per
            second
        cycling_speed (float | Unset): Average speed for bike routing in meters per second
        elevation_costs (ElevationCosts | Unset): Different elevation cost profiles for street
            routing.
            Using a elevation cost profile will prefer routes with a smaller incline and smaller
            difference in elevation, even if the routed way is longer.

            - `NONE`: Ignore elevation data for routing. This is the default behavior
            - `LOW`: Add a low penalty for inclines. This will favor longer paths, if the elevation
            increase and incline are smaller.
            - `HIGH`: Add a high penalty for inclines. This will favor even longer paths, if the
            elevation increase and incline are smaller.
        transit_modes (list[Mode] | Unset):
        pre_transit_modes (list[Mode] | Unset):
        post_transit_modes (list[Mode] | Unset):
        direct_mode (Mode | Unset): # Street modes

              - `WALK`
              - `BIKE`
              - `RENTAL` Experimental. Expect unannounced breaking changes (without version bumps) for
            all parameters and returned structs.
              - `CAR`
              - `CAR_PARKING` Experimental. Expect unannounced breaking changes (without version
            bumps) for all parameters and returned structs.
              - `CAR_DROPOFF` Experimental. Expect unannounced breaking changes (without version
            bumps) for all perameters and returned structs.
              - `ODM` on-demand taxis from the Prima+ÖV Project
              - `RIDE_SHARING` ride sharing from the Prima+ÖV Project
              - `FLEX` flexible transports

            # Transit modes

              - `TRANSIT`: translates to
            `TRAM,FERRY,AIRPLANE,BUS,COACH,RAIL,ODM,RIDE_SHARING,FUNICULAR,AERIAL_LIFT,OTHER`
              - `TRAM`: trams
              - `SUBWAY`: subway trains (Paris Metro, London Underground, but also NYC Subway,
            Hamburger Hochbahn, and other non-underground services)
              - `FERRY`: ferries
              - `AIRPLANE`: airline flights
              - `BUS`: short distance buses (does not include `COACH`)
              - `COACH`: long distance buses (does not include `BUS`)
              - `RAIL`: translates to
            `HIGHSPEED_RAIL,LONG_DISTANCE,NIGHT_RAIL,REGIONAL_RAIL,SUBURBAN,SUBWAY`
              - `HIGHSPEED_RAIL`: long distance high speed trains (e.g. TGV)
              - `LONG_DISTANCE`: long distance inter city trains
              - `NIGHT_RAIL`: long distance night trains
              - `REGIONAL_FAST_RAIL`: deprecated, `REGIONAL_RAIL` will be used
              - `REGIONAL_RAIL`: regional train
              - `SUBURBAN`: suburban trains (e.g. S-Bahn, RER, Elizabeth Line, ...)
              - `ODM`: demand responsive transport
              - `RIDE_SHARING`: ride sharing
              - `FUNICULAR`: Funicular. Any rail system designed for steep inclines.
              - `AERIAL_LIFT`: Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway).
            Cable transport where cabins, cars, gondolas or open chairs are suspended by means of one
            or more cables.
              - `AREAL_LIFT`: deprecated
              - `METRO`: deprecated
              - `CABLE_CAR`: deprecated
        max_pre_transit_time (int | Unset):  Default: 900.
        max_post_transit_time (int | Unset):  Default: 900.
        max_direct_time (int | Unset):  Default: 1800.
        with_distance (bool | Unset):  Default: False.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OneToManyIntermodalResponse
    """

    return (
        await asyncio_detailed(
            client=client,
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
    ).parsed
