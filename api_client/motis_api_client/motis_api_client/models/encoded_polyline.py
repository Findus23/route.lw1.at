from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EncodedPolyline")


@_attrs_define
class EncodedPolyline:
    """
    Attributes:
        points (str): The encoded points of the polyline using the Google polyline encoding.
        precision (int): The precision of the returned polyline (7 for /v1, 6 for /v2)
            Be aware that with precision 7, coordinates with |longitude| > 107.37 are undefined/will overflow.
        length (int): The number of points in the string
    """

    points: str
    precision: int
    length: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points = self.points

        precision = self.precision

        length = self.length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "points": points,
                "precision": precision,
                "length": length,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        points = d.pop("points")

        precision = d.pop("precision")

        length = d.pop("length")

        encoded_polyline = cls(
            points=points,
            precision=precision,
            length=length,
        )

        encoded_polyline.additional_properties = d
        return encoded_polyline

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
