from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mode import Mode
from ..models.pedestrian_profile import PedestrianProfile
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.itinerary_id import ItineraryId


T = TypeVar("T", bound="RefreshItineraryPostBody")


@_attrs_define
class RefreshItineraryPostBody:
    """Body for the `refreshItineraryPost` endpoint. All fields mirror the
    parameters of the `plan` endpoint - see the `plan` endpoint for their
    descriptions.

        Attributes:
            id (ItineraryId):
            require_display_name_match (bool | Unset):  Default: True.
            join_interlined_legs (bool | Unset):  Default: True.
            detailed_transfers (bool | Unset):
            detailed_legs (bool | Unset):  Default: True.
            with_fares (bool | Unset):  Default: False.
            with_scheduled_skipped_stops (bool | Unset):  Default: False.
            num_leg_alternatives (int | Unset):  Default: 0.
            transit_modes (list[Mode] | Unset):
            pedestrian_profile (PedestrianProfile | Unset): Different accessibility profiles for pedestrians.
            use_routed_transfers (bool | Unset):  Default: False.
            require_bike_transport (bool | Unset):  Default: False.
            require_car_transport (bool | Unset):  Default: False.
            language (list[str] | Unset):
    """

    id: ItineraryId
    require_display_name_match: bool | Unset = True
    join_interlined_legs: bool | Unset = True
    detailed_transfers: bool | Unset = UNSET
    detailed_legs: bool | Unset = True
    with_fares: bool | Unset = False
    with_scheduled_skipped_stops: bool | Unset = False
    num_leg_alternatives: int | Unset = 0
    transit_modes: list[Mode] | Unset = UNSET
    pedestrian_profile: PedestrianProfile | Unset = UNSET
    use_routed_transfers: bool | Unset = False
    require_bike_transport: bool | Unset = False
    require_car_transport: bool | Unset = False
    language: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.to_dict()

        require_display_name_match = self.require_display_name_match

        join_interlined_legs = self.join_interlined_legs

        detailed_transfers = self.detailed_transfers

        detailed_legs = self.detailed_legs

        with_fares = self.with_fares

        with_scheduled_skipped_stops = self.with_scheduled_skipped_stops

        num_leg_alternatives = self.num_leg_alternatives

        transit_modes: list[str] | Unset = UNSET
        if not isinstance(self.transit_modes, Unset):
            transit_modes = []
            for transit_modes_item_data in self.transit_modes:
                transit_modes_item = transit_modes_item_data.value
                transit_modes.append(transit_modes_item)

        pedestrian_profile: str | Unset = UNSET
        if not isinstance(self.pedestrian_profile, Unset):
            pedestrian_profile = self.pedestrian_profile.value

        use_routed_transfers = self.use_routed_transfers

        require_bike_transport = self.require_bike_transport

        require_car_transport = self.require_car_transport

        language: list[str] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if require_display_name_match is not UNSET:
            field_dict["requireDisplayNameMatch"] = require_display_name_match
        if join_interlined_legs is not UNSET:
            field_dict["joinInterlinedLegs"] = join_interlined_legs
        if detailed_transfers is not UNSET:
            field_dict["detailedTransfers"] = detailed_transfers
        if detailed_legs is not UNSET:
            field_dict["detailedLegs"] = detailed_legs
        if with_fares is not UNSET:
            field_dict["withFares"] = with_fares
        if with_scheduled_skipped_stops is not UNSET:
            field_dict["withScheduledSkippedStops"] = with_scheduled_skipped_stops
        if num_leg_alternatives is not UNSET:
            field_dict["numLegAlternatives"] = num_leg_alternatives
        if transit_modes is not UNSET:
            field_dict["transitModes"] = transit_modes
        if pedestrian_profile is not UNSET:
            field_dict["pedestrianProfile"] = pedestrian_profile
        if use_routed_transfers is not UNSET:
            field_dict["useRoutedTransfers"] = use_routed_transfers
        if require_bike_transport is not UNSET:
            field_dict["requireBikeTransport"] = require_bike_transport
        if require_car_transport is not UNSET:
            field_dict["requireCarTransport"] = require_car_transport
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.itinerary_id import ItineraryId

        d = dict(src_dict)
        id = ItineraryId.from_dict(d.pop("id"))

        require_display_name_match = d.pop("requireDisplayNameMatch", UNSET)

        join_interlined_legs = d.pop("joinInterlinedLegs", UNSET)

        detailed_transfers = d.pop("detailedTransfers", UNSET)

        detailed_legs = d.pop("detailedLegs", UNSET)

        with_fares = d.pop("withFares", UNSET)

        with_scheduled_skipped_stops = d.pop("withScheduledSkippedStops", UNSET)

        num_leg_alternatives = d.pop("numLegAlternatives", UNSET)

        _transit_modes = d.pop("transitModes", UNSET)
        transit_modes: list[Mode] | Unset = UNSET
        if _transit_modes is not UNSET:
            transit_modes = []
            for transit_modes_item_data in _transit_modes:
                transit_modes_item = Mode(transit_modes_item_data)

                transit_modes.append(transit_modes_item)

        _pedestrian_profile = d.pop("pedestrianProfile", UNSET)
        pedestrian_profile: PedestrianProfile | Unset
        if isinstance(_pedestrian_profile, Unset):
            pedestrian_profile = UNSET
        else:
            pedestrian_profile = PedestrianProfile(_pedestrian_profile)

        use_routed_transfers = d.pop("useRoutedTransfers", UNSET)

        require_bike_transport = d.pop("requireBikeTransport", UNSET)

        require_car_transport = d.pop("requireCarTransport", UNSET)

        language = cast(list[str], d.pop("language", UNSET))

        refresh_itinerary_post_body = cls(
            id=id,
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

        refresh_itinerary_post_body.additional_properties = d
        return refresh_itinerary_post_body

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
