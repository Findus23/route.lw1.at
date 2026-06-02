from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.routes_response_200 import RoutesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    zoom: float,
    min_: str,
    max_: str,
    language: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["zoom"] = zoom

    params["min"] = min_

    params["max"] = max_

    json_language: list[str] | Unset = UNSET
    if not isinstance(language, Unset):
        json_language = language

    params["language"] = json_language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/experimental/map/routes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | RoutesResponse200 | None:
    if response.status_code == 200:
        response_200 = RoutesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

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
) -> Response[Error | RoutesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    zoom: float,
    min_: str,
    max_: str,
    language: list[str] | Unset = UNSET,
) -> Response[Error | RoutesResponse200]:
    """Given an area frame (box defined by the top-right and bottom-left corners),
    it returns all routes and their respective shapes that operate within this area.
    Routes are filtered by zoom level. On low zoom levels, only long distance trains will be shown
    while on high zoom levels, also metros, buses and trams will be returned.

    Args:
        zoom (float):
        min_ (str):
        max_ (str):
        language (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RoutesResponse200]
    """

    kwargs = _get_kwargs(
        zoom=zoom,
        min_=min_,
        max_=max_,
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    zoom: float,
    min_: str,
    max_: str,
    language: list[str] | Unset = UNSET,
) -> Error | RoutesResponse200 | None:
    """Given an area frame (box defined by the top-right and bottom-left corners),
    it returns all routes and their respective shapes that operate within this area.
    Routes are filtered by zoom level. On low zoom levels, only long distance trains will be shown
    while on high zoom levels, also metros, buses and trams will be returned.

    Args:
        zoom (float):
        min_ (str):
        max_ (str):
        language (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RoutesResponse200
    """

    return sync_detailed(
        client=client,
        zoom=zoom,
        min_=min_,
        max_=max_,
        language=language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    zoom: float,
    min_: str,
    max_: str,
    language: list[str] | Unset = UNSET,
) -> Response[Error | RoutesResponse200]:
    """Given an area frame (box defined by the top-right and bottom-left corners),
    it returns all routes and their respective shapes that operate within this area.
    Routes are filtered by zoom level. On low zoom levels, only long distance trains will be shown
    while on high zoom levels, also metros, buses and trams will be returned.

    Args:
        zoom (float):
        min_ (str):
        max_ (str):
        language (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RoutesResponse200]
    """

    kwargs = _get_kwargs(
        zoom=zoom,
        min_=min_,
        max_=max_,
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    zoom: float,
    min_: str,
    max_: str,
    language: list[str] | Unset = UNSET,
) -> Error | RoutesResponse200 | None:
    """Given an area frame (box defined by the top-right and bottom-left corners),
    it returns all routes and their respective shapes that operate within this area.
    Routes are filtered by zoom level. On low zoom levels, only long distance trains will be shown
    while on high zoom levels, also metros, buses and trams will be returned.

    Args:
        zoom (float):
        min_ (str):
        max_ (str):
        language (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RoutesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            zoom=zoom,
            min_=min_,
            max_=max_,
            language=language,
        )
    ).parsed
