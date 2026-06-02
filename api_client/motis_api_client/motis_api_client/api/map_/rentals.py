from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.rentals_response_200 import RentalsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    min_: str | Unset = UNSET,
    max_: str | Unset = UNSET,
    point: str | Unset = UNSET,
    radius: int | Unset = UNSET,
    provider_groups: list[str] | Unset = UNSET,
    providers: list[str] | Unset = UNSET,
    with_providers: bool | Unset = True,
    with_stations: bool | Unset = True,
    with_vehicles: bool | Unset = True,
    with_zones: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["min"] = min_

    params["max"] = max_

    params["point"] = point

    params["radius"] = radius

    json_provider_groups: list[str] | Unset = UNSET
    if not isinstance(provider_groups, Unset):
        json_provider_groups = provider_groups

    params["providerGroups"] = json_provider_groups

    json_providers: list[str] | Unset = UNSET
    if not isinstance(providers, Unset):
        json_providers = providers

    params["providers"] = json_providers

    params["withProviders"] = with_providers

    params["withStations"] = with_stations

    params["withVehicles"] = with_vehicles

    params["withZones"] = with_zones

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/rentals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | RentalsResponse200 | None:
    if response.status_code == 200:
        response_200 = RentalsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | RentalsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    min_: str | Unset = UNSET,
    max_: str | Unset = UNSET,
    point: str | Unset = UNSET,
    radius: int | Unset = UNSET,
    provider_groups: list[str] | Unset = UNSET,
    providers: list[str] | Unset = UNSET,
    with_providers: bool | Unset = True,
    with_stations: bool | Unset = True,
    with_vehicles: bool | Unset = True,
    with_zones: bool | Unset = True,
) -> Response[Error | RentalsResponse200]:
    """Get a list of rental providers or all rental stations and vehicles for
    a map section or provider

     Various options to filter the providers, stations and vehicles are
    available. If none of these filters are provided, a list of all
    available rental providers is returned without any station, vehicle or
    zone data.

    At least one of the following filters must be provided to retrieve
    station, vehicle and zone data:

    - A bounding box defined by the `min` and `max` parameters
    - A circle defined by the `point` and `radius` parameters
    - A list of provider groups via the `providerGroups` parameter
    - A list of providers via the `providers` parameter

    Only data that matches all the provided filters is returned.

    Provide the `withProviders=false` parameter to retrieve only provider
    groups if detailed feed information is not required.

    Args:
        min_ (str | Unset):
        max_ (str | Unset):
        point (str | Unset):
        radius (int | Unset):
        provider_groups (list[str] | Unset):
        providers (list[str] | Unset):
        with_providers (bool | Unset):  Default: True.
        with_stations (bool | Unset):  Default: True.
        with_vehicles (bool | Unset):  Default: True.
        with_zones (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RentalsResponse200]
    """

    kwargs = _get_kwargs(
        min_=min_,
        max_=max_,
        point=point,
        radius=radius,
        provider_groups=provider_groups,
        providers=providers,
        with_providers=with_providers,
        with_stations=with_stations,
        with_vehicles=with_vehicles,
        with_zones=with_zones,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    min_: str | Unset = UNSET,
    max_: str | Unset = UNSET,
    point: str | Unset = UNSET,
    radius: int | Unset = UNSET,
    provider_groups: list[str] | Unset = UNSET,
    providers: list[str] | Unset = UNSET,
    with_providers: bool | Unset = True,
    with_stations: bool | Unset = True,
    with_vehicles: bool | Unset = True,
    with_zones: bool | Unset = True,
) -> Error | RentalsResponse200 | None:
    """Get a list of rental providers or all rental stations and vehicles for
    a map section or provider

     Various options to filter the providers, stations and vehicles are
    available. If none of these filters are provided, a list of all
    available rental providers is returned without any station, vehicle or
    zone data.

    At least one of the following filters must be provided to retrieve
    station, vehicle and zone data:

    - A bounding box defined by the `min` and `max` parameters
    - A circle defined by the `point` and `radius` parameters
    - A list of provider groups via the `providerGroups` parameter
    - A list of providers via the `providers` parameter

    Only data that matches all the provided filters is returned.

    Provide the `withProviders=false` parameter to retrieve only provider
    groups if detailed feed information is not required.

    Args:
        min_ (str | Unset):
        max_ (str | Unset):
        point (str | Unset):
        radius (int | Unset):
        provider_groups (list[str] | Unset):
        providers (list[str] | Unset):
        with_providers (bool | Unset):  Default: True.
        with_stations (bool | Unset):  Default: True.
        with_vehicles (bool | Unset):  Default: True.
        with_zones (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RentalsResponse200
    """

    return sync_detailed(
        client=client,
        min_=min_,
        max_=max_,
        point=point,
        radius=radius,
        provider_groups=provider_groups,
        providers=providers,
        with_providers=with_providers,
        with_stations=with_stations,
        with_vehicles=with_vehicles,
        with_zones=with_zones,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    min_: str | Unset = UNSET,
    max_: str | Unset = UNSET,
    point: str | Unset = UNSET,
    radius: int | Unset = UNSET,
    provider_groups: list[str] | Unset = UNSET,
    providers: list[str] | Unset = UNSET,
    with_providers: bool | Unset = True,
    with_stations: bool | Unset = True,
    with_vehicles: bool | Unset = True,
    with_zones: bool | Unset = True,
) -> Response[Error | RentalsResponse200]:
    """Get a list of rental providers or all rental stations and vehicles for
    a map section or provider

     Various options to filter the providers, stations and vehicles are
    available. If none of these filters are provided, a list of all
    available rental providers is returned without any station, vehicle or
    zone data.

    At least one of the following filters must be provided to retrieve
    station, vehicle and zone data:

    - A bounding box defined by the `min` and `max` parameters
    - A circle defined by the `point` and `radius` parameters
    - A list of provider groups via the `providerGroups` parameter
    - A list of providers via the `providers` parameter

    Only data that matches all the provided filters is returned.

    Provide the `withProviders=false` parameter to retrieve only provider
    groups if detailed feed information is not required.

    Args:
        min_ (str | Unset):
        max_ (str | Unset):
        point (str | Unset):
        radius (int | Unset):
        provider_groups (list[str] | Unset):
        providers (list[str] | Unset):
        with_providers (bool | Unset):  Default: True.
        with_stations (bool | Unset):  Default: True.
        with_vehicles (bool | Unset):  Default: True.
        with_zones (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RentalsResponse200]
    """

    kwargs = _get_kwargs(
        min_=min_,
        max_=max_,
        point=point,
        radius=radius,
        provider_groups=provider_groups,
        providers=providers,
        with_providers=with_providers,
        with_stations=with_stations,
        with_vehicles=with_vehicles,
        with_zones=with_zones,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    min_: str | Unset = UNSET,
    max_: str | Unset = UNSET,
    point: str | Unset = UNSET,
    radius: int | Unset = UNSET,
    provider_groups: list[str] | Unset = UNSET,
    providers: list[str] | Unset = UNSET,
    with_providers: bool | Unset = True,
    with_stations: bool | Unset = True,
    with_vehicles: bool | Unset = True,
    with_zones: bool | Unset = True,
) -> Error | RentalsResponse200 | None:
    """Get a list of rental providers or all rental stations and vehicles for
    a map section or provider

     Various options to filter the providers, stations and vehicles are
    available. If none of these filters are provided, a list of all
    available rental providers is returned without any station, vehicle or
    zone data.

    At least one of the following filters must be provided to retrieve
    station, vehicle and zone data:

    - A bounding box defined by the `min` and `max` parameters
    - A circle defined by the `point` and `radius` parameters
    - A list of provider groups via the `providerGroups` parameter
    - A list of providers via the `providers` parameter

    Only data that matches all the provided filters is returned.

    Provide the `withProviders=false` parameter to retrieve only provider
    groups if detailed feed information is not required.

    Args:
        min_ (str | Unset):
        max_ (str | Unset):
        point (str | Unset):
        radius (int | Unset):
        provider_groups (list[str] | Unset):
        providers (list[str] | Unset):
        with_providers (bool | Unset):  Default: True.
        with_stations (bool | Unset):  Default: True.
        with_vehicles (bool | Unset):  Default: True.
        with_zones (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RentalsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            min_=min_,
            max_=max_,
            point=point,
            radius=radius,
            provider_groups=provider_groups,
            providers=providers,
            with_providers=with_providers,
            with_stations=with_stations,
            with_vehicles=with_vehicles,
            with_zones=with_zones,
        )
    ).parsed
