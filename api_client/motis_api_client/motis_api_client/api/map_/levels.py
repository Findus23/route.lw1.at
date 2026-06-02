from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response


def _get_kwargs(
    *,
    min_: str,
    max_: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["min"] = min_

    params["max"] = max_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/map/levels",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[float] | None:
    if response.status_code == 200:
        response_200 = cast(list[float], response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | list[float]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    min_: str,
    max_: str,
) -> Response[Error | list[float]]:
    """Get all available levels for a map section

    Args:
        min_ (str):
        max_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[float]]
    """

    kwargs = _get_kwargs(
        min_=min_,
        max_=max_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    min_: str,
    max_: str,
) -> Error | list[float] | None:
    """Get all available levels for a map section

    Args:
        min_ (str):
        max_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[float]
    """

    return sync_detailed(
        client=client,
        min_=min_,
        max_=max_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    min_: str,
    max_: str,
) -> Response[Error | list[float]]:
    """Get all available levels for a map section

    Args:
        min_ (str):
        max_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[float]]
    """

    kwargs = _get_kwargs(
        min_=min_,
        max_=max_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    min_: str,
    max_: str,
) -> Error | list[float] | None:
    """Get all available levels for a map section

    Args:
        min_ (str):
        max_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[float]
    """

    return (
        await asyncio_detailed(
            client=client,
            min_=min_,
            max_=max_,
        )
    ).parsed
