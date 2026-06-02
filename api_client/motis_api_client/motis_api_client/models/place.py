from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mode import Mode
from ..models.pickup_dropoff_type import PickupDropoffType
from ..models.vertex_type import VertexType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert


T = TypeVar("T", bound="Place")


@_attrs_define
class Place:
    """
    Attributes:
        name (str): name of the transit stop / PoI / address
        lat (float): latitude
        lon (float): longitude
        stop_id (str | Unset): The ID of the stop. This is often something that users don't care about.
        parent_id (str | Unset): If it's not a root stop, this field contains the `stopId` of the parent stop.
        importance (float | Unset): The importance of the stop between 0-1.
        level (float | Unset): level according to OpenStreetMap
            If no level is given, the field will be unset.

            For older versions (v1-v5), this field is mandatory and therefore set to 0.
            Affected endpoints: plan, trip, stoptimes, one-to-all, map/stops, map/trips
        tz (str | Unset): timezone name (e.g. "Europe/Berlin")
        arrival (datetime.datetime | Unset): arrival time
        departure (datetime.datetime | Unset): departure time
        scheduled_arrival (datetime.datetime | Unset): scheduled arrival time
        scheduled_departure (datetime.datetime | Unset): scheduled departure time
        scheduled_track (str | Unset): scheduled track from the static schedule timetable dataset
        track (str | Unset): The current track/platform information, updated with real-time updates if available.
            Can be missing if neither real-time updates nor the schedule timetable contains track information.
        stop_code (str | Unset): Short, abbreviated identifier of the stop intended for users
            (e.g. printed on signage, used in SMS / passenger info systems).
            Comes from the GTFS `stop_code` field.
        description (str | Unset): description of the location that provides more detailed information
        vertex_type (VertexType | Unset): - `NORMAL` - latitude / longitude coordinate or address
            - `BIKESHARE` - bike sharing station
            - `TRANSIT` - transit stop
        pickup_type (PickupDropoffType | Unset): - `NORMAL` - entry/exit is possible normally
            - `NOT_ALLOWED` - entry/exit is not allowed
        dropoff_type (PickupDropoffType | Unset): - `NORMAL` - entry/exit is possible normally
            - `NOT_ALLOWED` - entry/exit is not allowed
        cancelled (bool | Unset): Whether this stop is cancelled due to the realtime situation.
        alerts (list[Alert] | Unset): Alerts for this stop.
        flex (str | Unset): for `FLEX` transports, the flex location area or location group name
        flex_id (str | Unset): for `FLEX` transports, the flex location area ID or location group ID
        flex_start_pickup_drop_off_window (datetime.datetime | Unset): Time that on-demand service becomes available
        flex_end_pickup_drop_off_window (datetime.datetime | Unset): Time that on-demand service ends
        modes (list[Mode] | Unset): available transport modes for stops
    """

    name: str
    lat: float
    lon: float
    stop_id: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    importance: float | Unset = UNSET
    level: float | Unset = UNSET
    tz: str | Unset = UNSET
    arrival: datetime.datetime | Unset = UNSET
    departure: datetime.datetime | Unset = UNSET
    scheduled_arrival: datetime.datetime | Unset = UNSET
    scheduled_departure: datetime.datetime | Unset = UNSET
    scheduled_track: str | Unset = UNSET
    track: str | Unset = UNSET
    stop_code: str | Unset = UNSET
    description: str | Unset = UNSET
    vertex_type: VertexType | Unset = UNSET
    pickup_type: PickupDropoffType | Unset = UNSET
    dropoff_type: PickupDropoffType | Unset = UNSET
    cancelled: bool | Unset = UNSET
    alerts: list[Alert] | Unset = UNSET
    flex: str | Unset = UNSET
    flex_id: str | Unset = UNSET
    flex_start_pickup_drop_off_window: datetime.datetime | Unset = UNSET
    flex_end_pickup_drop_off_window: datetime.datetime | Unset = UNSET
    modes: list[Mode] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        lat = self.lat

        lon = self.lon

        stop_id = self.stop_id

        parent_id = self.parent_id

        importance = self.importance

        level = self.level

        tz = self.tz

        arrival: str | Unset = UNSET
        if not isinstance(self.arrival, Unset):
            arrival = self.arrival.isoformat()

        departure: str | Unset = UNSET
        if not isinstance(self.departure, Unset):
            departure = self.departure.isoformat()

        scheduled_arrival: str | Unset = UNSET
        if not isinstance(self.scheduled_arrival, Unset):
            scheduled_arrival = self.scheduled_arrival.isoformat()

        scheduled_departure: str | Unset = UNSET
        if not isinstance(self.scheduled_departure, Unset):
            scheduled_departure = self.scheduled_departure.isoformat()

        scheduled_track = self.scheduled_track

        track = self.track

        stop_code = self.stop_code

        description = self.description

        vertex_type: str | Unset = UNSET
        if not isinstance(self.vertex_type, Unset):
            vertex_type = self.vertex_type.value

        pickup_type: str | Unset = UNSET
        if not isinstance(self.pickup_type, Unset):
            pickup_type = self.pickup_type.value

        dropoff_type: str | Unset = UNSET
        if not isinstance(self.dropoff_type, Unset):
            dropoff_type = self.dropoff_type.value

        cancelled = self.cancelled

        alerts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item = alerts_item_data.to_dict()
                alerts.append(alerts_item)

        flex = self.flex

        flex_id = self.flex_id

        flex_start_pickup_drop_off_window: str | Unset = UNSET
        if not isinstance(self.flex_start_pickup_drop_off_window, Unset):
            flex_start_pickup_drop_off_window = self.flex_start_pickup_drop_off_window.isoformat()

        flex_end_pickup_drop_off_window: str | Unset = UNSET
        if not isinstance(self.flex_end_pickup_drop_off_window, Unset):
            flex_end_pickup_drop_off_window = self.flex_end_pickup_drop_off_window.isoformat()

        modes: list[str] | Unset = UNSET
        if not isinstance(self.modes, Unset):
            modes = []
            for modes_item_data in self.modes:
                modes_item = modes_item_data.value
                modes.append(modes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "lat": lat,
                "lon": lon,
            }
        )
        if stop_id is not UNSET:
            field_dict["stopId"] = stop_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if importance is not UNSET:
            field_dict["importance"] = importance
        if level is not UNSET:
            field_dict["level"] = level
        if tz is not UNSET:
            field_dict["tz"] = tz
        if arrival is not UNSET:
            field_dict["arrival"] = arrival
        if departure is not UNSET:
            field_dict["departure"] = departure
        if scheduled_arrival is not UNSET:
            field_dict["scheduledArrival"] = scheduled_arrival
        if scheduled_departure is not UNSET:
            field_dict["scheduledDeparture"] = scheduled_departure
        if scheduled_track is not UNSET:
            field_dict["scheduledTrack"] = scheduled_track
        if track is not UNSET:
            field_dict["track"] = track
        if stop_code is not UNSET:
            field_dict["stopCode"] = stop_code
        if description is not UNSET:
            field_dict["description"] = description
        if vertex_type is not UNSET:
            field_dict["vertexType"] = vertex_type
        if pickup_type is not UNSET:
            field_dict["pickupType"] = pickup_type
        if dropoff_type is not UNSET:
            field_dict["dropoffType"] = dropoff_type
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if alerts is not UNSET:
            field_dict["alerts"] = alerts
        if flex is not UNSET:
            field_dict["flex"] = flex
        if flex_id is not UNSET:
            field_dict["flexId"] = flex_id
        if flex_start_pickup_drop_off_window is not UNSET:
            field_dict["flexStartPickupDropOffWindow"] = flex_start_pickup_drop_off_window
        if flex_end_pickup_drop_off_window is not UNSET:
            field_dict["flexEndPickupDropOffWindow"] = flex_end_pickup_drop_off_window
        if modes is not UNSET:
            field_dict["modes"] = modes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert import Alert

        d = dict(src_dict)
        name = d.pop("name")

        lat = d.pop("lat")

        lon = d.pop("lon")

        stop_id = d.pop("stopId", UNSET)

        parent_id = d.pop("parentId", UNSET)

        importance = d.pop("importance", UNSET)

        level = d.pop("level", UNSET)

        tz = d.pop("tz", UNSET)

        _arrival = d.pop("arrival", UNSET)
        arrival: datetime.datetime | Unset
        if isinstance(_arrival, Unset):
            arrival = UNSET
        else:
            arrival = datetime.datetime.fromisoformat(_arrival)

        _departure = d.pop("departure", UNSET)
        departure: datetime.datetime | Unset
        if isinstance(_departure, Unset):
            departure = UNSET
        else:
            departure = datetime.datetime.fromisoformat(_departure)

        _scheduled_arrival = d.pop("scheduledArrival", UNSET)
        scheduled_arrival: datetime.datetime | Unset
        if isinstance(_scheduled_arrival, Unset):
            scheduled_arrival = UNSET
        else:
            scheduled_arrival = datetime.datetime.fromisoformat(_scheduled_arrival)

        _scheduled_departure = d.pop("scheduledDeparture", UNSET)
        scheduled_departure: datetime.datetime | Unset
        if isinstance(_scheduled_departure, Unset):
            scheduled_departure = UNSET
        else:
            scheduled_departure = datetime.datetime.fromisoformat(_scheduled_departure)

        scheduled_track = d.pop("scheduledTrack", UNSET)

        track = d.pop("track", UNSET)

        stop_code = d.pop("stopCode", UNSET)

        description = d.pop("description", UNSET)

        _vertex_type = d.pop("vertexType", UNSET)
        vertex_type: VertexType | Unset
        if isinstance(_vertex_type, Unset):
            vertex_type = UNSET
        else:
            vertex_type = VertexType(_vertex_type)

        _pickup_type = d.pop("pickupType", UNSET)
        pickup_type: PickupDropoffType | Unset
        if isinstance(_pickup_type, Unset):
            pickup_type = UNSET
        else:
            pickup_type = PickupDropoffType(_pickup_type)

        _dropoff_type = d.pop("dropoffType", UNSET)
        dropoff_type: PickupDropoffType | Unset
        if isinstance(_dropoff_type, Unset):
            dropoff_type = UNSET
        else:
            dropoff_type = PickupDropoffType(_dropoff_type)

        cancelled = d.pop("cancelled", UNSET)

        _alerts = d.pop("alerts", UNSET)
        alerts: list[Alert] | Unset = UNSET
        if _alerts is not UNSET:
            alerts = []
            for alerts_item_data in _alerts:
                alerts_item = Alert.from_dict(alerts_item_data)

                alerts.append(alerts_item)

        flex = d.pop("flex", UNSET)

        flex_id = d.pop("flexId", UNSET)

        _flex_start_pickup_drop_off_window = d.pop("flexStartPickupDropOffWindow", UNSET)
        flex_start_pickup_drop_off_window: datetime.datetime | Unset
        if isinstance(_flex_start_pickup_drop_off_window, Unset):
            flex_start_pickup_drop_off_window = UNSET
        else:
            flex_start_pickup_drop_off_window = datetime.datetime.fromisoformat(_flex_start_pickup_drop_off_window)

        _flex_end_pickup_drop_off_window = d.pop("flexEndPickupDropOffWindow", UNSET)
        flex_end_pickup_drop_off_window: datetime.datetime | Unset
        if isinstance(_flex_end_pickup_drop_off_window, Unset):
            flex_end_pickup_drop_off_window = UNSET
        else:
            flex_end_pickup_drop_off_window = datetime.datetime.fromisoformat(_flex_end_pickup_drop_off_window)

        _modes = d.pop("modes", UNSET)
        modes: list[Mode] | Unset = UNSET
        if _modes is not UNSET:
            modes = []
            for modes_item_data in _modes:
                modes_item = Mode(modes_item_data)

                modes.append(modes_item)

        place = cls(
            name=name,
            lat=lat,
            lon=lon,
            stop_id=stop_id,
            parent_id=parent_id,
            importance=importance,
            level=level,
            tz=tz,
            arrival=arrival,
            departure=departure,
            scheduled_arrival=scheduled_arrival,
            scheduled_departure=scheduled_departure,
            scheduled_track=scheduled_track,
            track=track,
            stop_code=stop_code,
            description=description,
            vertex_type=vertex_type,
            pickup_type=pickup_type,
            dropoff_type=dropoff_type,
            cancelled=cancelled,
            alerts=alerts,
            flex=flex,
            flex_id=flex_id,
            flex_start_pickup_drop_off_window=flex_start_pickup_drop_off_window,
            flex_end_pickup_drop_off_window=flex_end_pickup_drop_off_window,
            modes=modes,
        )

        place.additional_properties = d
        return place

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
