from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mode import Mode
from ..models.wheelchair_accessibility import WheelchairAccessibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert
    from ..models.category import Category
    from ..models.encoded_polyline import EncodedPolyline
    from ..models.place import Place
    from ..models.rental import Rental
    from ..models.step_instruction import StepInstruction


T = TypeVar("T", bound="Leg")


@_attrs_define
class Leg:
    """
    Attributes:
        mode (Mode): # Street modes

              - `WALK`
              - `BIKE`
              - `RENTAL` Experimental. Expect unannounced breaking changes (without version bumps) for all parameters and
            returned structs.
              - `CAR`
              - `CAR_PARKING` Experimental. Expect unannounced breaking changes (without version bumps) for all parameters
            and returned structs.
              - `CAR_DROPOFF` Experimental. Expect unannounced breaking changes (without version bumps) for all perameters
            and returned structs.
              - `ODM` on-demand taxis from the Prima+ÖV Project
              - `RIDE_SHARING` ride sharing from the Prima+ÖV Project
              - `FLEX` flexible transports

            # Transit modes

              - `TRANSIT`: translates to `TRAM,FERRY,AIRPLANE,BUS,COACH,RAIL,ODM,RIDE_SHARING,FUNICULAR,AERIAL_LIFT,OTHER`
              - `TRAM`: trams
              - `SUBWAY`: subway trains (Paris Metro, London Underground, but also NYC Subway, Hamburger Hochbahn, and other
            non-underground services)
              - `FERRY`: ferries
              - `AIRPLANE`: airline flights
              - `BUS`: short distance buses (does not include `COACH`)
              - `COACH`: long distance buses (does not include `BUS`)
              - `RAIL`: translates to `HIGHSPEED_RAIL,LONG_DISTANCE,NIGHT_RAIL,REGIONAL_RAIL,SUBURBAN,SUBWAY`
              - `HIGHSPEED_RAIL`: long distance high speed trains (e.g. TGV)
              - `LONG_DISTANCE`: long distance inter city trains
              - `NIGHT_RAIL`: long distance night trains
              - `REGIONAL_FAST_RAIL`: deprecated, `REGIONAL_RAIL` will be used
              - `REGIONAL_RAIL`: regional train
              - `SUBURBAN`: suburban trains (e.g. S-Bahn, RER, Elizabeth Line, ...)
              - `ODM`: demand responsive transport
              - `RIDE_SHARING`: ride sharing
              - `FUNICULAR`: Funicular. Any rail system designed for steep inclines.
              - `AERIAL_LIFT`: Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). Cable transport where
            cabins, cars, gondolas or open chairs are suspended by means of one or more cables.
              - `AREAL_LIFT`: deprecated
              - `METRO`: deprecated
              - `CABLE_CAR`: deprecated
        from_ (Place):
        to (Place):
        duration (int): Leg duration in seconds

            If leg is footpath:
              The footpath duration is derived from the default footpath
              duration using the query parameters `transferTimeFactor` and
              `additionalTransferTime` as follows:
              `leg.duration = defaultDuration * transferTimeFactor + additionalTransferTime.`
              In case the defaultDuration is needed, it can be calculated by
              `defaultDuration = (leg.duration - additionalTransferTime) / transferTimeFactor`.
              Note that the default values are `transferTimeFactor = 1` and
              `additionalTransferTime = 0` in case they are not explicitly
              provided in the query.
        start_time (datetime.datetime): leg departure time
        end_time (datetime.datetime): leg arrival time
        scheduled_start_time (datetime.datetime): scheduled leg departure time
        scheduled_end_time (datetime.datetime): scheduled leg arrival time
        real_time (bool): Whether there is real-time data about this leg
        scheduled (bool): Whether this leg was originally scheduled to run or is an additional service.
            Scheduled times will equal realtime times in this case.
        leg_geometry (EncodedPolyline):
        distance (float | Unset): For non-transit legs the distance traveled while traversing this leg in meters.
        interline_with_previous_leg (bool | Unset): For transit legs, if the rider should stay on the vehicle as it
            changes route names.
        headsign (str | Unset): For transit legs, the headsign of the bus or train being used.
            For non-transit legs, null
        trip_from (Place | Unset):
        trip_to (Place | Unset):
        category (Category | Unset): not available for GTFS datasets by default
            For NeTEx it contains information about the vehicle category, e.g. IC/InterCity
        route_id (str | Unset):
        route_url (str | Unset):
        direction_id (str | Unset):
        route_color (str | Unset):
        route_text_color (str | Unset):
        route_type (int | Unset):
        agency_name (str | Unset):
        agency_url (str | Unset):
        agency_id (str | Unset):
        trip_id (str | Unset):
        route_short_name (str | Unset):
        route_long_name (str | Unset):
        trip_short_name (str | Unset):
        display_name (str | Unset):
        cancelled (bool | Unset): Whether this trip is cancelled
        source (str | Unset): Filename and line number where this trip is from
        intermediate_stops (list[Place] | Unset): For transit legs, intermediate stops between the Place where the leg
            originates
            and the Place where the leg ends. For non-transit legs, null.
        steps (list[StepInstruction] | Unset): A series of turn by turn instructions
            used for walking, biking and driving.
            This field is omitted if the request disables detailed leg output.
        rental (Rental | Unset): Vehicle rental
        fare_transfer_index (int | Unset): Index into `Itinerary.fareTransfers` array
            to identify which fare transfer this leg belongs to
        effective_fare_leg_index (int | Unset): Index into the
            `Itinerary.fareTransfers[fareTransferIndex].effectiveFareLegProducts` array
            to identify which effective fare leg this itinerary leg belongs to
        alerts (list[Alert] | Unset): Alerts for this stop.
        looped_calendar_since (datetime.datetime | Unset): If set, this attribute indicates that this trip has been
            expanded
            beyond the feed end date (enabled by config flag `timetable.dataset.extend_calendar`)
            by looping active weekdays, e.g. from calendar.txt in GTFS.
        bikes_allowed (bool | Unset): Whether bikes can be carried on this leg.
        wheelchair_accessible (WheelchairAccessibility | Unset):
        alternatives (list[list[Leg]] | Unset): Alternative connections that can replace this transit leg.
            Each alternative is normally a sequence of 3 legs:
            `[ingress footpath, transit, egress footpath]`.
            Only populated when the request sets `numLegAlternatives` > 0
            (capped to that value).

            Interlined legs:
            `alternatives` is populated only on the first (main) leg of
            an interlined chain. Subsequent interlined legs (carrying
            `interlineWithPreviousLeg=true`) leave `alternatives` unset.
            Alternatives are valid for the whole interlined segment.

            An alternative may itself cover an interlined segment:
            the alternative's middle transit then expands into multiple
            interlined legs when `joinInterlinedLegs=false`. In that
            case the alternative contains more than 3 legs: ingress
            footpath, followed by N interlined transit legs (the
            secondary ones carrying `interlineWithPreviousLeg=true`),
            followed by an egress footpath.
    """

    mode: Mode
    from_: Place
    to: Place
    duration: int
    start_time: datetime.datetime
    end_time: datetime.datetime
    scheduled_start_time: datetime.datetime
    scheduled_end_time: datetime.datetime
    real_time: bool
    scheduled: bool
    leg_geometry: EncodedPolyline
    distance: float | Unset = UNSET
    interline_with_previous_leg: bool | Unset = UNSET
    headsign: str | Unset = UNSET
    trip_from: Place | Unset = UNSET
    trip_to: Place | Unset = UNSET
    category: Category | Unset = UNSET
    route_id: str | Unset = UNSET
    route_url: str | Unset = UNSET
    direction_id: str | Unset = UNSET
    route_color: str | Unset = UNSET
    route_text_color: str | Unset = UNSET
    route_type: int | Unset = UNSET
    agency_name: str | Unset = UNSET
    agency_url: str | Unset = UNSET
    agency_id: str | Unset = UNSET
    trip_id: str | Unset = UNSET
    route_short_name: str | Unset = UNSET
    route_long_name: str | Unset = UNSET
    trip_short_name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    cancelled: bool | Unset = UNSET
    source: str | Unset = UNSET
    intermediate_stops: list[Place] | Unset = UNSET
    steps: list[StepInstruction] | Unset = UNSET
    rental: Rental | Unset = UNSET
    fare_transfer_index: int | Unset = UNSET
    effective_fare_leg_index: int | Unset = UNSET
    alerts: list[Alert] | Unset = UNSET
    looped_calendar_since: datetime.datetime | Unset = UNSET
    bikes_allowed: bool | Unset = UNSET
    wheelchair_accessible: WheelchairAccessibility | Unset = UNSET
    alternatives: list[list[Leg]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        from_ = self.from_.to_dict()

        to = self.to.to_dict()

        duration = self.duration

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        scheduled_start_time = self.scheduled_start_time.isoformat()

        scheduled_end_time = self.scheduled_end_time.isoformat()

        real_time = self.real_time

        scheduled = self.scheduled

        leg_geometry = self.leg_geometry.to_dict()

        distance = self.distance

        interline_with_previous_leg = self.interline_with_previous_leg

        headsign = self.headsign

        trip_from: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trip_from, Unset):
            trip_from = self.trip_from.to_dict()

        trip_to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trip_to, Unset):
            trip_to = self.trip_to.to_dict()

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        route_id = self.route_id

        route_url = self.route_url

        direction_id = self.direction_id

        route_color = self.route_color

        route_text_color = self.route_text_color

        route_type = self.route_type

        agency_name = self.agency_name

        agency_url = self.agency_url

        agency_id = self.agency_id

        trip_id = self.trip_id

        route_short_name = self.route_short_name

        route_long_name = self.route_long_name

        trip_short_name = self.trip_short_name

        display_name = self.display_name

        cancelled = self.cancelled

        source = self.source

        intermediate_stops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intermediate_stops, Unset):
            intermediate_stops = []
            for intermediate_stops_item_data in self.intermediate_stops:
                intermediate_stops_item = intermediate_stops_item_data.to_dict()
                intermediate_stops.append(intermediate_stops_item)

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        rental: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rental, Unset):
            rental = self.rental.to_dict()

        fare_transfer_index = self.fare_transfer_index

        effective_fare_leg_index = self.effective_fare_leg_index

        alerts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item = alerts_item_data.to_dict()
                alerts.append(alerts_item)

        looped_calendar_since: str | Unset = UNSET
        if not isinstance(self.looped_calendar_since, Unset):
            looped_calendar_since = self.looped_calendar_since.isoformat()

        bikes_allowed = self.bikes_allowed

        wheelchair_accessible: str | Unset = UNSET
        if not isinstance(self.wheelchair_accessible, Unset):
            wheelchair_accessible = self.wheelchair_accessible.value

        alternatives: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.alternatives, Unset):
            alternatives = []
            for alternatives_item_data in self.alternatives:
                alternatives_item = []
                for alternatives_item_item_data in alternatives_item_data:
                    alternatives_item_item = alternatives_item_item_data.to_dict()
                    alternatives_item.append(alternatives_item_item)

                alternatives.append(alternatives_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "from": from_,
                "to": to,
                "duration": duration,
                "startTime": start_time,
                "endTime": end_time,
                "scheduledStartTime": scheduled_start_time,
                "scheduledEndTime": scheduled_end_time,
                "realTime": real_time,
                "scheduled": scheduled,
                "legGeometry": leg_geometry,
            }
        )
        if distance is not UNSET:
            field_dict["distance"] = distance
        if interline_with_previous_leg is not UNSET:
            field_dict["interlineWithPreviousLeg"] = interline_with_previous_leg
        if headsign is not UNSET:
            field_dict["headsign"] = headsign
        if trip_from is not UNSET:
            field_dict["tripFrom"] = trip_from
        if trip_to is not UNSET:
            field_dict["tripTo"] = trip_to
        if category is not UNSET:
            field_dict["category"] = category
        if route_id is not UNSET:
            field_dict["routeId"] = route_id
        if route_url is not UNSET:
            field_dict["routeUrl"] = route_url
        if direction_id is not UNSET:
            field_dict["directionId"] = direction_id
        if route_color is not UNSET:
            field_dict["routeColor"] = route_color
        if route_text_color is not UNSET:
            field_dict["routeTextColor"] = route_text_color
        if route_type is not UNSET:
            field_dict["routeType"] = route_type
        if agency_name is not UNSET:
            field_dict["agencyName"] = agency_name
        if agency_url is not UNSET:
            field_dict["agencyUrl"] = agency_url
        if agency_id is not UNSET:
            field_dict["agencyId"] = agency_id
        if trip_id is not UNSET:
            field_dict["tripId"] = trip_id
        if route_short_name is not UNSET:
            field_dict["routeShortName"] = route_short_name
        if route_long_name is not UNSET:
            field_dict["routeLongName"] = route_long_name
        if trip_short_name is not UNSET:
            field_dict["tripShortName"] = trip_short_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if source is not UNSET:
            field_dict["source"] = source
        if intermediate_stops is not UNSET:
            field_dict["intermediateStops"] = intermediate_stops
        if steps is not UNSET:
            field_dict["steps"] = steps
        if rental is not UNSET:
            field_dict["rental"] = rental
        if fare_transfer_index is not UNSET:
            field_dict["fareTransferIndex"] = fare_transfer_index
        if effective_fare_leg_index is not UNSET:
            field_dict["effectiveFareLegIndex"] = effective_fare_leg_index
        if alerts is not UNSET:
            field_dict["alerts"] = alerts
        if looped_calendar_since is not UNSET:
            field_dict["loopedCalendarSince"] = looped_calendar_since
        if bikes_allowed is not UNSET:
            field_dict["bikesAllowed"] = bikes_allowed
        if wheelchair_accessible is not UNSET:
            field_dict["wheelchairAccessible"] = wheelchair_accessible
        if alternatives is not UNSET:
            field_dict["alternatives"] = alternatives

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert import Alert
        from ..models.category import Category
        from ..models.encoded_polyline import EncodedPolyline
        from ..models.place import Place
        from ..models.rental import Rental
        from ..models.step_instruction import StepInstruction

        d = dict(src_dict)
        mode = Mode(d.pop("mode"))

        from_ = Place.from_dict(d.pop("from"))

        to = Place.from_dict(d.pop("to"))

        duration = d.pop("duration")

        start_time = datetime.datetime.fromisoformat(d.pop("startTime"))

        end_time = datetime.datetime.fromisoformat(d.pop("endTime"))

        scheduled_start_time = datetime.datetime.fromisoformat(d.pop("scheduledStartTime"))

        scheduled_end_time = datetime.datetime.fromisoformat(d.pop("scheduledEndTime"))

        real_time = d.pop("realTime")

        scheduled = d.pop("scheduled")

        leg_geometry = EncodedPolyline.from_dict(d.pop("legGeometry"))

        distance = d.pop("distance", UNSET)

        interline_with_previous_leg = d.pop("interlineWithPreviousLeg", UNSET)

        headsign = d.pop("headsign", UNSET)

        _trip_from = d.pop("tripFrom", UNSET)
        trip_from: Place | Unset
        if isinstance(_trip_from, Unset):
            trip_from = UNSET
        else:
            trip_from = Place.from_dict(_trip_from)

        _trip_to = d.pop("tripTo", UNSET)
        trip_to: Place | Unset
        if isinstance(_trip_to, Unset):
            trip_to = UNSET
        else:
            trip_to = Place.from_dict(_trip_to)

        _category = d.pop("category", UNSET)
        category: Category | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = Category.from_dict(_category)

        route_id = d.pop("routeId", UNSET)

        route_url = d.pop("routeUrl", UNSET)

        direction_id = d.pop("directionId", UNSET)

        route_color = d.pop("routeColor", UNSET)

        route_text_color = d.pop("routeTextColor", UNSET)

        route_type = d.pop("routeType", UNSET)

        agency_name = d.pop("agencyName", UNSET)

        agency_url = d.pop("agencyUrl", UNSET)

        agency_id = d.pop("agencyId", UNSET)

        trip_id = d.pop("tripId", UNSET)

        route_short_name = d.pop("routeShortName", UNSET)

        route_long_name = d.pop("routeLongName", UNSET)

        trip_short_name = d.pop("tripShortName", UNSET)

        display_name = d.pop("displayName", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        source = d.pop("source", UNSET)

        _intermediate_stops = d.pop("intermediateStops", UNSET)
        intermediate_stops: list[Place] | Unset = UNSET
        if _intermediate_stops is not UNSET:
            intermediate_stops = []
            for intermediate_stops_item_data in _intermediate_stops:
                intermediate_stops_item = Place.from_dict(intermediate_stops_item_data)

                intermediate_stops.append(intermediate_stops_item)

        _steps = d.pop("steps", UNSET)
        steps: list[StepInstruction] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = StepInstruction.from_dict(steps_item_data)

                steps.append(steps_item)

        _rental = d.pop("rental", UNSET)
        rental: Rental | Unset
        if isinstance(_rental, Unset):
            rental = UNSET
        else:
            rental = Rental.from_dict(_rental)

        fare_transfer_index = d.pop("fareTransferIndex", UNSET)

        effective_fare_leg_index = d.pop("effectiveFareLegIndex", UNSET)

        _alerts = d.pop("alerts", UNSET)
        alerts: list[Alert] | Unset = UNSET
        if _alerts is not UNSET:
            alerts = []
            for alerts_item_data in _alerts:
                alerts_item = Alert.from_dict(alerts_item_data)

                alerts.append(alerts_item)

        _looped_calendar_since = d.pop("loopedCalendarSince", UNSET)
        looped_calendar_since: datetime.datetime | Unset
        if isinstance(_looped_calendar_since, Unset):
            looped_calendar_since = UNSET
        else:
            looped_calendar_since = datetime.datetime.fromisoformat(_looped_calendar_since)

        bikes_allowed = d.pop("bikesAllowed", UNSET)

        _wheelchair_accessible = d.pop("wheelchairAccessible", UNSET)
        wheelchair_accessible: WheelchairAccessibility | Unset
        if isinstance(_wheelchair_accessible, Unset):
            wheelchair_accessible = UNSET
        else:
            wheelchair_accessible = WheelchairAccessibility(_wheelchair_accessible)

        _alternatives = d.pop("alternatives", UNSET)
        alternatives: list[list[Leg]] | Unset = UNSET
        if _alternatives is not UNSET:
            alternatives = []
            for alternatives_item_data in _alternatives:
                alternatives_item = []
                _alternatives_item = alternatives_item_data
                for alternatives_item_item_data in _alternatives_item:
                    alternatives_item_item = Leg.from_dict(alternatives_item_item_data)

                    alternatives_item.append(alternatives_item_item)

                alternatives.append(alternatives_item)

        leg = cls(
            mode=mode,
            from_=from_,
            to=to,
            duration=duration,
            start_time=start_time,
            end_time=end_time,
            scheduled_start_time=scheduled_start_time,
            scheduled_end_time=scheduled_end_time,
            real_time=real_time,
            scheduled=scheduled,
            leg_geometry=leg_geometry,
            distance=distance,
            interline_with_previous_leg=interline_with_previous_leg,
            headsign=headsign,
            trip_from=trip_from,
            trip_to=trip_to,
            category=category,
            route_id=route_id,
            route_url=route_url,
            direction_id=direction_id,
            route_color=route_color,
            route_text_color=route_text_color,
            route_type=route_type,
            agency_name=agency_name,
            agency_url=agency_url,
            agency_id=agency_id,
            trip_id=trip_id,
            route_short_name=route_short_name,
            route_long_name=route_long_name,
            trip_short_name=trip_short_name,
            display_name=display_name,
            cancelled=cancelled,
            source=source,
            intermediate_stops=intermediate_stops,
            steps=steps,
            rental=rental,
            fare_transfer_index=fare_transfer_index,
            effective_fare_leg_index=effective_fare_leg_index,
            alerts=alerts,
            looped_calendar_since=looped_calendar_since,
            bikes_allowed=bikes_allowed,
            wheelchair_accessible=wheelchair_accessible,
            alternatives=alternatives,
        )

        leg.additional_properties = d
        return leg

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
