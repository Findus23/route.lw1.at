from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place import Place
    from ..models.reachable_place import ReachablePlace


T = TypeVar("T", bound="Reachable")


@_attrs_define
class Reachable:
    """Object containing all reachable places by One-to-All search

    Attributes:
        one (Place | Unset):
        all_ (list[ReachablePlace] | Unset): List of locations reachable by One-to-All
    """

    one: Place | Unset = UNSET
    all_: list[ReachablePlace] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        one: dict[str, Any] | Unset = UNSET
        if not isinstance(self.one, Unset):
            one = self.one.to_dict()

        all_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_, Unset):
            all_ = []
            for all_item_data in self.all_:
                all_item = all_item_data.to_dict()
                all_.append(all_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if one is not UNSET:
            field_dict["one"] = one
        if all_ is not UNSET:
            field_dict["all"] = all_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place import Place
        from ..models.reachable_place import ReachablePlace

        d = dict(src_dict)
        _one = d.pop("one", UNSET)
        one: Place | Unset
        if isinstance(_one, Unset):
            one = UNSET
        else:
            one = Place.from_dict(_one)

        _all_ = d.pop("all", UNSET)
        all_: list[ReachablePlace] | Unset = UNSET
        if _all_ is not UNSET:
            all_ = []
            for all_item_data in _all_:
                all_item = ReachablePlace.from_dict(all_item_data)

                all_.append(all_item)

        reachable = cls(
            one=one,
            all_=all_,
        )

        reachable.additional_properties = d
        return reachable

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
