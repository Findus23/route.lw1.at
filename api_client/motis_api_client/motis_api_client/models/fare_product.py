from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fare_media import FareMedia
    from ..models.rider_category import RiderCategory


T = TypeVar("T", bound="FareProduct")


@_attrs_define
class FareProduct:
    """
    Attributes:
        name (str): The name of the fare product as displayed to riders.
        amount (float): The cost of the fare product. May be negative to represent transfer discounts. May be zero to
            represent a fare product that is free.
        currency (str): ISO 4217 currency code. The currency of the cost of the fare product.
        rider_category (RiderCategory | Unset):
        media (FareMedia | Unset):
    """

    name: str
    amount: float
    currency: str
    rider_category: RiderCategory | Unset = UNSET
    media: FareMedia | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        amount = self.amount

        currency = self.currency

        rider_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rider_category, Unset):
            rider_category = self.rider_category.to_dict()

        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "amount": amount,
                "currency": currency,
            }
        )
        if rider_category is not UNSET:
            field_dict["riderCategory"] = rider_category
        if media is not UNSET:
            field_dict["media"] = media

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fare_media import FareMedia
        from ..models.rider_category import RiderCategory

        d = dict(src_dict)
        name = d.pop("name")

        amount = d.pop("amount")

        currency = d.pop("currency")

        _rider_category = d.pop("riderCategory", UNSET)
        rider_category: RiderCategory | Unset
        if isinstance(_rider_category, Unset):
            rider_category = UNSET
        else:
            rider_category = RiderCategory.from_dict(_rider_category)

        _media = d.pop("media", UNSET)
        media: FareMedia | Unset
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = FareMedia.from_dict(_media)

        fare_product = cls(
            name=name,
            amount=amount,
            currency=currency,
            rider_category=rider_category,
            media=media,
        )

        fare_product.additional_properties = d
        return fare_product

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
