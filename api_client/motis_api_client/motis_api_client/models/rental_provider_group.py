from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rental_form_factor import RentalFormFactor
from ..types import UNSET, Unset

T = TypeVar("T", bound="RentalProviderGroup")


@_attrs_define
class RentalProviderGroup:
    """
    Attributes:
        id (str): Unique identifier of the rental provider group
        name (str): Name of the provider group to be displayed to customers
        providers (list[str]): List of rental provider IDs that belong to this group
        form_factors (list[RentalFormFactor]): List of form factors offered by this provider group
        color (str | Unset): Color associated with this provider group, in hexadecimal RGB format
            (e.g. "#FF0000" for red). Can be empty.
    """

    id: str
    name: str
    providers: list[str]
    form_factors: list[RentalFormFactor]
    color: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        providers = self.providers

        form_factors = []
        for form_factors_item_data in self.form_factors:
            form_factors_item = form_factors_item_data.value
            form_factors.append(form_factors_item)

        color = self.color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "providers": providers,
                "formFactors": form_factors,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        providers = cast(list[str], d.pop("providers"))

        form_factors = []
        _form_factors = d.pop("formFactors")
        for form_factors_item_data in _form_factors:
            form_factors_item = RentalFormFactor(form_factors_item_data)

            form_factors.append(form_factors_item)

        color = d.pop("color", UNSET)

        rental_provider_group = cls(
            id=id,
            name=name,
            providers=providers,
            form_factors=form_factors,
            color=color,
        )

        rental_provider_group.additional_properties = d
        return rental_provider_group

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
