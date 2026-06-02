from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.leg_id import LegId


T = TypeVar("T", bound="ItineraryId")


@_attrs_define
class ItineraryId:
    """
    Attributes:
        legs (list[LegId]):
    """

    legs: list[LegId]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legs = []
        for legs_item_data in self.legs:
            legs_item = legs_item_data.to_dict()
            legs.append(legs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "legs": legs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leg_id import LegId

        d = dict(src_dict)
        legs = []
        _legs = d.pop("legs")
        for legs_item_data in _legs:
            legs_item = LegId.from_dict(legs_item_data)

            legs.append(legs_item)

        itinerary_id = cls(
            legs=legs,
        )

        itinerary_id.additional_properties = d
        return itinerary_id

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
