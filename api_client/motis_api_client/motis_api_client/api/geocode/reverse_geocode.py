from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.location_type import LocationType
from ...models.match import Match
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    place: str,
    type_: list[LocationType] | Unset = UNSET,
    num_results: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["place"] = place

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)

    params["type"] = json_type_

    params["numResults"] = num_results

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/reverse-geocode",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[Match] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Match.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | list[Match]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    place: str,
    type_: list[LocationType] | Unset = UNSET,
    num_results: int | Unset = UNSET,
) -> Response[Error | list[Match]]:
    """Translate coordinates to the closest address(es)/places/stops.

    Args:
        place (str):
        type_ (list[LocationType] | Unset):
        num_results (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[Match]]
    """

    kwargs = _get_kwargs(
        place=place,
        type_=type_,
        num_results=num_results,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    place: str,
    type_: list[LocationType] | Unset = UNSET,
    num_results: int | Unset = UNSET,
) -> Error | list[Match] | None:
    """Translate coordinates to the closest address(es)/places/stops.

    Args:
        place (str):
        type_ (list[LocationType] | Unset):
        num_results (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[Match]
    """

    return sync_detailed(
        client=client,
        place=place,
        type_=type_,
        num_results=num_results,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    place: str,
    type_: list[LocationType] | Unset = UNSET,
    num_results: int | Unset = UNSET,
) -> Response[Error | list[Match]]:
    """Translate coordinates to the closest address(es)/places/stops.

    Args:
        place (str):
        type_ (list[LocationType] | Unset):
        num_results (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[Match]]
    """

    kwargs = _get_kwargs(
        place=place,
        type_=type_,
        num_results=num_results,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    place: str,
    type_: list[LocationType] | Unset = UNSET,
    num_results: int | Unset = UNSET,
) -> Error | list[Match] | None:
    """Translate coordinates to the closest address(es)/places/stops.

    Args:
        place (str):
        type_ (list[LocationType] | Unset):
        num_results (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[Match]
    """

    return (
        await asyncio_detailed(
            client=client,
            place=place,
            type_=type_,
            num_results=num_results,
        )
    ).parsed
