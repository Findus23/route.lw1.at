import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.mode import Mode
from ...models.stoptimes_direction import StoptimesDirection
from ...models.stoptimes_response_200 import StoptimesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    stop_id: str | Unset = UNSET,
    center: str | Unset = UNSET,
    time: datetime.datetime | Unset = UNSET,
    arrive_by: bool | Unset = False,
    direction: StoptimesDirection | Unset = UNSET,
    window: int | Unset = UNSET,
    mode: list[Mode] | Unset = UNSET,
    n: int | Unset = UNSET,
    radius: int | Unset = UNSET,
    exact_radius: bool | Unset = False,
    fetch_stops: bool | Unset = UNSET,
    page_cursor: str | Unset = UNSET,
    with_scheduled_skipped_stops: bool | Unset = False,
    language: list[str] | Unset = UNSET,
    with_alerts: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["stopId"] = stop_id

    params["center"] = center

    json_time: str | Unset = UNSET
    if not isinstance(time, Unset):
        json_time = time.isoformat()
    params["time"] = json_time

    params["arriveBy"] = arrive_by

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    params["window"] = window

    json_mode: list[str] | Unset = UNSET
    if not isinstance(mode, Unset):
        json_mode = []
        for mode_item_data in mode:
            mode_item = mode_item_data.value
            json_mode.append(mode_item)

    params["mode"] = json_mode

    params["n"] = n

    params["radius"] = radius

    params["exactRadius"] = exact_radius

    params["fetchStops"] = fetch_stops

    params["pageCursor"] = page_cursor

    params["withScheduledSkippedStops"] = with_scheduled_skipped_stops

    json_language: list[str] | Unset = UNSET
    if not isinstance(language, Unset):
        json_language = language

    params["language"] = json_language

    params["withAlerts"] = with_alerts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v6/stoptimes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | StoptimesResponse200 | None:
    if response.status_code == 200:
        response_200 = StoptimesResponse200.from_dict(response.json())

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
) -> Response[Error | StoptimesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    stop_id: str | Unset = UNSET,
    center: str | Unset = UNSET,
    time: datetime.datetime | Unset = UNSET,
    arrive_by: bool | Unset = False,
    direction: StoptimesDirection | Unset = UNSET,
    window: int | Unset = UNSET,
    mode: list[Mode] | Unset = UNSET,
    n: int | Unset = UNSET,
    radius: int | Unset = UNSET,
    exact_radius: bool | Unset = False,
    fetch_stops: bool | Unset = UNSET,
    page_cursor: str | Unset = UNSET,
    with_scheduled_skipped_stops: bool | Unset = False,
    language: list[str] | Unset = UNSET,
    with_alerts: bool | Unset = True,
) -> Response[Error | StoptimesResponse200]:
    """Get the next N departures or arrivals of a stop sorted by time

    Args:
        stop_id (str | Unset):
        center (str | Unset):
        time (datetime.datetime | Unset):
        arrive_by (bool | Unset):  Default: False.
        direction (StoptimesDirection | Unset):
        window (int | Unset):
        mode (list[Mode] | Unset):
        n (int | Unset):
        radius (int | Unset):
        exact_radius (bool | Unset):  Default: False.
        fetch_stops (bool | Unset):
        page_cursor (str | Unset):
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        language (list[str] | Unset):
        with_alerts (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StoptimesResponse200]
    """

    kwargs = _get_kwargs(
        stop_id=stop_id,
        center=center,
        time=time,
        arrive_by=arrive_by,
        direction=direction,
        window=window,
        mode=mode,
        n=n,
        radius=radius,
        exact_radius=exact_radius,
        fetch_stops=fetch_stops,
        page_cursor=page_cursor,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        language=language,
        with_alerts=with_alerts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    stop_id: str | Unset = UNSET,
    center: str | Unset = UNSET,
    time: datetime.datetime | Unset = UNSET,
    arrive_by: bool | Unset = False,
    direction: StoptimesDirection | Unset = UNSET,
    window: int | Unset = UNSET,
    mode: list[Mode] | Unset = UNSET,
    n: int | Unset = UNSET,
    radius: int | Unset = UNSET,
    exact_radius: bool | Unset = False,
    fetch_stops: bool | Unset = UNSET,
    page_cursor: str | Unset = UNSET,
    with_scheduled_skipped_stops: bool | Unset = False,
    language: list[str] | Unset = UNSET,
    with_alerts: bool | Unset = True,
) -> Error | StoptimesResponse200 | None:
    """Get the next N departures or arrivals of a stop sorted by time

    Args:
        stop_id (str | Unset):
        center (str | Unset):
        time (datetime.datetime | Unset):
        arrive_by (bool | Unset):  Default: False.
        direction (StoptimesDirection | Unset):
        window (int | Unset):
        mode (list[Mode] | Unset):
        n (int | Unset):
        radius (int | Unset):
        exact_radius (bool | Unset):  Default: False.
        fetch_stops (bool | Unset):
        page_cursor (str | Unset):
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        language (list[str] | Unset):
        with_alerts (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StoptimesResponse200
    """

    return sync_detailed(
        client=client,
        stop_id=stop_id,
        center=center,
        time=time,
        arrive_by=arrive_by,
        direction=direction,
        window=window,
        mode=mode,
        n=n,
        radius=radius,
        exact_radius=exact_radius,
        fetch_stops=fetch_stops,
        page_cursor=page_cursor,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        language=language,
        with_alerts=with_alerts,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    stop_id: str | Unset = UNSET,
    center: str | Unset = UNSET,
    time: datetime.datetime | Unset = UNSET,
    arrive_by: bool | Unset = False,
    direction: StoptimesDirection | Unset = UNSET,
    window: int | Unset = UNSET,
    mode: list[Mode] | Unset = UNSET,
    n: int | Unset = UNSET,
    radius: int | Unset = UNSET,
    exact_radius: bool | Unset = False,
    fetch_stops: bool | Unset = UNSET,
    page_cursor: str | Unset = UNSET,
    with_scheduled_skipped_stops: bool | Unset = False,
    language: list[str] | Unset = UNSET,
    with_alerts: bool | Unset = True,
) -> Response[Error | StoptimesResponse200]:
    """Get the next N departures or arrivals of a stop sorted by time

    Args:
        stop_id (str | Unset):
        center (str | Unset):
        time (datetime.datetime | Unset):
        arrive_by (bool | Unset):  Default: False.
        direction (StoptimesDirection | Unset):
        window (int | Unset):
        mode (list[Mode] | Unset):
        n (int | Unset):
        radius (int | Unset):
        exact_radius (bool | Unset):  Default: False.
        fetch_stops (bool | Unset):
        page_cursor (str | Unset):
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        language (list[str] | Unset):
        with_alerts (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StoptimesResponse200]
    """

    kwargs = _get_kwargs(
        stop_id=stop_id,
        center=center,
        time=time,
        arrive_by=arrive_by,
        direction=direction,
        window=window,
        mode=mode,
        n=n,
        radius=radius,
        exact_radius=exact_radius,
        fetch_stops=fetch_stops,
        page_cursor=page_cursor,
        with_scheduled_skipped_stops=with_scheduled_skipped_stops,
        language=language,
        with_alerts=with_alerts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    stop_id: str | Unset = UNSET,
    center: str | Unset = UNSET,
    time: datetime.datetime | Unset = UNSET,
    arrive_by: bool | Unset = False,
    direction: StoptimesDirection | Unset = UNSET,
    window: int | Unset = UNSET,
    mode: list[Mode] | Unset = UNSET,
    n: int | Unset = UNSET,
    radius: int | Unset = UNSET,
    exact_radius: bool | Unset = False,
    fetch_stops: bool | Unset = UNSET,
    page_cursor: str | Unset = UNSET,
    with_scheduled_skipped_stops: bool | Unset = False,
    language: list[str] | Unset = UNSET,
    with_alerts: bool | Unset = True,
) -> Error | StoptimesResponse200 | None:
    """Get the next N departures or arrivals of a stop sorted by time

    Args:
        stop_id (str | Unset):
        center (str | Unset):
        time (datetime.datetime | Unset):
        arrive_by (bool | Unset):  Default: False.
        direction (StoptimesDirection | Unset):
        window (int | Unset):
        mode (list[Mode] | Unset):
        n (int | Unset):
        radius (int | Unset):
        exact_radius (bool | Unset):  Default: False.
        fetch_stops (bool | Unset):
        page_cursor (str | Unset):
        with_scheduled_skipped_stops (bool | Unset):  Default: False.
        language (list[str] | Unset):
        with_alerts (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StoptimesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            stop_id=stop_id,
            center=center,
            time=time,
            arrive_by=arrive_by,
            direction=direction,
            window=window,
            mode=mode,
            n=n,
            radius=radius,
            exact_radius=exact_radius,
            fetch_stops=fetch_stops,
            page_cursor=page_cursor,
            with_scheduled_skipped_stops=with_scheduled_skipped_stops,
            language=language,
            with_alerts=with_alerts,
        )
    ).parsed
