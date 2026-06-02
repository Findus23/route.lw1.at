from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerConfig")


@_attrs_define
class ServerConfig:
    """
    Attributes:
        motis_version (str): the version of this MOTIS server
        has_elevation (bool): true if elevation is loaded
        has_routed_transfers (bool): true if routed transfers available
        has_street_routing (bool): true if street routing is available
        max_one_to_many_size (float): limit for the number of `many` locations for one-to-many requests
        max_one_to_all_travel_time_limit (float): limit for maxTravelTime API param in minutes
        max_pre_post_transit_time_limit (float): limit for maxPrePostTransitTime API param in seconds
        max_direct_time_limit (float): limit for maxDirectTime API param in seconds
        shapes_debug_enabled (bool): true if experimental route shapes debug download API is enabled
    """

    motis_version: str
    has_elevation: bool
    has_routed_transfers: bool
    has_street_routing: bool
    max_one_to_many_size: float
    max_one_to_all_travel_time_limit: float
    max_pre_post_transit_time_limit: float
    max_direct_time_limit: float
    shapes_debug_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        motis_version = self.motis_version

        has_elevation = self.has_elevation

        has_routed_transfers = self.has_routed_transfers

        has_street_routing = self.has_street_routing

        max_one_to_many_size = self.max_one_to_many_size

        max_one_to_all_travel_time_limit = self.max_one_to_all_travel_time_limit

        max_pre_post_transit_time_limit = self.max_pre_post_transit_time_limit

        max_direct_time_limit = self.max_direct_time_limit

        shapes_debug_enabled = self.shapes_debug_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "motisVersion": motis_version,
                "hasElevation": has_elevation,
                "hasRoutedTransfers": has_routed_transfers,
                "hasStreetRouting": has_street_routing,
                "maxOneToManySize": max_one_to_many_size,
                "maxOneToAllTravelTimeLimit": max_one_to_all_travel_time_limit,
                "maxPrePostTransitTimeLimit": max_pre_post_transit_time_limit,
                "maxDirectTimeLimit": max_direct_time_limit,
                "shapesDebugEnabled": shapes_debug_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        motis_version = d.pop("motisVersion")

        has_elevation = d.pop("hasElevation")

        has_routed_transfers = d.pop("hasRoutedTransfers")

        has_street_routing = d.pop("hasStreetRouting")

        max_one_to_many_size = d.pop("maxOneToManySize")

        max_one_to_all_travel_time_limit = d.pop("maxOneToAllTravelTimeLimit")

        max_pre_post_transit_time_limit = d.pop("maxPrePostTransitTimeLimit")

        max_direct_time_limit = d.pop("maxDirectTimeLimit")

        shapes_debug_enabled = d.pop("shapesDebugEnabled")

        server_config = cls(
            motis_version=motis_version,
            has_elevation=has_elevation,
            has_routed_transfers=has_routed_transfers,
            has_street_routing=has_street_routing,
            max_one_to_many_size=max_one_to_many_size,
            max_one_to_all_travel_time_limit=max_one_to_all_travel_time_limit,
            max_pre_post_transit_time_limit=max_pre_post_transit_time_limit,
            max_direct_time_limit=max_direct_time_limit,
            shapes_debug_enabled=shapes_debug_enabled,
        )

        server_config.additional_properties = d
        return server_config

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
