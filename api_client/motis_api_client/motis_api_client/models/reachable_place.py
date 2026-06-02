from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place import Place


T = TypeVar("T", bound="ReachablePlace")


@_attrs_define
class ReachablePlace:
    """Place reachable by One-to-All

    Attributes:
        place (Place | Unset):
        duration (int | Unset): Total travel duration
        k (int | Unset): k is the smallest number, for which a journey with the shortest duration and at most k-1
            transfers exist.
            You can think of k as the number of connections used.

            In more detail:

            k=0: No connection, e.g. for the one location
            k=1: Direct connection
            k=2: Connection with 1 transfer
    """

    place: Place | Unset = UNSET
    duration: int | Unset = UNSET
    k: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        place: dict[str, Any] | Unset = UNSET
        if not isinstance(self.place, Unset):
            place = self.place.to_dict()

        duration = self.duration

        k = self.k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if place is not UNSET:
            field_dict["place"] = place
        if duration is not UNSET:
            field_dict["duration"] = duration
        if k is not UNSET:
            field_dict["k"] = k

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place import Place

        d = dict(src_dict)
        _place = d.pop("place", UNSET)
        place: Place | Unset
        if isinstance(_place, Unset):
            place = UNSET
        else:
            place = Place.from_dict(_place)

        duration = d.pop("duration", UNSET)

        k = d.pop("k", UNSET)

        reachable_place = cls(
            place=place,
            duration=duration,
            k=k,
        )

        reachable_place.additional_properties = d
        return reachable_place

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
