from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.itinerary import Itinerary
from ...models.mode import Mode
from ...models.pedestrian_profile import PedestrianProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    itinerary_id: str,
    require_display_name_match: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    detailed_transfers: bool | Unset = UNSET,
    detailed_legs: bool | Unset = True,
    with_fares: bool | Unset = False,
    with_scheduled_skipped_stops: bool | Unset = False,
    num_leg_alternatives: int | Unset = 0,
    transit_modes: list[Mode] | Unset = UNSET,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    use_routed_transfers: bool | Unset = False,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
    language: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["itineraryId"] = itinerary_id

    params["requireDisplayNameMatch"] = require_display_name_match

    params["joinInterlinedLegs"] = join_interlined_legs

    params["detailedTransfers"] = detailed_transfers

    params["detailedLegs"] = detailed_legs

    params["withFares"] = with_fares

    params["withScheduledSkippedStops"] = with_scheduled_skipped_stops

    params["numLegAlternatives"] = num_leg_alternatives

    json_transit_modes: list[str] | Unset = UNSET
    if not isinstance(transit_modes, Unset):
        json_transit_modes = []
        for transit_modes_item_data in transit_modes:
            transit_modes_item = transit_modes_item_data.value
            json_transit_modes.append(transit_modes_item)

    params["transitModes"] = json_transit_modes

    json_pedestrian_profile: str | Unset = UNSET
    if not isinstance(pedestrian_profile, Unset):
        json_pedestrian_profile = pedestrian_profile.value

    params["pedestrianProfile"] = json_pedestrian_profile

    params["useRoutedTransfers"] = use_routed_transfers

    params["requireBikeTransport"] = require_bike_transport

    params["requireCarTransport"] = require_car_transport

    json_language: list[str] | Unset = UNSET
    if not isinstance(language, Unset):
        json_language = language

    params["language"] = json_language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v6/refresh-itinerary",
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
    itinerary_id: str,
    require_display_name_match: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    detailed_transfers: bool | Unset = UNSET,
    detailed_legs: bool | Unset = True,
    with_fares: bool | Unset = False,
    with_scheduled_skipped_stops: bool | Unset = False,
    num_leg_alternatives: int | Unset = 0,
    transit_modes: list[Mode] | Unset = UNSET,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    use_routed_transfers: bool | Unset = False,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
    language: list[str] | Unset = UNSET,
) -> Response[Error | Itinerary]:
    """Reconstruct an itinerary from an itinerary ID.

     Experimental (API might change without prior notice and without API version bump).
    Only supports walking at start/end or station-to-station itineraries.

    All parameters mirror those of the `plan` endpoint - see the `plan`
    endpoint for their descriptions.

    Args:
        itinerary_id (str):
        require_display_name_match (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        detailed_transfers (bool | Unset):
        detailed_legs (bool | Unset):  Default: True.
        with_fares (bool | Unset):  Default: False.
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        num_leg_alternatives (int | Unset):  Default: 0.
        transit_modes (list[Mode] | Unset):
        pedestrian_profile (PedestrianProfile | Unset): Different accessibility profiles for
            pedestrians.
        use_routed_transfers (bool | Unset):  Default: False.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.
        language (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Itinerary]
    """

    kwargs = _get_kwargs(
        itinerary_id=itinerary_id,
        require_display_name_match=require_display_name_match,
        join_interlined_legs=join_interlined_legs,
        detailed_transfers=detailed_transfers,
        detailed_legs=detailed_legs,
        with_fares=with_fares,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        num_leg_alternatives=num_leg_alternatives,
        transit_modes=transit_modes,
        pedestrian_profile=pedestrian_profile,
        use_routed_transfers=use_routed_transfers,
        require_bike_transport=require_bike_transport,
        require_car_transport=require_car_transport,
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    itinerary_id: str,
    require_display_name_match: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    detailed_transfers: bool | Unset = UNSET,
    detailed_legs: bool | Unset = True,
    with_fares: bool | Unset = False,
    with_scheduled_skipped_stops: bool | Unset = False,
    num_leg_alternatives: int | Unset = 0,
    transit_modes: list[Mode] | Unset = UNSET,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    use_routed_transfers: bool | Unset = False,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
    language: list[str] | Unset = UNSET,
) -> Error | Itinerary | None:
    """Reconstruct an itinerary from an itinerary ID.

     Experimental (API might change without prior notice and without API version bump).
    Only supports walking at start/end or station-to-station itineraries.

    All parameters mirror those of the `plan` endpoint - see the `plan`
    endpoint for their descriptions.

    Args:
        itinerary_id (str):
        require_display_name_match (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        detailed_transfers (bool | Unset):
        detailed_legs (bool | Unset):  Default: True.
        with_fares (bool | Unset):  Default: False.
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        num_leg_alternatives (int | Unset):  Default: 0.
        transit_modes (list[Mode] | Unset):
        pedestrian_profile (PedestrianProfile | Unset): Different accessibility profiles for
            pedestrians.
        use_routed_transfers (bool | Unset):  Default: False.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.
        language (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Itinerary
    """

    return sync_detailed(
        client=client,
        itinerary_id=itinerary_id,
        require_display_name_match=require_display_name_match,
        join_interlined_legs=join_interlined_legs,
        detailed_transfers=detailed_transfers,
        detailed_legs=detailed_legs,
        with_fares=with_fares,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        num_leg_alternatives=num_leg_alternatives,
        transit_modes=transit_modes,
        pedestrian_profile=pedestrian_profile,
        use_routed_transfers=use_routed_transfers,
        require_bike_transport=require_bike_transport,
        require_car_transport=require_car_transport,
        language=language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    itinerary_id: str,
    require_display_name_match: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    detailed_transfers: bool | Unset = UNSET,
    detailed_legs: bool | Unset = True,
    with_fares: bool | Unset = False,
    with_scheduled_skipped_stops: bool | Unset = False,
    num_leg_alternatives: int | Unset = 0,
    transit_modes: list[Mode] | Unset = UNSET,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    use_routed_transfers: bool | Unset = False,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
    language: list[str] | Unset = UNSET,
) -> Response[Error | Itinerary]:
    """Reconstruct an itinerary from an itinerary ID.

     Experimental (API might change without prior notice and without API version bump).
    Only supports walking at start/end or station-to-station itineraries.

    All parameters mirror those of the `plan` endpoint - see the `plan`
    endpoint for their descriptions.

    Args:
        itinerary_id (str):
        require_display_name_match (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        detailed_transfers (bool | Unset):
        detailed_legs (bool | Unset):  Default: True.
        with_fares (bool | Unset):  Default: False.
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        num_leg_alternatives (int | Unset):  Default: 0.
        transit_modes (list[Mode] | Unset):
        pedestrian_profile (PedestrianProfile | Unset): Different accessibility profiles for
            pedestrians.
        use_routed_transfers (bool | Unset):  Default: False.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.
        language (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Itinerary]
    """

    kwargs = _get_kwargs(
        itinerary_id=itinerary_id,
        require_display_name_match=require_display_name_match,
        join_interlined_legs=join_interlined_legs,
        detailed_transfers=detailed_transfers,
        detailed_legs=detailed_legs,
        with_fares=with_fares,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        num_leg_alternatives=num_leg_alternatives,
        transit_modes=transit_modes,
        pedestrian_profile=pedestrian_profile,
        use_routed_transfers=use_routed_transfers,
        require_bike_transport=require_bike_transport,
        require_car_transport=require_car_transport,
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    itinerary_id: str,
    require_display_name_match: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    detailed_transfers: bool | Unset = UNSET,
    detailed_legs: bool | Unset = True,
    with_fares: bool | Unset = False,
    with_scheduled_skipped_stops: bool | Unset = False,
    num_leg_alternatives: int | Unset = 0,
    transit_modes: list[Mode] | Unset = UNSET,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    use_routed_transfers: bool | Unset = False,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
    language: list[str] | Unset = UNSET,
) -> Error | Itinerary | None:
    """Reconstruct an itinerary from an itinerary ID.

     Experimental (API might change without prior notice and without API version bump).
    Only supports walking at start/end or station-to-station itineraries.

    All parameters mirror those of the `plan` endpoint - see the `plan`
    endpoint for their descriptions.

    Args:
        itinerary_id (str):
        require_display_name_match (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        detailed_transfers (bool | Unset):
        detailed_legs (bool | Unset):  Default: True.
        with_fares (bool | Unset):  Default: False.
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        num_leg_alternatives (int | Unset):  Default: 0.
        transit_modes (list[Mode] | Unset):
        pedestrian_profile (PedestrianProfile | Unset): Different accessibility profiles for
            pedestrians.
        use_routed_transfers (bool | Unset):  Default: False.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.
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
            itinerary_id=itinerary_id,
            require_display_name_match=require_display_name_match,
            join_interlined_legs=join_interlined_legs,
            detailed_transfers=detailed_transfers,
            detailed_legs=detailed_legs,
            with_fares=with_fares,
            with_scheduled_skipped_stops=with_scheduled_skipped_stops,
            num_leg_alternatives=num_leg_alternatives,
            transit_modes=transit_modes,
            pedestrian_profile=pedestrian_profile,
            use_routed_transfers=use_routed_transfers,
            require_bike_transport=require_bike_transport,
            require_car_transport=require_car_transport,
            language=language,
        )
    ).parsed
