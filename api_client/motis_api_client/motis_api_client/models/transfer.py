from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place import Place


T = TypeVar("T", bound="Transfer")


@_attrs_define
class Transfer:
    """transfer from one location to another

    Attributes:
        to (Place):
        default (float | Unset): optional; missing if the GTFS did not contain a transfer
            transfer duration in minutes according to GTFS (+heuristics)
        foot (float | Unset): optional; missing if no path was found (timetable / osr)
            transfer duration in minutes for the foot profile
        foot_routed (float | Unset): optional; missing if no path was found with foot routing
            transfer duration in minutes for the foot profile
        wheelchair (float | Unset): optional; missing if no path was found with the wheelchair profile
            transfer duration in minutes for the wheelchair profile
        wheelchair_routed (float | Unset): optional; missing if no path was found with the wheelchair profile
            transfer duration in minutes for the wheelchair profile
        wheelchair_uses_elevator (bool | Unset): optional; missing if no path was found with the wheelchair profile
            true if the wheelchair path uses an elevator
        car (float | Unset): optional; missing if no path was found with car routing
            transfer duration in minutes for the car profile
    """

    to: Place
    default: float | Unset = UNSET
    foot: float | Unset = UNSET
    foot_routed: float | Unset = UNSET
    wheelchair: float | Unset = UNSET
    wheelchair_routed: float | Unset = UNSET
    wheelchair_uses_elevator: bool | Unset = UNSET
    car: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to = self.to.to_dict()

        default = self.default

        foot = self.foot

        foot_routed = self.foot_routed

        wheelchair = self.wheelchair

        wheelchair_routed = self.wheelchair_routed

        wheelchair_uses_elevator = self.wheelchair_uses_elevator

        car = self.car

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "to": to,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if foot is not UNSET:
            field_dict["foot"] = foot
        if foot_routed is not UNSET:
            field_dict["footRouted"] = foot_routed
        if wheelchair is not UNSET:
            field_dict["wheelchair"] = wheelchair
        if wheelchair_routed is not UNSET:
            field_dict["wheelchairRouted"] = wheelchair_routed
        if wheelchair_uses_elevator is not UNSET:
            field_dict["wheelchairUsesElevator"] = wheelchair_uses_elevator
        if car is not UNSET:
            field_dict["car"] = car

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place import Place

        d = dict(src_dict)
        to = Place.from_dict(d.pop("to"))

        default = d.pop("default", UNSET)

        foot = d.pop("foot", UNSET)

        foot_routed = d.pop("footRouted", UNSET)

        wheelchair = d.pop("wheelchair", UNSET)

        wheelchair_routed = d.pop("wheelchairRouted", UNSET)

        wheelchair_uses_elevator = d.pop("wheelchairUsesElevator", UNSET)

        car = d.pop("car", UNSET)

        transfer = cls(
            to=to,
            default=default,
            foot=foot,
            foot_routed=foot_routed,
            wheelchair=wheelchair,
            wheelchair_routed=wheelchair_routed,
            wheelchair_uses_elevator=wheelchair_uses_elevator,
            car=car,
        )

        transfer.additional_properties = d
        return transfer

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
