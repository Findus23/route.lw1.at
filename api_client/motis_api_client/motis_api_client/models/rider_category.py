from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RiderCategory")


@_attrs_define
class RiderCategory:
    """
    Attributes:
        rider_category_name (str): Rider category name as displayed to the rider.
        is_default_fare_category (bool): Specifies if this category should be considered the default (i.e. the main
            category displayed to riders).
        eligibility_url (str | Unset): URL to a web page providing detailed information about the rider category and/or
            its eligibility criteria.
    """

    rider_category_name: str
    is_default_fare_category: bool
    eligibility_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rider_category_name = self.rider_category_name

        is_default_fare_category = self.is_default_fare_category

        eligibility_url = self.eligibility_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "riderCategoryName": rider_category_name,
                "isDefaultFareCategory": is_default_fare_category,
            }
        )
        if eligibility_url is not UNSET:
            field_dict["eligibilityUrl"] = eligibility_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rider_category_name = d.pop("riderCategoryName")

        is_default_fare_category = d.pop("isDefaultFareCategory")

        eligibility_url = d.pop("eligibilityUrl", UNSET)

        rider_category = cls(
            rider_category_name=rider_category_name,
            is_default_fare_category=is_default_fare_category,
            eligibility_url=eligibility_url,
        )

        rider_category.additional_properties = d
        return rider_category

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
