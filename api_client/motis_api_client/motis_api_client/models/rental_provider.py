from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rental_form_factor import RentalFormFactor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rental_vehicle_type import RentalVehicleType
    from ..models.rental_zone_restrictions import RentalZoneRestrictions


T = TypeVar("T", bound="RentalProvider")


@_attrs_define
class RentalProvider:
    """
    Attributes:
        id (str): Unique identifier of the rental provider
        name (str): Name of the provider to be displayed to customers
        group_id (str): Id of the rental provider group this provider belongs to
        bbox (list[float]): Bounding box of the area covered by this rental provider,
            [west, south, east, north] as [lon, lat, lon, lat]
        vehicle_types (list[RentalVehicleType]):
        form_factors (list[RentalFormFactor]): List of form factors offered by this provider
        default_restrictions (RentalZoneRestrictions):
        global_geofencing_rules (list[RentalZoneRestrictions]):
        operator (str | Unset): Name of the system operator
        url (str | Unset): URL of the vehicle share system
        purchase_url (str | Unset): URL where a customer can purchase a membership
        color (str | Unset): Color associated with this provider, in hexadecimal RGB format
            (e.g. "#FF0000" for red). Can be empty.
    """

    id: str
    name: str
    group_id: str
    bbox: list[float]
    vehicle_types: list[RentalVehicleType]
    form_factors: list[RentalFormFactor]
    default_restrictions: RentalZoneRestrictions
    global_geofencing_rules: list[RentalZoneRestrictions]
    operator: str | Unset = UNSET
    url: str | Unset = UNSET
    purchase_url: str | Unset = UNSET
    color: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        group_id = self.group_id

        bbox = self.bbox

        vehicle_types = []
        for vehicle_types_item_data in self.vehicle_types:
            vehicle_types_item = vehicle_types_item_data.to_dict()
            vehicle_types.append(vehicle_types_item)

        form_factors = []
        for form_factors_item_data in self.form_factors:
            form_factors_item = form_factors_item_data.value
            form_factors.append(form_factors_item)

        default_restrictions = self.default_restrictions.to_dict()

        global_geofencing_rules = []
        for global_geofencing_rules_item_data in self.global_geofencing_rules:
            global_geofencing_rules_item = global_geofencing_rules_item_data.to_dict()
            global_geofencing_rules.append(global_geofencing_rules_item)

        operator = self.operator

        url = self.url

        purchase_url = self.purchase_url

        color = self.color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "groupId": group_id,
                "bbox": bbox,
                "vehicleTypes": vehicle_types,
                "formFactors": form_factors,
                "defaultRestrictions": default_restrictions,
                "globalGeofencingRules": global_geofencing_rules,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator
        if url is not UNSET:
            field_dict["url"] = url
        if purchase_url is not UNSET:
            field_dict["purchaseUrl"] = purchase_url
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rental_vehicle_type import RentalVehicleType
        from ..models.rental_zone_restrictions import RentalZoneRestrictions

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        group_id = d.pop("groupId")

        bbox = cast(list[float], d.pop("bbox"))

        vehicle_types = []
        _vehicle_types = d.pop("vehicleTypes")
        for vehicle_types_item_data in _vehicle_types:
            vehicle_types_item = RentalVehicleType.from_dict(vehicle_types_item_data)

            vehicle_types.append(vehicle_types_item)

        form_factors = []
        _form_factors = d.pop("formFactors")
        for form_factors_item_data in _form_factors:
            form_factors_item = RentalFormFactor(form_factors_item_data)

            form_factors.append(form_factors_item)

        default_restrictions = RentalZoneRestrictions.from_dict(d.pop("defaultRestrictions"))

        global_geofencing_rules = []
        _global_geofencing_rules = d.pop("globalGeofencingRules")
        for global_geofencing_rules_item_data in _global_geofencing_rules:
            global_geofencing_rules_item = RentalZoneRestrictions.from_dict(global_geofencing_rules_item_data)

            global_geofencing_rules.append(global_geofencing_rules_item)

        operator = d.pop("operator", UNSET)

        url = d.pop("url", UNSET)

        purchase_url = d.pop("purchaseUrl", UNSET)

        color = d.pop("color", UNSET)

        rental_provider = cls(
            id=id,
            name=name,
            group_id=group_id,
            bbox=bbox,
            vehicle_types=vehicle_types,
            form_factors=form_factors,
            default_restrictions=default_restrictions,
            global_geofencing_rules=global_geofencing_rules,
            operator=operator,
            url=url,
            purchase_url=purchase_url,
            color=color,
        )

        rental_provider.additional_properties = d
        return rental_provider

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
