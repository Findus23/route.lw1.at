from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fare_transfer import FareTransfer
    from ..models.leg import Leg


T = TypeVar("T", bound="Itinerary")


@_attrs_define
class Itinerary:
    """
    Attributes:
        duration (int): journey duration in seconds
        start_time (datetime.datetime): journey departure time
        end_time (datetime.datetime): journey arrival time
        transfers (int): The number of transfers this trip has.
        id (str): Experimental (format might change). Opaque itinerary identifier.
            Pass it as `itineraryId` to `refresh-itinerary` endpoint for reconstruction using the new schedule/realtime
            data.
        legs (list[Leg]): Journey legs
        fare_transfers (list[FareTransfer] | Unset): Fare information
    """

    duration: int
    start_time: datetime.datetime
    end_time: datetime.datetime
    transfers: int
    id: str
    legs: list[Leg]
    fare_transfers: list[FareTransfer] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        transfers = self.transfers

        id = self.id

        legs = []
        for legs_item_data in self.legs:
            legs_item = legs_item_data.to_dict()
            legs.append(legs_item)

        fare_transfers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fare_transfers, Unset):
            fare_transfers = []
            for fare_transfers_item_data in self.fare_transfers:
                fare_transfers_item = fare_transfers_item_data.to_dict()
                fare_transfers.append(fare_transfers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "startTime": start_time,
                "endTime": end_time,
                "transfers": transfers,
                "id": id,
                "legs": legs,
            }
        )
        if fare_transfers is not UNSET:
            field_dict["fareTransfers"] = fare_transfers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fare_transfer import FareTransfer
        from ..models.leg import Leg

        d = dict(src_dict)
        duration = d.pop("duration")

        start_time = datetime.datetime.fromisoformat(d.pop("startTime"))

        end_time = datetime.datetime.fromisoformat(d.pop("endTime"))

        transfers = d.pop("transfers")

        id = d.pop("id")

        legs = []
        _legs = d.pop("legs")
        for legs_item_data in _legs:
            legs_item = Leg.from_dict(legs_item_data)

            legs.append(legs_item)

        _fare_transfers = d.pop("fareTransfers", UNSET)
        fare_transfers: list[FareTransfer] | Unset = UNSET
        if _fare_transfers is not UNSET:
            fare_transfers = []
            for fare_transfers_item_data in _fare_transfers:
                fare_transfers_item = FareTransfer.from_dict(fare_transfers_item_data)

                fare_transfers.append(fare_transfers_item)

        itinerary = cls(
            duration=duration,
            start_time=start_time,
            end_time=end_time,
            transfers=transfers,
            id=id,
            legs=legs,
            fare_transfers=fare_transfers,
        )

        itinerary.additional_properties = d
        return itinerary

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
