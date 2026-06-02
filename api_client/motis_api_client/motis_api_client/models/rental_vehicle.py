from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rental_form_factor import RentalFormFactor
from ..models.rental_propulsion_type import RentalPropulsionType
from ..models.rental_return_constraint import RentalReturnConstraint
from ..types import UNSET, Unset

T = TypeVar("T", bound="RentalVehicle")


@_attrs_define
class RentalVehicle:
    """
    Attributes:
        id (str): Unique identifier of the rental vehicle
        provider_id (str): Unique identifier of the rental provider
        provider_group_id (str): Unique identifier of the rental provider group
        type_id (str): Vehicle type ID (unique within the provider)
        lat (float): latitude
        lon (float): longitude
        form_factor (RentalFormFactor):
        propulsion_type (RentalPropulsionType):
        return_constraint (RentalReturnConstraint):
        is_reserved (bool): true if the vehicle is currently reserved by a customer, false otherwise
        is_disabled (bool): true if the vehicle is out of service, false otherwise
        station_id (str | Unset): Station ID if the vehicle is currently at a station
        home_station_id (str | Unset): Station ID where the vehicle must be returned, if applicable
        rental_uri_android (str | Unset): Rental URI for Android (deep link to the specific vehicle)
        rental_uri_ios (str | Unset): Rental URI for iOS (deep link to the specific vehicle)
        rental_uri_web (str | Unset): Rental URI for web (deep link to the specific vehicle)
    """

    id: str
    provider_id: str
    provider_group_id: str
    type_id: str
    lat: float
    lon: float
    form_factor: RentalFormFactor
    propulsion_type: RentalPropulsionType
    return_constraint: RentalReturnConstraint
    is_reserved: bool
    is_disabled: bool
    station_id: str | Unset = UNSET
    home_station_id: str | Unset = UNSET
    rental_uri_android: str | Unset = UNSET
    rental_uri_ios: str | Unset = UNSET
    rental_uri_web: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        provider_id = self.provider_id

        provider_group_id = self.provider_group_id

        type_id = self.type_id

        lat = self.lat

        lon = self.lon

        form_factor = self.form_factor.value

        propulsion_type = self.propulsion_type.value

        return_constraint = self.return_constraint.value

        is_reserved = self.is_reserved

        is_disabled = self.is_disabled

        station_id = self.station_id

        home_station_id = self.home_station_id

        rental_uri_android = self.rental_uri_android

        rental_uri_ios = self.rental_uri_ios

        rental_uri_web = self.rental_uri_web

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "providerId": provider_id,
                "providerGroupId": provider_group_id,
                "typeId": type_id,
                "lat": lat,
                "lon": lon,
                "formFactor": form_factor,
                "propulsionType": propulsion_type,
                "returnConstraint": return_constraint,
                "isReserved": is_reserved,
                "isDisabled": is_disabled,
            }
        )
        if station_id is not UNSET:
            field_dict["stationId"] = station_id
        if home_station_id is not UNSET:
            field_dict["homeStationId"] = home_station_id
        if rental_uri_android is not UNSET:
            field_dict["rentalUriAndroid"] = rental_uri_android
        if rental_uri_ios is not UNSET:
            field_dict["rentalUriIOS"] = rental_uri_ios
        if rental_uri_web is not UNSET:
            field_dict["rentalUriWeb"] = rental_uri_web

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        provider_id = d.pop("providerId")

        provider_group_id = d.pop("providerGroupId")

        type_id = d.pop("typeId")

        lat = d.pop("lat")

        lon = d.pop("lon")

        form_factor = RentalFormFactor(d.pop("formFactor"))

        propulsion_type = RentalPropulsionType(d.pop("propulsionType"))

        return_constraint = RentalReturnConstraint(d.pop("returnConstraint"))

        is_reserved = d.pop("isReserved")

        is_disabled = d.pop("isDisabled")

        station_id = d.pop("stationId", UNSET)

        home_station_id = d.pop("homeStationId", UNSET)

        rental_uri_android = d.pop("rentalUriAndroid", UNSET)

        rental_uri_ios = d.pop("rentalUriIOS", UNSET)

        rental_uri_web = d.pop("rentalUriWeb", UNSET)

        rental_vehicle = cls(
            id=id,
            provider_id=provider_id,
            provider_group_id=provider_group_id,
            type_id=type_id,
            lat=lat,
            lon=lon,
            form_factor=form_factor,
            propulsion_type=propulsion_type,
            return_constraint=return_constraint,
            is_reserved=is_reserved,
            is_disabled=is_disabled,
            station_id=station_id,
            home_station_id=home_station_id,
            rental_uri_android=rental_uri_android,
            rental_uri_ios=rental_uri_ios,
            rental_uri_web=rental_uri_web,
        )

        rental_vehicle.additional_properties = d
        return rental_vehicle

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
