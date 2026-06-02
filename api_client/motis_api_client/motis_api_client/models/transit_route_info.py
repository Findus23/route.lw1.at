from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransitRouteInfo")


@_attrs_define
class TransitRouteInfo:
    """
    Attributes:
        id (str):
        short_name (str):
        long_name (str):
        color (str | Unset):
        text_color (str | Unset):
    """

    id: str
    short_name: str
    long_name: str
    color: str | Unset = UNSET
    text_color: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        short_name = self.short_name

        long_name = self.long_name

        color = self.color

        text_color = self.text_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "shortName": short_name,
                "longName": long_name,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if text_color is not UNSET:
            field_dict["textColor"] = text_color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        short_name = d.pop("shortName")

        long_name = d.pop("longName")

        color = d.pop("color", UNSET)

        text_color = d.pop("textColor", UNSET)

        transit_route_info = cls(
            id=id,
            short_name=short_name,
            long_name=long_name,
            color=color,
            text_color=text_color,
        )

        transit_route_info.additional_properties = d
        return transit_route_info

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
