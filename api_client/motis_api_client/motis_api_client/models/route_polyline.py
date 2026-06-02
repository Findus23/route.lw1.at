from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.encoded_polyline import EncodedPolyline


T = TypeVar("T", bound="RoutePolyline")


@_attrs_define
class RoutePolyline:
    """Shared polyline used by one or more route segments

    Attributes:
        polyline (EncodedPolyline):
        colors (list[str]): Unique route colors of routes containing this segment
        route_indexes (list[int]): Indexes into the top-level routes array for routes containing this segment
    """

    polyline: EncodedPolyline
    colors: list[str]
    route_indexes: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        polyline = self.polyline.to_dict()

        colors = self.colors

        route_indexes = self.route_indexes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "polyline": polyline,
                "colors": colors,
                "routeIndexes": route_indexes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encoded_polyline import EncodedPolyline

        d = dict(src_dict)
        polyline = EncodedPolyline.from_dict(d.pop("polyline"))

        colors = cast(list[str], d.pop("colors"))

        route_indexes = cast(list[int], d.pop("routeIndexes"))

        route_polyline = cls(
            polyline=polyline,
            colors=colors,
            route_indexes=route_indexes,
        )

        route_polyline.additional_properties = d
        return route_polyline

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
