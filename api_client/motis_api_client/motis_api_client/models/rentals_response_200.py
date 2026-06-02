from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.rental_provider import RentalProvider
    from ..models.rental_provider_group import RentalProviderGroup
    from ..models.rental_station import RentalStation
    from ..models.rental_vehicle import RentalVehicle
    from ..models.rental_zone import RentalZone


T = TypeVar("T", bound="RentalsResponse200")


@_attrs_define
class RentalsResponse200:
    """
    Attributes:
        provider_groups (list[RentalProviderGroup]):
        providers (list[RentalProvider]):
        stations (list[RentalStation]):
        vehicles (list[RentalVehicle]):
        zones (list[RentalZone]):
    """

    provider_groups: list[RentalProviderGroup]
    providers: list[RentalProvider]
    stations: list[RentalStation]
    vehicles: list[RentalVehicle]
    zones: list[RentalZone]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_groups = []
        for provider_groups_item_data in self.provider_groups:
            provider_groups_item = provider_groups_item_data.to_dict()
            provider_groups.append(provider_groups_item)

        providers = []
        for providers_item_data in self.providers:
            providers_item = providers_item_data.to_dict()
            providers.append(providers_item)

        stations = []
        for stations_item_data in self.stations:
            stations_item = stations_item_data.to_dict()
            stations.append(stations_item)

        vehicles = []
        for vehicles_item_data in self.vehicles:
            vehicles_item = vehicles_item_data.to_dict()
            vehicles.append(vehicles_item)

        zones = []
        for zones_item_data in self.zones:
            zones_item = zones_item_data.to_dict()
            zones.append(zones_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerGroups": provider_groups,
                "providers": providers,
                "stations": stations,
                "vehicles": vehicles,
                "zones": zones,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rental_provider import RentalProvider
        from ..models.rental_provider_group import RentalProviderGroup
        from ..models.rental_station import RentalStation
        from ..models.rental_vehicle import RentalVehicle
        from ..models.rental_zone import RentalZone

        d = dict(src_dict)
        provider_groups = []
        _provider_groups = d.pop("providerGroups")
        for provider_groups_item_data in _provider_groups:
            provider_groups_item = RentalProviderGroup.from_dict(provider_groups_item_data)

            provider_groups.append(provider_groups_item)

        providers = []
        _providers = d.pop("providers")
        for providers_item_data in _providers:
            providers_item = RentalProvider.from_dict(providers_item_data)

            providers.append(providers_item)

        stations = []
        _stations = d.pop("stations")
        for stations_item_data in _stations:
            stations_item = RentalStation.from_dict(stations_item_data)

            stations.append(stations_item)

        vehicles = []
        _vehicles = d.pop("vehicles")
        for vehicles_item_data in _vehicles:
            vehicles_item = RentalVehicle.from_dict(vehicles_item_data)

            vehicles.append(vehicles_item)

        zones = []
        _zones = d.pop("zones")
        for zones_item_data in _zones:
            zones_item = RentalZone.from_dict(zones_item_data)

            zones.append(zones_item)

        rentals_response_200 = cls(
            provider_groups=provider_groups,
            providers=providers,
            stations=stations,
            vehicles=vehicles,
            zones=zones,
        )

        rentals_response_200.additional_properties = d
        return rentals_response_200

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
