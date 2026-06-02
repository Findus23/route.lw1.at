from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rental_form_factor import RentalFormFactor
from ..models.rental_propulsion_type import RentalPropulsionType
from ..models.rental_return_constraint import RentalReturnConstraint
from ..types import UNSET, Unset

T = TypeVar("T", bound="Rental")


@_attrs_define
class Rental:
    """Vehicle rental

    Attributes:
        provider_id (str): Rental provider ID
        provider_group_id (str): Rental provider group ID
        system_id (str): Vehicle share system ID
        system_name (str | Unset): Vehicle share system name
        url (str | Unset): URL of the vehicle share system
        color (str | Unset): Color associated with this provider, in hexadecimal RGB format
            (e.g. "#FF0000" for red). Can be empty.
        station_name (str | Unset): Name of the station
        from_station_name (str | Unset): Name of the station where the vehicle is picked up (empty for free floating
            vehicles)
        to_station_name (str | Unset): Name of the station where the vehicle is returned (empty for free floating
            vehicles)
        rental_uri_android (str | Unset): Rental URI for Android (deep link to the specific station or vehicle)
        rental_uri_ios (str | Unset): Rental URI for iOS (deep link to the specific station or vehicle)
        rental_uri_web (str | Unset): Rental URI for web (deep link to the specific station or vehicle)
        form_factor (RentalFormFactor | Unset):
        propulsion_type (RentalPropulsionType | Unset):
        return_constraint (RentalReturnConstraint | Unset):
    """

    provider_id: str
    provider_group_id: str
    system_id: str
    system_name: str | Unset = UNSET
    url: str | Unset = UNSET
    color: str | Unset = UNSET
    station_name: str | Unset = UNSET
    from_station_name: str | Unset = UNSET
    to_station_name: str | Unset = UNSET
    rental_uri_android: str | Unset = UNSET
    rental_uri_ios: str | Unset = UNSET
    rental_uri_web: str | Unset = UNSET
    form_factor: RentalFormFactor | Unset = UNSET
    propulsion_type: RentalPropulsionType | Unset = UNSET
    return_constraint: RentalReturnConstraint | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        provider_group_id = self.provider_group_id

        system_id = self.system_id

        system_name = self.system_name

        url = self.url

        color = self.color

        station_name = self.station_name

        from_station_name = self.from_station_name

        to_station_name = self.to_station_name

        rental_uri_android = self.rental_uri_android

        rental_uri_ios = self.rental_uri_ios

        rental_uri_web = self.rental_uri_web

        form_factor: str | Unset = UNSET
        if not isinstance(self.form_factor, Unset):
            form_factor = self.form_factor.value

        propulsion_type: str | Unset = UNSET
        if not isinstance(self.propulsion_type, Unset):
            propulsion_type = self.propulsion_type.value

        return_constraint: str | Unset = UNSET
        if not isinstance(self.return_constraint, Unset):
            return_constraint = self.return_constraint.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerId": provider_id,
                "providerGroupId": provider_group_id,
                "systemId": system_id,
            }
        )
        if system_name is not UNSET:
            field_dict["systemName"] = system_name
        if url is not UNSET:
            field_dict["url"] = url
        if color is not UNSET:
            field_dict["color"] = color
        if station_name is not UNSET:
            field_dict["stationName"] = station_name
        if from_station_name is not UNSET:
            field_dict["fromStationName"] = from_station_name
        if to_station_name is not UNSET:
            field_dict["toStationName"] = to_station_name
        if rental_uri_android is not UNSET:
            field_dict["rentalUriAndroid"] = rental_uri_android
        if rental_uri_ios is not UNSET:
            field_dict["rentalUriIOS"] = rental_uri_ios
        if rental_uri_web is not UNSET:
            field_dict["rentalUriWeb"] = rental_uri_web
        if form_factor is not UNSET:
            field_dict["formFactor"] = form_factor
        if propulsion_type is not UNSET:
            field_dict["propulsionType"] = propulsion_type
        if return_constraint is not UNSET:
            field_dict["returnConstraint"] = return_constraint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_id = d.pop("providerId")

        provider_group_id = d.pop("providerGroupId")

        system_id = d.pop("systemId")

        system_name = d.pop("systemName", UNSET)

        url = d.pop("url", UNSET)

        color = d.pop("color", UNSET)

        station_name = d.pop("stationName", UNSET)

        from_station_name = d.pop("fromStationName", UNSET)

        to_station_name = d.pop("toStationName", UNSET)

        rental_uri_android = d.pop("rentalUriAndroid", UNSET)

        rental_uri_ios = d.pop("rentalUriIOS", UNSET)

        rental_uri_web = d.pop("rentalUriWeb", UNSET)

        _form_factor = d.pop("formFactor", UNSET)
        form_factor: RentalFormFactor | Unset
        if isinstance(_form_factor, Unset):
            form_factor = UNSET
        else:
            form_factor = RentalFormFactor(_form_factor)

        _propulsion_type = d.pop("propulsionType", UNSET)
        propulsion_type: RentalPropulsionType | Unset
        if isinstance(_propulsion_type, Unset):
            propulsion_type = UNSET
        else:
            propulsion_type = RentalPropulsionType(_propulsion_type)

        _return_constraint = d.pop("returnConstraint", UNSET)
        return_constraint: RentalReturnConstraint | Unset
        if isinstance(_return_constraint, Unset):
            return_constraint = UNSET
        else:
            return_constraint = RentalReturnConstraint(_return_constraint)

        rental = cls(
            provider_id=provider_id,
            provider_group_id=provider_group_id,
            system_id=system_id,
            system_name=system_name,
            url=url,
            color=color,
            station_name=station_name,
            from_station_name=from_station_name,
            to_station_name=to_station_name,
            rental_uri_android=rental_uri_android,
            rental_uri_ios=rental_uri_ios,
            rental_uri_web=rental_uri_web,
            form_factor=form_factor,
            propulsion_type=propulsion_type,
            return_constraint=return_constraint,
        )

        rental.additional_properties = d
        return rental

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
