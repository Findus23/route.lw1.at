from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.direction import Direction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encoded_polyline import EncodedPolyline


T = TypeVar("T", bound="StepInstruction")


@_attrs_define
class StepInstruction:
    """
    Attributes:
        relative_direction (Direction):
        distance (float): The distance in meters that this step takes.
        from_level (float): level where this segment starts, based on OpenStreetMap data
        to_level (float): level where this segment starts, based on OpenStreetMap data
        polyline (EncodedPolyline):
        street_name (str): The name of the street.
        exit_ (str): Not implemented!
            When exiting a highway or traffic circle, the exit name/number.
        stay_on (bool): Not implemented!
            Indicates whether or not a street changes direction at an intersection.
        area (bool): Not implemented!
            This step is on an open area, such as a plaza or train platform,
            and thus the directions should say something like "cross"
        osm_way (int | Unset): OpenStreetMap way index
        toll (bool | Unset): Indicates that a fee must be paid by general traffic to use a road, road bridge or road
            tunnel.
        access_restriction (str | Unset): Experimental. Indicates whether access to this part of the route is
            restricted.
            See: https://wiki.openstreetmap.org/wiki/Conditional_restrictions
        elevation_up (int | Unset): incline in meters across this path segment
        elevation_down (int | Unset): decline in meters across this path segment
    """

    relative_direction: Direction
    distance: float
    from_level: float
    to_level: float
    polyline: EncodedPolyline
    street_name: str
    exit_: str
    stay_on: bool
    area: bool
    osm_way: int | Unset = UNSET
    toll: bool | Unset = UNSET
    access_restriction: str | Unset = UNSET
    elevation_up: int | Unset = UNSET
    elevation_down: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relative_direction = self.relative_direction.value

        distance = self.distance

        from_level = self.from_level

        to_level = self.to_level

        polyline = self.polyline.to_dict()

        street_name = self.street_name

        exit_ = self.exit_

        stay_on = self.stay_on

        area = self.area

        osm_way = self.osm_way

        toll = self.toll

        access_restriction = self.access_restriction

        elevation_up = self.elevation_up

        elevation_down = self.elevation_down

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relativeDirection": relative_direction,
                "distance": distance,
                "fromLevel": from_level,
                "toLevel": to_level,
                "polyline": polyline,
                "streetName": street_name,
                "exit": exit_,
                "stayOn": stay_on,
                "area": area,
            }
        )
        if osm_way is not UNSET:
            field_dict["osmWay"] = osm_way
        if toll is not UNSET:
            field_dict["toll"] = toll
        if access_restriction is not UNSET:
            field_dict["accessRestriction"] = access_restriction
        if elevation_up is not UNSET:
            field_dict["elevationUp"] = elevation_up
        if elevation_down is not UNSET:
            field_dict["elevationDown"] = elevation_down

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encoded_polyline import EncodedPolyline

        d = dict(src_dict)
        relative_direction = Direction(d.pop("relativeDirection"))

        distance = d.pop("distance")

        from_level = d.pop("fromLevel")

        to_level = d.pop("toLevel")

        polyline = EncodedPolyline.from_dict(d.pop("polyline"))

        street_name = d.pop("streetName")

        exit_ = d.pop("exit")

        stay_on = d.pop("stayOn")

        area = d.pop("area")

        osm_way = d.pop("osmWay", UNSET)

        toll = d.pop("toll", UNSET)

        access_restriction = d.pop("accessRestriction", UNSET)

        elevation_up = d.pop("elevationUp", UNSET)

        elevation_down = d.pop("elevationDown", UNSET)

        step_instruction = cls(
            relative_direction=relative_direction,
            distance=distance,
            from_level=from_level,
            to_level=to_level,
            polyline=polyline,
            street_name=street_name,
            exit_=exit_,
            stay_on=stay_on,
            area=area,
            osm_way=osm_way,
            toll=toll,
            access_restriction=access_restriction,
            elevation_up=elevation_up,
            elevation_down=elevation_down,
        )

        step_instruction.additional_properties = d
        return step_instruction

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
