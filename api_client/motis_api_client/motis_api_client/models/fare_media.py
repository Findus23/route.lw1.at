from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fare_media_type import FareMediaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FareMedia")


@_attrs_define
class FareMedia:
    """
    Attributes:
        fare_media_type (FareMediaType): - `NONE`: No fare media involved (e.g., cash payment)
            - `PAPER_TICKET`: Physical paper ticket
            - `TRANSIT_CARD`: Physical transit card with stored value
            - `CONTACTLESS_EMV`: cEMV (contactless payment)
            - `MOBILE_APP`: Mobile app with virtual transit cards/passes
        fare_media_name (str | Unset): Name of the fare media. Required for transit cards and mobile apps.
    """

    fare_media_type: FareMediaType
    fare_media_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fare_media_type = self.fare_media_type.value

        fare_media_name = self.fare_media_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fareMediaType": fare_media_type,
            }
        )
        if fare_media_name is not UNSET:
            field_dict["fareMediaName"] = fare_media_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fare_media_type = FareMediaType(d.pop("fareMediaType"))

        fare_media_name = d.pop("fareMediaName", UNSET)

        fare_media = cls(
            fare_media_type=fare_media_type,
            fare_media_name=fare_media_name,
        )

        fare_media.additional_properties = d
        return fare_media

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
