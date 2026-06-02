from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Area")


@_attrs_define
class Area:
    """Administrative area

    Attributes:
        name (str): Name of the area
        admin_level (float): [OpenStreetMap `admin_level`](https://wiki.openstreetmap.org/wiki/Key:admin_level)
            of the area
        matched (bool): Whether this area was matched by the input text
        unique (bool | Unset): Set for the first area after the `default` area that distinguishes areas
            if the match is ambiguous regarding (`default` area + place name / street [+ house number]).
        default (bool | Unset): Whether this area should be displayed as default area (area with admin level closest 7)
    """

    name: str
    admin_level: float
    matched: bool
    unique: bool | Unset = UNSET
    default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        admin_level = self.admin_level

        matched = self.matched

        unique = self.unique

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "adminLevel": admin_level,
                "matched": matched,
            }
        )
        if unique is not UNSET:
            field_dict["unique"] = unique
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        admin_level = d.pop("adminLevel")

        matched = d.pop("matched")

        unique = d.pop("unique", UNSET)

        default = d.pop("default", UNSET)

        area = cls(
            name=name,
            admin_level=admin_level,
            matched=matched,
            unique=unique,
            default=default,
        )

        area.additional_properties = d
        return area

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
