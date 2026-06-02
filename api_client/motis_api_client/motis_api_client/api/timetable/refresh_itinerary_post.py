from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.itinerary import Itinerary
from ...models.refresh_itinerary_post_body import RefreshItineraryPostBody
from ...types import Response


def _get_kwargs(
    *,
    body: RefreshItineraryPostBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v6/refresh-itinerary",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Itinerary | None:
    if response.status_code == 200:
        response_200 = Itinerary.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

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
    body: RefreshItineraryPostBody,
) -> Response[Error | Itinerary]:
    """Reconstruct an itinerary from a protobuf-JSON itinerary identifier.

     Experimental (API might change without prior notice and without API version bump).
    Only supports walking at start/end or station-to-station itineraries.

    All `RefreshItineraryPostBody` fields mirror the parameters of the
    `plan` endpoint - see the `plan` endpoint for their descriptions.

    Args:
        body (RefreshItineraryPostBody): Body for the `refreshItineraryPost` endpoint. All fields
            mirror the
            parameters of the `plan` endpoint - see the `plan` endpoint for their
            descriptions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Itinerary]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RefreshItineraryPostBody,
) -> Error | Itinerary | None:
    """Reconstruct an itinerary from a protobuf-JSON itinerary identifier.

     Experimental (API might change without prior notice and without API version bump).
    Only supports walking at start/end or station-to-station itineraries.

    All `RefreshItineraryPostBody` fields mirror the parameters of the
    `plan` endpoint - see the `plan` endpoint for their descriptions.

    Args:
        body (RefreshItineraryPostBody): Body for the `refreshItineraryPost` endpoint. All fields
            mirror the
            parameters of the `plan` endpoint - see the `plan` endpoint for their
            descriptions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Itinerary
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RefreshItineraryPostBody,
) -> Response[Error | Itinerary]:
    """Reconstruct an itinerary from a protobuf-JSON itinerary identifier.

     Experimental (API might change without prior notice and without API version bump).
    Only supports walking at start/end or station-to-station itineraries.

    All `RefreshItineraryPostBody` fields mirror the parameters of the
    `plan` endpoint - see the `plan` endpoint for their descriptions.

    Args:
        body (RefreshItineraryPostBody): Body for the `refreshItineraryPost` endpoint. All fields
            mirror the
            parameters of the `plan` endpoint - see the `plan` endpoint for their
            descriptions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Itinerary]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RefreshItineraryPostBody,
) -> Error | Itinerary | None:
    """Reconstruct an itinerary from a protobuf-JSON itinerary identifier.

     Experimental (API might change without prior notice and without API version bump).
    Only supports walking at start/end or station-to-station itineraries.

    All `RefreshItineraryPostBody` fields mirror the parameters of the
    `plan` endpoint - see the `plan` endpoint for their descriptions.

    Args:
        body (RefreshItineraryPostBody): Body for the `refreshItineraryPost` endpoint. All fields
            mirror the
            parameters of the `plan` endpoint - see the `plan` endpoint for their
            descriptions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Itinerary
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
