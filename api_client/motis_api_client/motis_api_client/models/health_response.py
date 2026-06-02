from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthResponse")


@_attrs_define
class HealthResponse:
    """
    Attributes:
        rt (bool | Unset): GTFSRT, SIRI Lite, VDV AUS, VDV454 feeds.
        gbfs (bool | Unset): GBFS feeds.
    """

    rt: bool | Unset = UNSET
    gbfs: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rt = self.rt

        gbfs = self.gbfs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rt is not UNSET:
            field_dict["rt"] = rt
        if gbfs is not UNSET:
            field_dict["gbfs"] = gbfs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rt = d.pop("rt", UNSET)

        gbfs = d.pop("gbfs", UNSET)

        health_response = cls(
            rt=rt,
            gbfs=gbfs,
        )

        health_response.additional_properties = d
        return health_response

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
