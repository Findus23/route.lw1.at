from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.itinerary import Itinerary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    trip_id: str,
    with_scheduled_skipped_stops: bool | Unset = False,
    detailed_legs: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    language: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["tripId"] = trip_id

    params["withScheduledSkippedStops"] = with_scheduled_skipped_stops

    params["detailedLegs"] = detailed_legs

    params["joinInterlinedLegs"] = join_interlined_legs

    json_language: list[str] | Unset = UNSET
    if not isinstance(language, Unset):
        json_language = language

    params["language"] = json_language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v6/trip",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Itinerary | None:
    if response.status_code == 200:
        response_200 = Itinerary.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Itinerary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    trip_id: str,
    with_scheduled_skipped_stops: bool | Unset = False,
    detailed_legs: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    language: list[str] | Unset = UNSET,
) -> Response[Error | Itinerary]:
    """Get a trip as itinerary

    Args:
        trip_id (str):
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        detailed_legs (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        language (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Itinerary]
    """

    kwargs = _get_kwargs(
        trip_id=trip_id,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        detailed_legs=detailed_legs,
        join_interlined_legs=join_interlined_legs,
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    trip_id: str,
    with_scheduled_skipped_stops: bool | Unset = False,
    detailed_legs: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    language: list[str] | Unset = UNSET,
) -> Error | Itinerary | None:
    """Get a trip as itinerary

    Args:
        trip_id (str):
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        detailed_legs (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        language (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Itinerary
    """

    return sync_detailed(
        client=client,
        trip_id=trip_id,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        detailed_legs=detailed_legs,
        join_interlined_legs=join_interlined_legs,
        language=language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    trip_id: str,
    with_scheduled_skipped_stops: bool | Unset = False,
    detailed_legs: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    language: list[str] | Unset = UNSET,
) -> Response[Error | Itinerary]:
    """Get a trip as itinerary

    Args:
        trip_id (str):
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        detailed_legs (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        language (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Itinerary]
    """

    kwargs = _get_kwargs(
        trip_id=trip_id,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        detailed_legs=detailed_legs,
        join_interlined_legs=join_interlined_legs,
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    trip_id: str,
    with_scheduled_skipped_stops: bool | Unset = False,
    detailed_legs: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    language: list[str] | Unset = UNSET,
) -> Error | Itinerary | None:
    """Get a trip as itinerary

    Args:
        trip_id (str):
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        detailed_legs (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        language (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Itinerary
    """

    return (
        await asyncio_detailed(
            client=client,
            trip_id=trip_id,
            with_scheduled_skipped_stops=with_scheduled_skipped_stops,
            detailed_legs=detailed_legs,
            join_interlined_legs=join_interlined_legs,
            language=language,
        )
    ).parsed
