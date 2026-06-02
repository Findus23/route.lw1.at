from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.duration import Duration
from ...models.elevation_costs import ElevationCosts
from ...models.error import Error
from ...models.mode import Mode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    one: str,
    many: list[str],
    mode: Mode,
    max_: float,
    max_matching_distance: float,
    elevation_costs: ElevationCosts | Unset = UNSET,
    arrive_by: bool,
    with_distance: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["one"] = one

    json_many = many

    params["many"] = json_many

    json_mode = mode.value
    params["mode"] = json_mode

    params["max"] = max_

    params["maxMatchingDistance"] = max_matching_distance

    json_elevation_costs: str | Unset = UNSET
    if not isinstance(elevation_costs, Unset):
        json_elevation_costs = elevation_costs.value

    params["elevationCosts"] = json_elevation_costs

    params["arriveBy"] = arrive_by

    params["withDistance"] = with_distance

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/one-to-many",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[Duration] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Duration.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Error | list[Duration]]:
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
    mode: Mode,
    max_: float,
    max_matching_distance: float,
    elevation_costs: ElevationCosts | Unset = UNSET,
    arrive_by: bool,
    with_distance: bool | Unset = False,
) -> Response[Error | list[Duration]]:
    r"""Street routing from one to many places or many to one.
    The order in the response array corresponds to the order of coordinates of the \`many\` parameter in
    the query.

    Args:
        one (str):
        many (list[str]):
        mode (Mode): # Street modes

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
        max_ (float):
        max_matching_distance (float):
        elevation_costs (ElevationCosts | Unset): Different elevation cost profiles for street
            routing.
            Using a elevation cost profile will prefer routes with a smaller incline and smaller
            difference in elevation, even if the routed way is longer.

            - `NONE`: Ignore elevation data for routing. This is the default behavior
            - `LOW`: Add a low penalty for inclines. This will favor longer paths, if the elevation
            increase and incline are smaller.
            - `HIGH`: Add a high penalty for inclines. This will favor even longer paths, if the
            elevation increase and incline are smaller.
        arrive_by (bool):
        with_distance (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[Duration]]
    """

    kwargs = _get_kwargs(
        one=one,
        many=many,
        mode=mode,
        max_=max_,
        max_matching_distance=max_matching_distance,
        elevation_costs=elevation_costs,
        arrive_by=arrive_by,
        with_distance=with_distance,
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
    mode: Mode,
    max_: float,
    max_matching_distance: float,
    elevation_costs: ElevationCosts | Unset = UNSET,
    arrive_by: bool,
    with_distance: bool | Unset = False,
) -> Error | list[Duration] | None:
    r"""Street routing from one to many places or many to one.
    The order in the response array corresponds to the order of coordinates of the \`many\` parameter in
    the query.

    Args:
        one (str):
        many (list[str]):
        mode (Mode): # Street modes

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
        max_ (float):
        max_matching_distance (float):
        elevation_costs (ElevationCosts | Unset): Different elevation cost profiles for street
            routing.
            Using a elevation cost profile will prefer routes with a smaller incline and smaller
            difference in elevation, even if the routed way is longer.

            - `NONE`: Ignore elevation data for routing. This is the default behavior
            - `LOW`: Add a low penalty for inclines. This will favor longer paths, if the elevation
            increase and incline are smaller.
            - `HIGH`: Add a high penalty for inclines. This will favor even longer paths, if the
            elevation increase and incline are smaller.
        arrive_by (bool):
        with_distance (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[Duration]
    """

    return sync_detailed(
        client=client,
        one=one,
        many=many,
        mode=mode,
        max_=max_,
        max_matching_distance=max_matching_distance,
        elevation_costs=elevation_costs,
        arrive_by=arrive_by,
        with_distance=with_distance,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    one: str,
    many: list[str],
    mode: Mode,
    max_: float,
    max_matching_distance: float,
    elevation_costs: ElevationCosts | Unset = UNSET,
    arrive_by: bool,
    with_distance: bool | Unset = False,
) -> Response[Error | list[Duration]]:
    r"""Street routing from one to many places or many to one.
    The order in the response array corresponds to the order of coordinates of the \`many\` parameter in
    the query.

    Args:
        one (str):
        many (list[str]):
        mode (Mode): # Street modes

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
        max_ (float):
        max_matching_distance (float):
        elevation_costs (ElevationCosts | Unset): Different elevation cost profiles for street
            routing.
            Using a elevation cost profile will prefer routes with a smaller incline and smaller
            difference in elevation, even if the routed way is longer.

            - `NONE`: Ignore elevation data for routing. This is the default behavior
            - `LOW`: Add a low penalty for inclines. This will favor longer paths, if the elevation
            increase and incline are smaller.
            - `HIGH`: Add a high penalty for inclines. This will favor even longer paths, if the
            elevation increase and incline are smaller.
        arrive_by (bool):
        with_distance (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[Duration]]
    """

    kwargs = _get_kwargs(
        one=one,
        many=many,
        mode=mode,
        max_=max_,
        max_matching_distance=max_matching_distance,
        elevation_costs=elevation_costs,
        arrive_by=arrive_by,
        with_distance=with_distance,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    one: str,
    many: list[str],
    mode: Mode,
    max_: float,
    max_matching_distance: float,
    elevation_costs: ElevationCosts | Unset = UNSET,
    arrive_by: bool,
    with_distance: bool | Unset = False,
) -> Error | list[Duration] | None:
    r"""Street routing from one to many places or many to one.
    The order in the response array corresponds to the order of coordinates of the \`many\` parameter in
    the query.

    Args:
        one (str):
        many (list[str]):
        mode (Mode): # Street modes

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
        max_ (float):
        max_matching_distance (float):
        elevation_costs (ElevationCosts | Unset): Different elevation cost profiles for street
            routing.
            Using a elevation cost profile will prefer routes with a smaller incline and smaller
            difference in elevation, even if the routed way is longer.

            - `NONE`: Ignore elevation data for routing. This is the default behavior
            - `LOW`: Add a low penalty for inclines. This will favor longer paths, if the elevation
            increase and incline are smaller.
            - `HIGH`: Add a high penalty for inclines. This will favor even longer paths, if the
            elevation increase and incline are smaller.
        arrive_by (bool):
        with_distance (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[Duration]
    """

    return (
        await asyncio_detailed(
            client=client,
            one=one,
            many=many,
            mode=mode,
            max_=max_,
            max_matching_distance=max_matching_distance,
            elevation_costs=elevation_costs,
            arrive_by=arrive_by,
            with_distance=with_distance,
        )
    ).parsed
