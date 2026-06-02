from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_config import ServerConfig


T = TypeVar("T", bound="InitialResponse200")


@_attrs_define
class InitialResponse200:
    """
    Attributes:
        lat (float): latitude
        lon (float): longitude
        zoom (float): zoom level
        server_config (ServerConfig):
    """

    lat: float
    lon: float
    zoom: float
    server_config: ServerConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lat = self.lat

        lon = self.lon

        zoom = self.zoom

        server_config = self.server_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lat": lat,
                "lon": lon,
                "zoom": zoom,
                "serverConfig": server_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_config import ServerConfig

        d = dict(src_dict)
        lat = d.pop("lat")

        lon = d.pop("lon")

        zoom = d.pop("zoom")

        server_config = ServerConfig.from_dict(d.pop("serverConfig"))

        initial_response_200 = cls(
            lat=lat,
            lon=lon,
            zoom=zoom,
            server_config=server_config,
        )

        initial_response_200.additional_properties = d
        return initial_response_200

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
