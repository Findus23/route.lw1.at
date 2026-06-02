from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encoded_polyline import EncodedPolyline
    from ..models.rental_zone_restrictions import RentalZoneRestrictions


T = TypeVar("T", bound="RentalZone")


@_attrs_define
class RentalZone:
    """
    Attributes:
        provider_id (str): Unique identifier of the rental provider
        provider_group_id (str): Unique identifier of the rental provider group
        z (int): Zone precedence / z-index (higher number = higher precedence)
        bbox (list[float]): Bounding box of the area covered by this zone,
            [west, south, east, north] as [lon, lat, lon, lat]
        area (list[list[EncodedPolyline]]): A multi-polygon contains a number of polygons, each containing a number
            of rings, which are encoded as polylines (with precision 6).

            For each polygon, the first ring is the outer ring, all subsequent rings
            are inner rings (holes).
        rules (list[RentalZoneRestrictions]):
        name (str | Unset): Public name of the geofencing zone
    """

    provider_id: str
    provider_group_id: str
    z: int
    bbox: list[float]
    area: list[list[EncodedPolyline]]
    rules: list[RentalZoneRestrictions]
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        provider_group_id = self.provider_group_id

        z = self.z

        bbox = self.bbox

        area = []
        for componentsschemas_multi_polygon_item_data in self.area:
            componentsschemas_multi_polygon_item = []
            for componentsschemas_multi_polygon_item_item_data in componentsschemas_multi_polygon_item_data:
                componentsschemas_multi_polygon_item_item = componentsschemas_multi_polygon_item_item_data.to_dict()
                componentsschemas_multi_polygon_item.append(componentsschemas_multi_polygon_item_item)

            area.append(componentsschemas_multi_polygon_item)

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerId": provider_id,
                "providerGroupId": provider_group_id,
                "z": z,
                "bbox": bbox,
                "area": area,
                "rules": rules,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encoded_polyline import EncodedPolyline
        from ..models.rental_zone_restrictions import RentalZoneRestrictions

        d = dict(src_dict)
        provider_id = d.pop("providerId")

        provider_group_id = d.pop("providerGroupId")

        z = d.pop("z")

        bbox = cast(list[float], d.pop("bbox"))

        area = []
        _area = d.pop("area")
        for componentsschemas_multi_polygon_item_data in _area:
            componentsschemas_multi_polygon_item = []
            _componentsschemas_multi_polygon_item = componentsschemas_multi_polygon_item_data
            for componentsschemas_multi_polygon_item_item_data in _componentsschemas_multi_polygon_item:
                componentsschemas_multi_polygon_item_item = EncodedPolyline.from_dict(
                    componentsschemas_multi_polygon_item_item_data
                )

                componentsschemas_multi_polygon_item.append(componentsschemas_multi_polygon_item_item)

            area.append(componentsschemas_multi_polygon_item)

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = RentalZoneRestrictions.from_dict(rules_item_data)

            rules.append(rules_item)

        name = d.pop("name", UNSET)

        rental_zone = cls(
            provider_id=provider_id,
            provider_group_id=provider_group_id,
            z=z,
            bbox=bbox,
            area=area,
            rules=rules,
            name=name,
        )

        rental_zone.additional_properties = d
        return rental_zone

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
