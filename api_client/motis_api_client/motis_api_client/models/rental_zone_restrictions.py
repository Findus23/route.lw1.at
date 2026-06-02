from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RentalZoneRestrictions")


@_attrs_define
class RentalZoneRestrictions:
    """
    Attributes:
        vehicle_type_idxs (list[int]): List of vehicle types (as indices into the provider's vehicle types
            array) to which these restrictions apply.
            If empty, the restrictions apply to all vehicle types of the provider.
        ride_start_allowed (bool): whether the ride is allowed to start in this zone
        ride_end_allowed (bool): whether the ride is allowed to end in this zone
        ride_through_allowed (bool): whether the ride is allowed to pass through this zone
        station_parking (bool | Unset): whether vehicles can only be parked at stations in this zone
    """

    vehicle_type_idxs: list[int]
    ride_start_allowed: bool
    ride_end_allowed: bool
    ride_through_allowed: bool
    station_parking: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vehicle_type_idxs = self.vehicle_type_idxs

        ride_start_allowed = self.ride_start_allowed

        ride_end_allowed = self.ride_end_allowed

        ride_through_allowed = self.ride_through_allowed

        station_parking = self.station_parking

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vehicleTypeIdxs": vehicle_type_idxs,
                "rideStartAllowed": ride_start_allowed,
                "rideEndAllowed": ride_end_allowed,
                "rideThroughAllowed": ride_through_allowed,
            }
        )
        if station_parking is not UNSET:
            field_dict["stationParking"] = station_parking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vehicle_type_idxs = cast(list[int], d.pop("vehicleTypeIdxs"))

        ride_start_allowed = d.pop("rideStartAllowed")

        ride_end_allowed = d.pop("rideEndAllowed")

        ride_through_allowed = d.pop("rideThroughAllowed")

        station_parking = d.pop("stationParking", UNSET)

        rental_zone_restrictions = cls(
            vehicle_type_idxs=vehicle_type_idxs,
            ride_start_allowed=ride_start_allowed,
            ride_end_allowed=ride_end_allowed,
            ride_through_allowed=ride_through_allowed,
            station_parking=station_parking,
        )

        rental_zone_restrictions.additional_properties = d
        return rental_zone_restrictions

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
