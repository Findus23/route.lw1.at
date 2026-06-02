from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fare_transfer_rule import FareTransferRule
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fare_product import FareProduct


T = TypeVar("T", bound="FareTransfer")


@_attrs_define
class FareTransfer:
    """The concept is derived from: https://gtfs.org/documentation/schedule/reference/#fare_transfer_rulestxt

    Terminology:
      - **Leg**: An itinerary leg as described by the `Leg` type of this API description.
      - **Effective Fare Leg**: Itinerary legs can be joined together to form one *effective fare leg*.
      - **Fare Transfer**: A fare transfer groups two or more effective fare legs.
      - **A** is the first *effective fare leg* of potentially multiple consecutive legs contained in a fare transfer
      - **B** is any *effective fare leg* following the first *effective fare leg* in this transfer
      - **AB** are all changes between *effective fare legs* contained in this transfer

    The fare transfer rule is used to derive the final set of products of the itinerary legs contained in this transfer:
      - A_AB means that any product from the first effective fare leg combined with the product attached to the transfer
    itself (AB) which can be empty (= free). Note that all subsequent effective fare leg products need to be ignored in
    this case.
      - A_AB_B mean that a product for each effective fare leg needs to be purchased in a addition to the product
    attached to the transfer itself (AB) which can be empty (= free)
      - AB only the transfer product itself has to be purchased. Note that all fare products attached to the contained
    effective fare legs need to be ignored in this case.

    An itinerary `Leg` references the index of the fare transfer and the index of the effective fare leg in this
    transfer it belongs to.

        Attributes:
            effective_fare_leg_products (list[list[list[FareProduct]]]): Lists all valid fare products for the effective
                fare legs.
                This is an `array<array<FareProduct>>` where the inner array
                lists all possible fare products that would cover this effective fare leg.
                Each "effective fare leg" can have multiple options for adult/child/weekly/monthly/day/one-way tickets etc.
                You can see the outer array as AND (you need one ticket for each effective fare leg (`A_AB_B`), the first
                effective fare leg (`A_AB`) or no fare leg at all but only the transfer product (`AB`)
                and the inner array as OR (you can choose which ticket to buy)
            rule (FareTransferRule | Unset):
            transfer_products (list[FareProduct] | Unset):
    """

    effective_fare_leg_products: list[list[list[FareProduct]]]
    rule: FareTransferRule | Unset = UNSET
    transfer_products: list[FareProduct] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_fare_leg_products = []
        for effective_fare_leg_products_item_data in self.effective_fare_leg_products:
            effective_fare_leg_products_item = []
            for effective_fare_leg_products_item_item_data in effective_fare_leg_products_item_data:
                effective_fare_leg_products_item_item = []
                for effective_fare_leg_products_item_item_item_data in effective_fare_leg_products_item_item_data:
                    effective_fare_leg_products_item_item_item = (
                        effective_fare_leg_products_item_item_item_data.to_dict()
                    )
                    effective_fare_leg_products_item_item.append(effective_fare_leg_products_item_item_item)

                effective_fare_leg_products_item.append(effective_fare_leg_products_item_item)

            effective_fare_leg_products.append(effective_fare_leg_products_item)

        rule: str | Unset = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.value

        transfer_products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transfer_products, Unset):
            transfer_products = []
            for transfer_products_item_data in self.transfer_products:
                transfer_products_item = transfer_products_item_data.to_dict()
                transfer_products.append(transfer_products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "effectiveFareLegProducts": effective_fare_leg_products,
            }
        )
        if rule is not UNSET:
            field_dict["rule"] = rule
        if transfer_products is not UNSET:
            field_dict["transferProducts"] = transfer_products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fare_product import FareProduct

        d = dict(src_dict)
        effective_fare_leg_products = []
        _effective_fare_leg_products = d.pop("effectiveFareLegProducts")
        for effective_fare_leg_products_item_data in _effective_fare_leg_products:
            effective_fare_leg_products_item = []
            _effective_fare_leg_products_item = effective_fare_leg_products_item_data
            for effective_fare_leg_products_item_item_data in _effective_fare_leg_products_item:
                effective_fare_leg_products_item_item = []
                _effective_fare_leg_products_item_item = effective_fare_leg_products_item_item_data
                for effective_fare_leg_products_item_item_item_data in _effective_fare_leg_products_item_item:
                    effective_fare_leg_products_item_item_item = FareProduct.from_dict(
                        effective_fare_leg_products_item_item_item_data
                    )

                    effective_fare_leg_products_item_item.append(effective_fare_leg_products_item_item_item)

                effective_fare_leg_products_item.append(effective_fare_leg_products_item_item)

            effective_fare_leg_products.append(effective_fare_leg_products_item)

        _rule = d.pop("rule", UNSET)
        rule: FareTransferRule | Unset
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = FareTransferRule(_rule)

        _transfer_products = d.pop("transferProducts", UNSET)
        transfer_products: list[FareProduct] | Unset = UNSET
        if _transfer_products is not UNSET:
            transfer_products = []
            for transfer_products_item_data in _transfer_products:
                transfer_products_item = FareProduct.from_dict(transfer_products_item_data)

                transfer_products.append(transfer_products_item)

        fare_transfer = cls(
            effective_fare_leg_products=effective_fare_leg_products,
            rule=rule,
            transfer_products=transfer_products,
        )

        fare_transfer.additional_properties = d
        return fare_transfer

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
