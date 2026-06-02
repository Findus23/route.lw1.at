import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.elevation_costs import ElevationCosts
from ...models.error import Error
from ...models.mode import Mode
from ...models.pedestrian_profile import PedestrianProfile
from ...models.plan_algorithm import PlanAlgorithm
from ...models.plan_response_200 import PlanResponse200
from ...models.rental_form_factor import RentalFormFactor
from ...models.rental_propulsion_type import RentalPropulsionType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_place: str,
    to_place: str,
    radius: float | Unset = UNSET,
    via: list[str] | Unset = UNSET,
    via_minimum_stay: list[int] | Unset = UNSET,
    time: datetime.datetime | Unset = UNSET,
    max_transfers: int | Unset = UNSET,
    max_travel_time: int | Unset = UNSET,
    min_transfer_time: int | Unset = 0,
    additional_transfer_time: int | Unset = 0,
    transfer_time_factor: float | Unset = 1.0,
    max_matching_distance: float | Unset = 25.0,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    pedestrian_speed: float | Unset = UNSET,
    cycling_speed: float | Unset = UNSET,
    elevation_costs: ElevationCosts | Unset = UNSET,
    use_routed_transfers: bool | Unset = False,
    detailed_transfers: bool | Unset = UNSET,
    detailed_legs: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    transit_modes: list[Mode] | Unset = UNSET,
    direct_modes: list[Mode] | Unset = UNSET,
    pre_transit_modes: list[Mode] | Unset = UNSET,
    post_transit_modes: list[Mode] | Unset = UNSET,
    direct_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    pre_transit_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    post_transit_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    direct_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    pre_transit_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    post_transit_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    direct_rental_providers: list[str] | Unset = UNSET,
    direct_rental_provider_groups: list[str] | Unset = UNSET,
    pre_transit_rental_providers: list[str] | Unset = UNSET,
    pre_transit_rental_provider_groups: list[str] | Unset = UNSET,
    post_transit_rental_providers: list[str] | Unset = UNSET,
    post_transit_rental_provider_groups: list[str] | Unset = UNSET,
    ignore_direct_rental_return_constraints: bool | Unset = False,
    ignore_pre_transit_rental_return_constraints: bool | Unset = False,
    ignore_post_transit_rental_return_constraints: bool | Unset = False,
    num_itineraries: int | Unset = 5,
    max_itineraries: int | Unset = UNSET,
    page_cursor: str | Unset = UNSET,
    timetable_view: bool | Unset = True,
    arrive_by: bool | Unset = False,
    search_window: int | Unset = 900,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
    max_pre_transit_time: int | Unset = 900,
    max_post_transit_time: int | Unset = 900,
    max_direct_time: int | Unset = 1800,
    fastest_direct_factor: float | Unset = 1.0,
    timeout: int | Unset = UNSET,
    passengers: int | Unset = UNSET,
    luggage: int | Unset = UNSET,
    slow_direct: bool | Unset = False,
    fastest_slow_direct_factor: float | Unset = 3.0,
    with_fares: bool | Unset = False,
    num_leg_alternatives: int | Unset = 0,
    with_scheduled_skipped_stops: bool | Unset = False,
    language: list[str] | Unset = UNSET,
    algorithm: PlanAlgorithm | Unset = PlanAlgorithm.PONG,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fromPlace"] = from_place

    params["toPlace"] = to_place

    params["radius"] = radius

    json_via: list[str] | Unset = UNSET
    if not isinstance(via, Unset):
        json_via = via

    params["via"] = json_via

    json_via_minimum_stay: list[int] | Unset = UNSET
    if not isinstance(via_minimum_stay, Unset):
        json_via_minimum_stay = via_minimum_stay

    params["viaMinimumStay"] = json_via_minimum_stay

    json_time: str | Unset = UNSET
    if not isinstance(time, Unset):
        json_time = time.isoformat()
    params["time"] = json_time

    params["maxTransfers"] = max_transfers

    params["maxTravelTime"] = max_travel_time

    params["minTransferTime"] = min_transfer_time

    params["additionalTransferTime"] = additional_transfer_time

    params["transferTimeFactor"] = transfer_time_factor

    params["maxMatchingDistance"] = max_matching_distance

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

    params["useRoutedTransfers"] = use_routed_transfers

    params["detailedTransfers"] = detailed_transfers

    params["detailedLegs"] = detailed_legs

    params["joinInterlinedLegs"] = join_interlined_legs

    json_transit_modes: list[str] | Unset = UNSET
    if not isinstance(transit_modes, Unset):
        json_transit_modes = []
        for transit_modes_item_data in transit_modes:
            transit_modes_item = transit_modes_item_data.value
            json_transit_modes.append(transit_modes_item)

    params["transitModes"] = json_transit_modes

    json_direct_modes: list[str] | Unset = UNSET
    if not isinstance(direct_modes, Unset):
        json_direct_modes = []
        for direct_modes_item_data in direct_modes:
            direct_modes_item = direct_modes_item_data.value
            json_direct_modes.append(direct_modes_item)

    params["directModes"] = json_direct_modes

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

    json_direct_rental_form_factors: list[str] | Unset = UNSET
    if not isinstance(direct_rental_form_factors, Unset):
        json_direct_rental_form_factors = []
        for direct_rental_form_factors_item_data in direct_rental_form_factors:
            direct_rental_form_factors_item = direct_rental_form_factors_item_data.value
            json_direct_rental_form_factors.append(direct_rental_form_factors_item)

    params["directRentalFormFactors"] = json_direct_rental_form_factors

    json_pre_transit_rental_form_factors: list[str] | Unset = UNSET
    if not isinstance(pre_transit_rental_form_factors, Unset):
        json_pre_transit_rental_form_factors = []
        for pre_transit_rental_form_factors_item_data in pre_transit_rental_form_factors:
            pre_transit_rental_form_factors_item = pre_transit_rental_form_factors_item_data.value
            json_pre_transit_rental_form_factors.append(pre_transit_rental_form_factors_item)

    params["preTransitRentalFormFactors"] = json_pre_transit_rental_form_factors

    json_post_transit_rental_form_factors: list[str] | Unset = UNSET
    if not isinstance(post_transit_rental_form_factors, Unset):
        json_post_transit_rental_form_factors = []
        for post_transit_rental_form_factors_item_data in post_transit_rental_form_factors:
            post_transit_rental_form_factors_item = post_transit_rental_form_factors_item_data.value
            json_post_transit_rental_form_factors.append(post_transit_rental_form_factors_item)

    params["postTransitRentalFormFactors"] = json_post_transit_rental_form_factors

    json_direct_rental_propulsion_types: list[str] | Unset = UNSET
    if not isinstance(direct_rental_propulsion_types, Unset):
        json_direct_rental_propulsion_types = []
        for direct_rental_propulsion_types_item_data in direct_rental_propulsion_types:
            direct_rental_propulsion_types_item = direct_rental_propulsion_types_item_data.value
            json_direct_rental_propulsion_types.append(direct_rental_propulsion_types_item)

    params["directRentalPropulsionTypes"] = json_direct_rental_propulsion_types

    json_pre_transit_rental_propulsion_types: list[str] | Unset = UNSET
    if not isinstance(pre_transit_rental_propulsion_types, Unset):
        json_pre_transit_rental_propulsion_types = []
        for pre_transit_rental_propulsion_types_item_data in pre_transit_rental_propulsion_types:
            pre_transit_rental_propulsion_types_item = pre_transit_rental_propulsion_types_item_data.value
            json_pre_transit_rental_propulsion_types.append(pre_transit_rental_propulsion_types_item)

    params["preTransitRentalPropulsionTypes"] = json_pre_transit_rental_propulsion_types

    json_post_transit_rental_propulsion_types: list[str] | Unset = UNSET
    if not isinstance(post_transit_rental_propulsion_types, Unset):
        json_post_transit_rental_propulsion_types = []
        for post_transit_rental_propulsion_types_item_data in post_transit_rental_propulsion_types:
            post_transit_rental_propulsion_types_item = post_transit_rental_propulsion_types_item_data.value
            json_post_transit_rental_propulsion_types.append(post_transit_rental_propulsion_types_item)

    params["postTransitRentalPropulsionTypes"] = json_post_transit_rental_propulsion_types

    json_direct_rental_providers: list[str] | Unset = UNSET
    if not isinstance(direct_rental_providers, Unset):
        json_direct_rental_providers = direct_rental_providers

    params["directRentalProviders"] = json_direct_rental_providers

    json_direct_rental_provider_groups: list[str] | Unset = UNSET
    if not isinstance(direct_rental_provider_groups, Unset):
        json_direct_rental_provider_groups = direct_rental_provider_groups

    params["directRentalProviderGroups"] = json_direct_rental_provider_groups

    json_pre_transit_rental_providers: list[str] | Unset = UNSET
    if not isinstance(pre_transit_rental_providers, Unset):
        json_pre_transit_rental_providers = pre_transit_rental_providers

    params["preTransitRentalProviders"] = json_pre_transit_rental_providers

    json_pre_transit_rental_provider_groups: list[str] | Unset = UNSET
    if not isinstance(pre_transit_rental_provider_groups, Unset):
        json_pre_transit_rental_provider_groups = pre_transit_rental_provider_groups

    params["preTransitRentalProviderGroups"] = json_pre_transit_rental_provider_groups

    json_post_transit_rental_providers: list[str] | Unset = UNSET
    if not isinstance(post_transit_rental_providers, Unset):
        json_post_transit_rental_providers = post_transit_rental_providers

    params["postTransitRentalProviders"] = json_post_transit_rental_providers

    json_post_transit_rental_provider_groups: list[str] | Unset = UNSET
    if not isinstance(post_transit_rental_provider_groups, Unset):
        json_post_transit_rental_provider_groups = post_transit_rental_provider_groups

    params["postTransitRentalProviderGroups"] = json_post_transit_rental_provider_groups

    params["ignoreDirectRentalReturnConstraints"] = ignore_direct_rental_return_constraints

    params["ignorePreTransitRentalReturnConstraints"] = ignore_pre_transit_rental_return_constraints

    params["ignorePostTransitRentalReturnConstraints"] = ignore_post_transit_rental_return_constraints

    params["numItineraries"] = num_itineraries

    params["maxItineraries"] = max_itineraries

    params["pageCursor"] = page_cursor

    params["timetableView"] = timetable_view

    params["arriveBy"] = arrive_by

    params["searchWindow"] = search_window

    params["requireBikeTransport"] = require_bike_transport

    params["requireCarTransport"] = require_car_transport

    params["maxPreTransitTime"] = max_pre_transit_time

    params["maxPostTransitTime"] = max_post_transit_time

    params["maxDirectTime"] = max_direct_time

    params["fastestDirectFactor"] = fastest_direct_factor

    params["timeout"] = timeout

    params["passengers"] = passengers

    params["luggage"] = luggage

    params["slowDirect"] = slow_direct

    params["fastestSlowDirectFactor"] = fastest_slow_direct_factor

    params["withFares"] = with_fares

    params["numLegAlternatives"] = num_leg_alternatives

    params["withScheduledSkippedStops"] = with_scheduled_skipped_stops

    json_language: list[str] | Unset = UNSET
    if not isinstance(language, Unset):
        json_language = language

    params["language"] = json_language

    json_algorithm: str | Unset = UNSET
    if not isinstance(algorithm, Unset):
        json_algorithm = algorithm.value

    params["algorithm"] = json_algorithm

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v6/plan",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PlanResponse200 | None:
    if response.status_code == 200:
        response_200 = PlanResponse200.from_dict(response.json())

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
) -> Response[Error | PlanResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_place: str,
    to_place: str,
    radius: float | Unset = UNSET,
    via: list[str] | Unset = UNSET,
    via_minimum_stay: list[int] | Unset = UNSET,
    time: datetime.datetime | Unset = UNSET,
    max_transfers: int | Unset = UNSET,
    max_travel_time: int | Unset = UNSET,
    min_transfer_time: int | Unset = 0,
    additional_transfer_time: int | Unset = 0,
    transfer_time_factor: float | Unset = 1.0,
    max_matching_distance: float | Unset = 25.0,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    pedestrian_speed: float | Unset = UNSET,
    cycling_speed: float | Unset = UNSET,
    elevation_costs: ElevationCosts | Unset = UNSET,
    use_routed_transfers: bool | Unset = False,
    detailed_transfers: bool | Unset = UNSET,
    detailed_legs: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    transit_modes: list[Mode] | Unset = UNSET,
    direct_modes: list[Mode] | Unset = UNSET,
    pre_transit_modes: list[Mode] | Unset = UNSET,
    post_transit_modes: list[Mode] | Unset = UNSET,
    direct_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    pre_transit_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    post_transit_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    direct_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    pre_transit_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    post_transit_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    direct_rental_providers: list[str] | Unset = UNSET,
    direct_rental_provider_groups: list[str] | Unset = UNSET,
    pre_transit_rental_providers: list[str] | Unset = UNSET,
    pre_transit_rental_provider_groups: list[str] | Unset = UNSET,
    post_transit_rental_providers: list[str] | Unset = UNSET,
    post_transit_rental_provider_groups: list[str] | Unset = UNSET,
    ignore_direct_rental_return_constraints: bool | Unset = False,
    ignore_pre_transit_rental_return_constraints: bool | Unset = False,
    ignore_post_transit_rental_return_constraints: bool | Unset = False,
    num_itineraries: int | Unset = 5,
    max_itineraries: int | Unset = UNSET,
    page_cursor: str | Unset = UNSET,
    timetable_view: bool | Unset = True,
    arrive_by: bool | Unset = False,
    search_window: int | Unset = 900,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
    max_pre_transit_time: int | Unset = 900,
    max_post_transit_time: int | Unset = 900,
    max_direct_time: int | Unset = 1800,
    fastest_direct_factor: float | Unset = 1.0,
    timeout: int | Unset = UNSET,
    passengers: int | Unset = UNSET,
    luggage: int | Unset = UNSET,
    slow_direct: bool | Unset = False,
    fastest_slow_direct_factor: float | Unset = 3.0,
    with_fares: bool | Unset = False,
    num_leg_alternatives: int | Unset = 0,
    with_scheduled_skipped_stops: bool | Unset = False,
    language: list[str] | Unset = UNSET,
    algorithm: PlanAlgorithm | Unset = PlanAlgorithm.PONG,
) -> Response[Error | PlanResponse200]:
    """Computes optimal connections from one place to another.

    Args:
        from_place (str):
        to_place (str):
        radius (float | Unset):
        via (list[str] | Unset):
        via_minimum_stay (list[int] | Unset):
        time (datetime.datetime | Unset):
        max_transfers (int | Unset):
        max_travel_time (int | Unset):
        min_transfer_time (int | Unset):  Default: 0.
        additional_transfer_time (int | Unset):  Default: 0.
        transfer_time_factor (float | Unset):  Default: 1.0.
        max_matching_distance (float | Unset):  Default: 25.0.
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
        use_routed_transfers (bool | Unset):  Default: False.
        detailed_transfers (bool | Unset):
        detailed_legs (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        transit_modes (list[Mode] | Unset):
        direct_modes (list[Mode] | Unset):
        pre_transit_modes (list[Mode] | Unset):
        post_transit_modes (list[Mode] | Unset):
        direct_rental_form_factors (list[RentalFormFactor] | Unset):
        pre_transit_rental_form_factors (list[RentalFormFactor] | Unset):
        post_transit_rental_form_factors (list[RentalFormFactor] | Unset):
        direct_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        pre_transit_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        post_transit_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        direct_rental_providers (list[str] | Unset):
        direct_rental_provider_groups (list[str] | Unset):
        pre_transit_rental_providers (list[str] | Unset):
        pre_transit_rental_provider_groups (list[str] | Unset):
        post_transit_rental_providers (list[str] | Unset):
        post_transit_rental_provider_groups (list[str] | Unset):
        ignore_direct_rental_return_constraints (bool | Unset):  Default: False.
        ignore_pre_transit_rental_return_constraints (bool | Unset):  Default: False.
        ignore_post_transit_rental_return_constraints (bool | Unset):  Default: False.
        num_itineraries (int | Unset):  Default: 5.
        max_itineraries (int | Unset):
        page_cursor (str | Unset):
        timetable_view (bool | Unset):  Default: True.
        arrive_by (bool | Unset):  Default: False.
        search_window (int | Unset):  Default: 900.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.
        max_pre_transit_time (int | Unset):  Default: 900.
        max_post_transit_time (int | Unset):  Default: 900.
        max_direct_time (int | Unset):  Default: 1800.
        fastest_direct_factor (float | Unset):  Default: 1.0.
        timeout (int | Unset):
        passengers (int | Unset):
        luggage (int | Unset):
        slow_direct (bool | Unset):  Default: False.
        fastest_slow_direct_factor (float | Unset):  Default: 3.0.
        with_fares (bool | Unset):  Default: False.
        num_leg_alternatives (int | Unset):  Default: 0.
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        language (list[str] | Unset):
        algorithm (PlanAlgorithm | Unset):  Default: PlanAlgorithm.PONG.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PlanResponse200]
    """

    kwargs = _get_kwargs(
        from_place=from_place,
        to_place=to_place,
        radius=radius,
        via=via,
        via_minimum_stay=via_minimum_stay,
        time=time,
        max_transfers=max_transfers,
        max_travel_time=max_travel_time,
        min_transfer_time=min_transfer_time,
        additional_transfer_time=additional_transfer_time,
        transfer_time_factor=transfer_time_factor,
        max_matching_distance=max_matching_distance,
        pedestrian_profile=pedestrian_profile,
        pedestrian_speed=pedestrian_speed,
        cycling_speed=cycling_speed,
        elevation_costs=elevation_costs,
        use_routed_transfers=use_routed_transfers,
        detailed_transfers=detailed_transfers,
        detailed_legs=detailed_legs,
        join_interlined_legs=join_interlined_legs,
        transit_modes=transit_modes,
        direct_modes=direct_modes,
        pre_transit_modes=pre_transit_modes,
        post_transit_modes=post_transit_modes,
        direct_rental_form_factors=direct_rental_form_factors,
        pre_transit_rental_form_factors=pre_transit_rental_form_factors,
        post_transit_rental_form_factors=post_transit_rental_form_factors,
        direct_rental_propulsion_types=direct_rental_propulsion_types,
        pre_transit_rental_propulsion_types=pre_transit_rental_propulsion_types,
        post_transit_rental_propulsion_types=post_transit_rental_propulsion_types,
        direct_rental_providers=direct_rental_providers,
        direct_rental_provider_groups=direct_rental_provider_groups,
        pre_transit_rental_providers=pre_transit_rental_providers,
        pre_transit_rental_provider_groups=pre_transit_rental_provider_groups,
        post_transit_rental_providers=post_transit_rental_providers,
        post_transit_rental_provider_groups=post_transit_rental_provider_groups,
        ignore_direct_rental_return_constraints=ignore_direct_rental_return_constraints,
        ignore_pre_transit_rental_return_constraints=ignore_pre_transit_rental_return_constraints,
        ignore_post_transit_rental_return_constraints=ignore_post_transit_rental_return_constraints,
        num_itineraries=num_itineraries,
        max_itineraries=max_itineraries,
        page_cursor=page_cursor,
        timetable_view=timetable_view,
        arrive_by=arrive_by,
        search_window=search_window,
        require_bike_transport=require_bike_transport,
        require_car_transport=require_car_transport,
        max_pre_transit_time=max_pre_transit_time,
        max_post_transit_time=max_post_transit_time,
        max_direct_time=max_direct_time,
        fastest_direct_factor=fastest_direct_factor,
        timeout=timeout,
        passengers=passengers,
        luggage=luggage,
        slow_direct=slow_direct,
        fastest_slow_direct_factor=fastest_slow_direct_factor,
        with_fares=with_fares,
        num_leg_alternatives=num_leg_alternatives,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        language=language,
        algorithm=algorithm,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    from_place: str,
    to_place: str,
    radius: float | Unset = UNSET,
    via: list[str] | Unset = UNSET,
    via_minimum_stay: list[int] | Unset = UNSET,
    time: datetime.datetime | Unset = UNSET,
    max_transfers: int | Unset = UNSET,
    max_travel_time: int | Unset = UNSET,
    min_transfer_time: int | Unset = 0,
    additional_transfer_time: int | Unset = 0,
    transfer_time_factor: float | Unset = 1.0,
    max_matching_distance: float | Unset = 25.0,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    pedestrian_speed: float | Unset = UNSET,
    cycling_speed: float | Unset = UNSET,
    elevation_costs: ElevationCosts | Unset = UNSET,
    use_routed_transfers: bool | Unset = False,
    detailed_transfers: bool | Unset = UNSET,
    detailed_legs: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    transit_modes: list[Mode] | Unset = UNSET,
    direct_modes: list[Mode] | Unset = UNSET,
    pre_transit_modes: list[Mode] | Unset = UNSET,
    post_transit_modes: list[Mode] | Unset = UNSET,
    direct_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    pre_transit_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    post_transit_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    direct_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    pre_transit_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    post_transit_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    direct_rental_providers: list[str] | Unset = UNSET,
    direct_rental_provider_groups: list[str] | Unset = UNSET,
    pre_transit_rental_providers: list[str] | Unset = UNSET,
    pre_transit_rental_provider_groups: list[str] | Unset = UNSET,
    post_transit_rental_providers: list[str] | Unset = UNSET,
    post_transit_rental_provider_groups: list[str] | Unset = UNSET,
    ignore_direct_rental_return_constraints: bool | Unset = False,
    ignore_pre_transit_rental_return_constraints: bool | Unset = False,
    ignore_post_transit_rental_return_constraints: bool | Unset = False,
    num_itineraries: int | Unset = 5,
    max_itineraries: int | Unset = UNSET,
    page_cursor: str | Unset = UNSET,
    timetable_view: bool | Unset = True,
    arrive_by: bool | Unset = False,
    search_window: int | Unset = 900,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
    max_pre_transit_time: int | Unset = 900,
    max_post_transit_time: int | Unset = 900,
    max_direct_time: int | Unset = 1800,
    fastest_direct_factor: float | Unset = 1.0,
    timeout: int | Unset = UNSET,
    passengers: int | Unset = UNSET,
    luggage: int | Unset = UNSET,
    slow_direct: bool | Unset = False,
    fastest_slow_direct_factor: float | Unset = 3.0,
    with_fares: bool | Unset = False,
    num_leg_alternatives: int | Unset = 0,
    with_scheduled_skipped_stops: bool | Unset = False,
    language: list[str] | Unset = UNSET,
    algorithm: PlanAlgorithm | Unset = PlanAlgorithm.PONG,
) -> Error | PlanResponse200 | None:
    """Computes optimal connections from one place to another.

    Args:
        from_place (str):
        to_place (str):
        radius (float | Unset):
        via (list[str] | Unset):
        via_minimum_stay (list[int] | Unset):
        time (datetime.datetime | Unset):
        max_transfers (int | Unset):
        max_travel_time (int | Unset):
        min_transfer_time (int | Unset):  Default: 0.
        additional_transfer_time (int | Unset):  Default: 0.
        transfer_time_factor (float | Unset):  Default: 1.0.
        max_matching_distance (float | Unset):  Default: 25.0.
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
        use_routed_transfers (bool | Unset):  Default: False.
        detailed_transfers (bool | Unset):
        detailed_legs (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        transit_modes (list[Mode] | Unset):
        direct_modes (list[Mode] | Unset):
        pre_transit_modes (list[Mode] | Unset):
        post_transit_modes (list[Mode] | Unset):
        direct_rental_form_factors (list[RentalFormFactor] | Unset):
        pre_transit_rental_form_factors (list[RentalFormFactor] | Unset):
        post_transit_rental_form_factors (list[RentalFormFactor] | Unset):
        direct_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        pre_transit_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        post_transit_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        direct_rental_providers (list[str] | Unset):
        direct_rental_provider_groups (list[str] | Unset):
        pre_transit_rental_providers (list[str] | Unset):
        pre_transit_rental_provider_groups (list[str] | Unset):
        post_transit_rental_providers (list[str] | Unset):
        post_transit_rental_provider_groups (list[str] | Unset):
        ignore_direct_rental_return_constraints (bool | Unset):  Default: False.
        ignore_pre_transit_rental_return_constraints (bool | Unset):  Default: False.
        ignore_post_transit_rental_return_constraints (bool | Unset):  Default: False.
        num_itineraries (int | Unset):  Default: 5.
        max_itineraries (int | Unset):
        page_cursor (str | Unset):
        timetable_view (bool | Unset):  Default: True.
        arrive_by (bool | Unset):  Default: False.
        search_window (int | Unset):  Default: 900.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.
        max_pre_transit_time (int | Unset):  Default: 900.
        max_post_transit_time (int | Unset):  Default: 900.
        max_direct_time (int | Unset):  Default: 1800.
        fastest_direct_factor (float | Unset):  Default: 1.0.
        timeout (int | Unset):
        passengers (int | Unset):
        luggage (int | Unset):
        slow_direct (bool | Unset):  Default: False.
        fastest_slow_direct_factor (float | Unset):  Default: 3.0.
        with_fares (bool | Unset):  Default: False.
        num_leg_alternatives (int | Unset):  Default: 0.
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        language (list[str] | Unset):
        algorithm (PlanAlgorithm | Unset):  Default: PlanAlgorithm.PONG.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PlanResponse200
    """

    return sync_detailed(
        client=client,
        from_place=from_place,
        to_place=to_place,
        radius=radius,
        via=via,
        via_minimum_stay=via_minimum_stay,
        time=time,
        max_transfers=max_transfers,
        max_travel_time=max_travel_time,
        min_transfer_time=min_transfer_time,
        additional_transfer_time=additional_transfer_time,
        transfer_time_factor=transfer_time_factor,
        max_matching_distance=max_matching_distance,
        pedestrian_profile=pedestrian_profile,
        pedestrian_speed=pedestrian_speed,
        cycling_speed=cycling_speed,
        elevation_costs=elevation_costs,
        use_routed_transfers=use_routed_transfers,
        detailed_transfers=detailed_transfers,
        detailed_legs=detailed_legs,
        join_interlined_legs=join_interlined_legs,
        transit_modes=transit_modes,
        direct_modes=direct_modes,
        pre_transit_modes=pre_transit_modes,
        post_transit_modes=post_transit_modes,
        direct_rental_form_factors=direct_rental_form_factors,
        pre_transit_rental_form_factors=pre_transit_rental_form_factors,
        post_transit_rental_form_factors=post_transit_rental_form_factors,
        direct_rental_propulsion_types=direct_rental_propulsion_types,
        pre_transit_rental_propulsion_types=pre_transit_rental_propulsion_types,
        post_transit_rental_propulsion_types=post_transit_rental_propulsion_types,
        direct_rental_providers=direct_rental_providers,
        direct_rental_provider_groups=direct_rental_provider_groups,
        pre_transit_rental_providers=pre_transit_rental_providers,
        pre_transit_rental_provider_groups=pre_transit_rental_provider_groups,
        post_transit_rental_providers=post_transit_rental_providers,
        post_transit_rental_provider_groups=post_transit_rental_provider_groups,
        ignore_direct_rental_return_constraints=ignore_direct_rental_return_constraints,
        ignore_pre_transit_rental_return_constraints=ignore_pre_transit_rental_return_constraints,
        ignore_post_transit_rental_return_constraints=ignore_post_transit_rental_return_constraints,
        num_itineraries=num_itineraries,
        max_itineraries=max_itineraries,
        page_cursor=page_cursor,
        timetable_view=timetable_view,
        arrive_by=arrive_by,
        search_window=search_window,
        require_bike_transport=require_bike_transport,
        require_car_transport=require_car_transport,
        max_pre_transit_time=max_pre_transit_time,
        max_post_transit_time=max_post_transit_time,
        max_direct_time=max_direct_time,
        fastest_direct_factor=fastest_direct_factor,
        timeout=timeout,
        passengers=passengers,
        luggage=luggage,
        slow_direct=slow_direct,
        fastest_slow_direct_factor=fastest_slow_direct_factor,
        with_fares=with_fares,
        num_leg_alternatives=num_leg_alternatives,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        language=language,
        algorithm=algorithm,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_place: str,
    to_place: str,
    radius: float | Unset = UNSET,
    via: list[str] | Unset = UNSET,
    via_minimum_stay: list[int] | Unset = UNSET,
    time: datetime.datetime | Unset = UNSET,
    max_transfers: int | Unset = UNSET,
    max_travel_time: int | Unset = UNSET,
    min_transfer_time: int | Unset = 0,
    additional_transfer_time: int | Unset = 0,
    transfer_time_factor: float | Unset = 1.0,
    max_matching_distance: float | Unset = 25.0,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    pedestrian_speed: float | Unset = UNSET,
    cycling_speed: float | Unset = UNSET,
    elevation_costs: ElevationCosts | Unset = UNSET,
    use_routed_transfers: bool | Unset = False,
    detailed_transfers: bool | Unset = UNSET,
    detailed_legs: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    transit_modes: list[Mode] | Unset = UNSET,
    direct_modes: list[Mode] | Unset = UNSET,
    pre_transit_modes: list[Mode] | Unset = UNSET,
    post_transit_modes: list[Mode] | Unset = UNSET,
    direct_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    pre_transit_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    post_transit_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    direct_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    pre_transit_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    post_transit_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    direct_rental_providers: list[str] | Unset = UNSET,
    direct_rental_provider_groups: list[str] | Unset = UNSET,
    pre_transit_rental_providers: list[str] | Unset = UNSET,
    pre_transit_rental_provider_groups: list[str] | Unset = UNSET,
    post_transit_rental_providers: list[str] | Unset = UNSET,
    post_transit_rental_provider_groups: list[str] | Unset = UNSET,
    ignore_direct_rental_return_constraints: bool | Unset = False,
    ignore_pre_transit_rental_return_constraints: bool | Unset = False,
    ignore_post_transit_rental_return_constraints: bool | Unset = False,
    num_itineraries: int | Unset = 5,
    max_itineraries: int | Unset = UNSET,
    page_cursor: str | Unset = UNSET,
    timetable_view: bool | Unset = True,
    arrive_by: bool | Unset = False,
    search_window: int | Unset = 900,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
    max_pre_transit_time: int | Unset = 900,
    max_post_transit_time: int | Unset = 900,
    max_direct_time: int | Unset = 1800,
    fastest_direct_factor: float | Unset = 1.0,
    timeout: int | Unset = UNSET,
    passengers: int | Unset = UNSET,
    luggage: int | Unset = UNSET,
    slow_direct: bool | Unset = False,
    fastest_slow_direct_factor: float | Unset = 3.0,
    with_fares: bool | Unset = False,
    num_leg_alternatives: int | Unset = 0,
    with_scheduled_skipped_stops: bool | Unset = False,
    language: list[str] | Unset = UNSET,
    algorithm: PlanAlgorithm | Unset = PlanAlgorithm.PONG,
) -> Response[Error | PlanResponse200]:
    """Computes optimal connections from one place to another.

    Args:
        from_place (str):
        to_place (str):
        radius (float | Unset):
        via (list[str] | Unset):
        via_minimum_stay (list[int] | Unset):
        time (datetime.datetime | Unset):
        max_transfers (int | Unset):
        max_travel_time (int | Unset):
        min_transfer_time (int | Unset):  Default: 0.
        additional_transfer_time (int | Unset):  Default: 0.
        transfer_time_factor (float | Unset):  Default: 1.0.
        max_matching_distance (float | Unset):  Default: 25.0.
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
        use_routed_transfers (bool | Unset):  Default: False.
        detailed_transfers (bool | Unset):
        detailed_legs (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        transit_modes (list[Mode] | Unset):
        direct_modes (list[Mode] | Unset):
        pre_transit_modes (list[Mode] | Unset):
        post_transit_modes (list[Mode] | Unset):
        direct_rental_form_factors (list[RentalFormFactor] | Unset):
        pre_transit_rental_form_factors (list[RentalFormFactor] | Unset):
        post_transit_rental_form_factors (list[RentalFormFactor] | Unset):
        direct_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        pre_transit_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        post_transit_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        direct_rental_providers (list[str] | Unset):
        direct_rental_provider_groups (list[str] | Unset):
        pre_transit_rental_providers (list[str] | Unset):
        pre_transit_rental_provider_groups (list[str] | Unset):
        post_transit_rental_providers (list[str] | Unset):
        post_transit_rental_provider_groups (list[str] | Unset):
        ignore_direct_rental_return_constraints (bool | Unset):  Default: False.
        ignore_pre_transit_rental_return_constraints (bool | Unset):  Default: False.
        ignore_post_transit_rental_return_constraints (bool | Unset):  Default: False.
        num_itineraries (int | Unset):  Default: 5.
        max_itineraries (int | Unset):
        page_cursor (str | Unset):
        timetable_view (bool | Unset):  Default: True.
        arrive_by (bool | Unset):  Default: False.
        search_window (int | Unset):  Default: 900.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.
        max_pre_transit_time (int | Unset):  Default: 900.
        max_post_transit_time (int | Unset):  Default: 900.
        max_direct_time (int | Unset):  Default: 1800.
        fastest_direct_factor (float | Unset):  Default: 1.0.
        timeout (int | Unset):
        passengers (int | Unset):
        luggage (int | Unset):
        slow_direct (bool | Unset):  Default: False.
        fastest_slow_direct_factor (float | Unset):  Default: 3.0.
        with_fares (bool | Unset):  Default: False.
        num_leg_alternatives (int | Unset):  Default: 0.
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        language (list[str] | Unset):
        algorithm (PlanAlgorithm | Unset):  Default: PlanAlgorithm.PONG.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PlanResponse200]
    """

    kwargs = _get_kwargs(
        from_place=from_place,
        to_place=to_place,
        radius=radius,
        via=via,
        via_minimum_stay=via_minimum_stay,
        time=time,
        max_transfers=max_transfers,
        max_travel_time=max_travel_time,
        min_transfer_time=min_transfer_time,
        additional_transfer_time=additional_transfer_time,
        transfer_time_factor=transfer_time_factor,
        max_matching_distance=max_matching_distance,
        pedestrian_profile=pedestrian_profile,
        pedestrian_speed=pedestrian_speed,
        cycling_speed=cycling_speed,
        elevation_costs=elevation_costs,
        use_routed_transfers=use_routed_transfers,
        detailed_transfers=detailed_transfers,
        detailed_legs=detailed_legs,
        join_interlined_legs=join_interlined_legs,
        transit_modes=transit_modes,
        direct_modes=direct_modes,
        pre_transit_modes=pre_transit_modes,
        post_transit_modes=post_transit_modes,
        direct_rental_form_factors=direct_rental_form_factors,
        pre_transit_rental_form_factors=pre_transit_rental_form_factors,
        post_transit_rental_form_factors=post_transit_rental_form_factors,
        direct_rental_propulsion_types=direct_rental_propulsion_types,
        pre_transit_rental_propulsion_types=pre_transit_rental_propulsion_types,
        post_transit_rental_propulsion_types=post_transit_rental_propulsion_types,
        direct_rental_providers=direct_rental_providers,
        direct_rental_provider_groups=direct_rental_provider_groups,
        pre_transit_rental_providers=pre_transit_rental_providers,
        pre_transit_rental_provider_groups=pre_transit_rental_provider_groups,
        post_transit_rental_providers=post_transit_rental_providers,
        post_transit_rental_provider_groups=post_transit_rental_provider_groups,
        ignore_direct_rental_return_constraints=ignore_direct_rental_return_constraints,
        ignore_pre_transit_rental_return_constraints=ignore_pre_transit_rental_return_constraints,
        ignore_post_transit_rental_return_constraints=ignore_post_transit_rental_return_constraints,
        num_itineraries=num_itineraries,
        max_itineraries=max_itineraries,
        page_cursor=page_cursor,
        timetable_view=timetable_view,
        arrive_by=arrive_by,
        search_window=search_window,
        require_bike_transport=require_bike_transport,
        require_car_transport=require_car_transport,
        max_pre_transit_time=max_pre_transit_time,
        max_post_transit_time=max_post_transit_time,
        max_direct_time=max_direct_time,
        fastest_direct_factor=fastest_direct_factor,
        timeout=timeout,
        passengers=passengers,
        luggage=luggage,
        slow_direct=slow_direct,
        fastest_slow_direct_factor=fastest_slow_direct_factor,
        with_fares=with_fares,
        num_leg_alternatives=num_leg_alternatives,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        language=language,
        algorithm=algorithm,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_place: str,
    to_place: str,
    radius: float | Unset = UNSET,
    via: list[str] | Unset = UNSET,
    via_minimum_stay: list[int] | Unset = UNSET,
    time: datetime.datetime | Unset = UNSET,
    max_transfers: int | Unset = UNSET,
    max_travel_time: int | Unset = UNSET,
    min_transfer_time: int | Unset = 0,
    additional_transfer_time: int | Unset = 0,
    transfer_time_factor: float | Unset = 1.0,
    max_matching_distance: float | Unset = 25.0,
    pedestrian_profile: PedestrianProfile | Unset = UNSET,
    pedestrian_speed: float | Unset = UNSET,
    cycling_speed: float | Unset = UNSET,
    elevation_costs: ElevationCosts | Unset = UNSET,
    use_routed_transfers: bool | Unset = False,
    detailed_transfers: bool | Unset = UNSET,
    detailed_legs: bool | Unset = True,
    join_interlined_legs: bool | Unset = True,
    transit_modes: list[Mode] | Unset = UNSET,
    direct_modes: list[Mode] | Unset = UNSET,
    pre_transit_modes: list[Mode] | Unset = UNSET,
    post_transit_modes: list[Mode] | Unset = UNSET,
    direct_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    pre_transit_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    post_transit_rental_form_factors: list[RentalFormFactor] | Unset = UNSET,
    direct_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    pre_transit_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    post_transit_rental_propulsion_types: list[RentalPropulsionType] | Unset = UNSET,
    direct_rental_providers: list[str] | Unset = UNSET,
    direct_rental_provider_groups: list[str] | Unset = UNSET,
    pre_transit_rental_providers: list[str] | Unset = UNSET,
    pre_transit_rental_provider_groups: list[str] | Unset = UNSET,
    post_transit_rental_providers: list[str] | Unset = UNSET,
    post_transit_rental_provider_groups: list[str] | Unset = UNSET,
    ignore_direct_rental_return_constraints: bool | Unset = False,
    ignore_pre_transit_rental_return_constraints: bool | Unset = False,
    ignore_post_transit_rental_return_constraints: bool | Unset = False,
    num_itineraries: int | Unset = 5,
    max_itineraries: int | Unset = UNSET,
    page_cursor: str | Unset = UNSET,
    timetable_view: bool | Unset = True,
    arrive_by: bool | Unset = False,
    search_window: int | Unset = 900,
    require_bike_transport: bool | Unset = False,
    require_car_transport: bool | Unset = False,
    max_pre_transit_time: int | Unset = 900,
    max_post_transit_time: int | Unset = 900,
    max_direct_time: int | Unset = 1800,
    fastest_direct_factor: float | Unset = 1.0,
    timeout: int | Unset = UNSET,
    passengers: int | Unset = UNSET,
    luggage: int | Unset = UNSET,
    slow_direct: bool | Unset = False,
    fastest_slow_direct_factor: float | Unset = 3.0,
    with_fares: bool | Unset = False,
    num_leg_alternatives: int | Unset = 0,
    with_scheduled_skipped_stops: bool | Unset = False,
    language: list[str] | Unset = UNSET,
    algorithm: PlanAlgorithm | Unset = PlanAlgorithm.PONG,
) -> Error | PlanResponse200 | None:
    """Computes optimal connections from one place to another.

    Args:
        from_place (str):
        to_place (str):
        radius (float | Unset):
        via (list[str] | Unset):
        via_minimum_stay (list[int] | Unset):
        time (datetime.datetime | Unset):
        max_transfers (int | Unset):
        max_travel_time (int | Unset):
        min_transfer_time (int | Unset):  Default: 0.
        additional_transfer_time (int | Unset):  Default: 0.
        transfer_time_factor (float | Unset):  Default: 1.0.
        max_matching_distance (float | Unset):  Default: 25.0.
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
        use_routed_transfers (bool | Unset):  Default: False.
        detailed_transfers (bool | Unset):
        detailed_legs (bool | Unset):  Default: True.
        join_interlined_legs (bool | Unset):  Default: True.
        transit_modes (list[Mode] | Unset):
        direct_modes (list[Mode] | Unset):
        pre_transit_modes (list[Mode] | Unset):
        post_transit_modes (list[Mode] | Unset):
        direct_rental_form_factors (list[RentalFormFactor] | Unset):
        pre_transit_rental_form_factors (list[RentalFormFactor] | Unset):
        post_transit_rental_form_factors (list[RentalFormFactor] | Unset):
        direct_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        pre_transit_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        post_transit_rental_propulsion_types (list[RentalPropulsionType] | Unset):
        direct_rental_providers (list[str] | Unset):
        direct_rental_provider_groups (list[str] | Unset):
        pre_transit_rental_providers (list[str] | Unset):
        pre_transit_rental_provider_groups (list[str] | Unset):
        post_transit_rental_providers (list[str] | Unset):
        post_transit_rental_provider_groups (list[str] | Unset):
        ignore_direct_rental_return_constraints (bool | Unset):  Default: False.
        ignore_pre_transit_rental_return_constraints (bool | Unset):  Default: False.
        ignore_post_transit_rental_return_constraints (bool | Unset):  Default: False.
        num_itineraries (int | Unset):  Default: 5.
        max_itineraries (int | Unset):
        page_cursor (str | Unset):
        timetable_view (bool | Unset):  Default: True.
        arrive_by (bool | Unset):  Default: False.
        search_window (int | Unset):  Default: 900.
        require_bike_transport (bool | Unset):  Default: False.
        require_car_transport (bool | Unset):  Default: False.
        max_pre_transit_time (int | Unset):  Default: 900.
        max_post_transit_time (int | Unset):  Default: 900.
        max_direct_time (int | Unset):  Default: 1800.
        fastest_direct_factor (float | Unset):  Default: 1.0.
        timeout (int | Unset):
        passengers (int | Unset):
        luggage (int | Unset):
        slow_direct (bool | Unset):  Default: False.
        fastest_slow_direct_factor (float | Unset):  Default: 3.0.
        with_fares (bool | Unset):  Default: False.
        num_leg_alternatives (int | Unset):  Default: 0.
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        language (list[str] | Unset):
        algorithm (PlanAlgorithm | Unset):  Default: PlanAlgorithm.PONG.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PlanResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            from_place=from_place,
            to_place=to_place,
            radius=radius,
            via=via,
            via_minimum_stay=via_minimum_stay,
            time=time,
            max_transfers=max_transfers,
            max_travel_time=max_travel_time,
            min_transfer_time=min_transfer_time,
            additional_transfer_time=additional_transfer_time,
            transfer_time_factor=transfer_time_factor,
            max_matching_distance=max_matching_distance,
            pedestrian_profile=pedestrian_profile,
            pedestrian_speed=pedestrian_speed,
            cycling_speed=cycling_speed,
            elevation_costs=elevation_costs,
            use_routed_transfers=use_routed_transfers,
            detailed_transfers=detailed_transfers,
            detailed_legs=detailed_legs,
            join_interlined_legs=join_interlined_legs,
            transit_modes=transit_modes,
            direct_modes=direct_modes,
            pre_transit_modes=pre_transit_modes,
            post_transit_modes=post_transit_modes,
            direct_rental_form_factors=direct_rental_form_factors,
            pre_transit_rental_form_factors=pre_transit_rental_form_factors,
            post_transit_rental_form_factors=post_transit_rental_form_factors,
            direct_rental_propulsion_types=direct_rental_propulsion_types,
            pre_transit_rental_propulsion_types=pre_transit_rental_propulsion_types,
            post_transit_rental_propulsion_types=post_transit_rental_propulsion_types,
            direct_rental_providers=direct_rental_providers,
            direct_rental_provider_groups=direct_rental_provider_groups,
            pre_transit_rental_providers=pre_transit_rental_providers,
            pre_transit_rental_provider_groups=pre_transit_rental_provider_groups,
            post_transit_rental_providers=post_transit_rental_providers,
            post_transit_rental_provider_groups=post_transit_rental_provider_groups,
            ignore_direct_rental_return_constraints=ignore_direct_rental_return_constraints,
            ignore_pre_transit_rental_return_constraints=ignore_pre_transit_rental_return_constraints,
            ignore_post_transit_rental_return_constraints=ignore_post_transit_rental_return_constraints,
            num_itineraries=num_itineraries,
            max_itineraries=max_itineraries,
            page_cursor=page_cursor,
            timetable_view=timetable_view,
            arrive_by=arrive_by,
            search_window=search_window,
            require_bike_transport=require_bike_transport,
            require_car_transport=require_car_transport,
            max_pre_transit_time=max_pre_transit_time,
            max_post_transit_time=max_post_transit_time,
            max_direct_time=max_direct_time,
            fastest_direct_factor=fastest_direct_factor,
            timeout=timeout,
            passengers=passengers,
            luggage=luggage,
            slow_direct=slow_direct,
            fastest_slow_direct_factor=fastest_slow_direct_factor,
            with_fares=with_fares,
            num_leg_alternatives=num_leg_alternatives,
            with_scheduled_skipped_stops=with_scheduled_skipped_stops,
            language=language,
            algorithm=algorithm,
        )
    ).parsed
