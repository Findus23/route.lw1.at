from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.place import Place
    from ..models.transfer import Transfer


T = TypeVar("T", bound="TransfersResponse200")


@_attrs_define
class TransfersResponse200:
    """
    Attributes:
        place (Place):
        root (Place):
        equivalences (list[Place]):
        has_foot_transfers (bool): true if the server has foot transfers computed
        has_wheelchair_transfers (bool): true if the server has wheelchair transfers computed
        has_car_transfers (bool): true if the server has car transfers computed
        transfers (list[Transfer]): all outgoing transfers of this location
    """

    place: Place
    root: Place
    equivalences: list[Place]
    has_foot_transfers: bool
    has_wheelchair_transfers: bool
    has_car_transfers: bool
    transfers: list[Transfer]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        place = self.place.to_dict()

        root = self.root.to_dict()

        equivalences = []
        for equivalences_item_data in self.equivalences:
            equivalences_item = equivalences_item_data.to_dict()
            equivalences.append(equivalences_item)

        has_foot_transfers = self.has_foot_transfers

        has_wheelchair_transfers = self.has_wheelchair_transfers

        has_car_transfers = self.has_car_transfers

        transfers = []
        for transfers_item_data in self.transfers:
            transfers_item = transfers_item_data.to_dict()
            transfers.append(transfers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "place": place,
                "root": root,
                "equivalences": equivalences,
                "hasFootTransfers": has_foot_transfers,
                "hasWheelchairTransfers": has_wheelchair_transfers,
                "hasCarTransfers": has_car_transfers,
                "transfers": transfers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place import Place
        from ..models.transfer import Transfer

        d = dict(src_dict)
        place = Place.from_dict(d.pop("place"))

        root = Place.from_dict(d.pop("root"))

        equivalences = []
        _equivalences = d.pop("equivalences")
        for equivalences_item_data in _equivalences:
            equivalences_item = Place.from_dict(equivalences_item_data)

            equivalences.append(equivalences_item)

        has_foot_transfers = d.pop("hasFootTransfers")

        has_wheelchair_transfers = d.pop("hasWheelchairTransfers")

        has_car_transfers = d.pop("hasCarTransfers")

        transfers = []
        _transfers = d.pop("transfers")
        for transfers_item_data in _transfers:
            transfers_item = Transfer.from_dict(transfers_item_data)

            transfers.append(transfers_item)

        transfers_response_200 = cls(
            place=place,
            root=root,
            equivalences=equivalences,
            has_foot_transfers=has_foot_transfers,
            has_wheelchair_transfers=has_wheelchair_transfers,
            has_car_transfers=has_car_transfers,
            transfers=transfers,
        )

        transfers_response_200.additional_properties = d
        return transfers_response_200

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
