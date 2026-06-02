from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rental_form_factor import RentalFormFactor
from ..models.rental_propulsion_type import RentalPropulsionType
from ..models.rental_return_constraint import RentalReturnConstraint
from ..types import UNSET, Unset

T = TypeVar("T", bound="RentalVehicleType")


@_attrs_define
class RentalVehicleType:
    """
    Attributes:
        id (str): Unique identifier of the vehicle type (unique within the provider)
        form_factor (RentalFormFactor):
        propulsion_type (RentalPropulsionType):
        return_constraint (RentalReturnConstraint):
        return_constraint_guessed (bool): Whether the return constraint was guessed instead of being specified by the
            rental provider
        name (str | Unset): Public name of the vehicle type (can be empty)
    """

    id: str
    form_factor: RentalFormFactor
    propulsion_type: RentalPropulsionType
    return_constraint: RentalReturnConstraint
    return_constraint_guessed: bool
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        form_factor = self.form_factor.value

        propulsion_type = self.propulsion_type.value

        return_constraint = self.return_constraint.value

        return_constraint_guessed = self.return_constraint_guessed

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "formFactor": form_factor,
                "propulsionType": propulsion_type,
                "returnConstraint": return_constraint,
                "returnConstraintGuessed": return_constraint_guessed,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        form_factor = RentalFormFactor(d.pop("formFactor"))

        propulsion_type = RentalPropulsionType(d.pop("propulsionType"))

        return_constraint = RentalReturnConstraint(d.pop("returnConstraint"))

        return_constraint_guessed = d.pop("returnConstraintGuessed")

        name = d.pop("name", UNSET)

        rental_vehicle_type = cls(
            id=id,
            form_factor=form_factor,
            propulsion_type=propulsion_type,
            return_constraint=return_constraint,
            return_constraint_guessed=return_constraint_guessed,
            name=name,
        )

        rental_vehicle_type.additional_properties = d
        return rental_vehicle_type

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
