from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration import Duration
    from ..models.pareto_set_entry import ParetoSetEntry


T = TypeVar("T", bound="OneToManyIntermodalResponse")


@_attrs_define
class OneToManyIntermodalResponse:
    """Object containing the optimal street and transit durations for One-to-Many routing

    Attributes:
        street_durations (list[Duration] | Unset): Fastest durations for street routing
            The order of the items corresponds to the order of the `many` locations
            If no street routed connection is found, the corresponding `Duration` will be empty
        transit_durations (list[list[ParetoSetEntry]] | Unset): Pareto optimal solutions
            The order of the items corresponds to the order of the `many` locations
            If no connection using transits is found, the corresponding `ParetoSet` will be empty
    """

    street_durations: list[Duration] | Unset = UNSET
    transit_durations: list[list[ParetoSetEntry]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        street_durations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.street_durations, Unset):
            street_durations = []
            for street_durations_item_data in self.street_durations:
                street_durations_item = street_durations_item_data.to_dict()
                street_durations.append(street_durations_item)

        transit_durations: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.transit_durations, Unset):
            transit_durations = []
            for transit_durations_item_data in self.transit_durations:
                transit_durations_item = []
                for componentsschemas_pareto_set_item_data in transit_durations_item_data:
                    componentsschemas_pareto_set_item = componentsschemas_pareto_set_item_data.to_dict()
                    transit_durations_item.append(componentsschemas_pareto_set_item)

                transit_durations.append(transit_durations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if street_durations is not UNSET:
            field_dict["street_durations"] = street_durations
        if transit_durations is not UNSET:
            field_dict["transit_durations"] = transit_durations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duration import Duration
        from ..models.pareto_set_entry import ParetoSetEntry

        d = dict(src_dict)
        _street_durations = d.pop("street_durations", UNSET)
        street_durations: list[Duration] | Unset = UNSET
        if _street_durations is not UNSET:
            street_durations = []
            for street_durations_item_data in _street_durations:
                street_durations_item = Duration.from_dict(street_durations_item_data)

                street_durations.append(street_durations_item)

        _transit_durations = d.pop("transit_durations", UNSET)
        transit_durations: list[list[ParetoSetEntry]] | Unset = UNSET
        if _transit_durations is not UNSET:
            transit_durations = []
            for transit_durations_item_data in _transit_durations:
                transit_durations_item = []
                _transit_durations_item = transit_durations_item_data
                for componentsschemas_pareto_set_item_data in _transit_durations_item:
                    componentsschemas_pareto_set_item = ParetoSetEntry.from_dict(componentsschemas_pareto_set_item_data)

                    transit_durations_item.append(componentsschemas_pareto_set_item)

                transit_durations.append(transit_durations_item)

        one_to_many_intermodal_response = cls(
            street_durations=street_durations,
            transit_durations=transit_durations,
        )

        one_to_many_intermodal_response.additional_properties = d
        return one_to_many_intermodal_response

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
