from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ParetoSetEntry")


@_attrs_define
class ParetoSetEntry:
    """Object containing a single element of a ParetoSet

    Attributes:
        duration (float): duration in seconds for the the best solution using `transfer` transfers

            Notice that the resolution is currently in minutes, because of implementation details
        transfers (int): The minimal number of transfers required to arrive within `duration` seconds

            transfers=0: Direct transit connecion without any transfers
            transfers=1: Transit connection with 1 transfer
    """

    duration: float
    transfers: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        transfers = self.transfers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "transfers": transfers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration = d.pop("duration")

        transfers = d.pop("transfers")

        pareto_set_entry = cls(
            duration=duration,
            transfers=transfers,
        )

        pareto_set_entry.additional_properties = d
        return pareto_set_entry

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
