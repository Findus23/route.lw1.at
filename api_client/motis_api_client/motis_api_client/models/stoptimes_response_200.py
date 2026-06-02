from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.place import Place
    from ..models.stop_time import StopTime


T = TypeVar("T", bound="StoptimesResponse200")


@_attrs_define
class StoptimesResponse200:
    """
    Attributes:
        stop_times (list[StopTime]): list of stop times
        place (Place):
        previous_page_cursor (str): Use the cursor to get the previous page of results. Insert the cursor into the
            request and post it to get the previous page.
            The previous page is a set of stop times BEFORE the first stop time in the result.
        next_page_cursor (str): Use the cursor to get the next page of results. Insert the cursor into the request and
            post it to get the next page.
            The next page is a set of stop times AFTER the last stop time in this result.
    """

    stop_times: list[StopTime]
    place: Place
    previous_page_cursor: str
    next_page_cursor: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stop_times = []
        for stop_times_item_data in self.stop_times:
            stop_times_item = stop_times_item_data.to_dict()
            stop_times.append(stop_times_item)

        place = self.place.to_dict()

        previous_page_cursor = self.previous_page_cursor

        next_page_cursor = self.next_page_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopTimes": stop_times,
                "place": place,
                "previousPageCursor": previous_page_cursor,
                "nextPageCursor": next_page_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place import Place
        from ..models.stop_time import StopTime

        d = dict(src_dict)
        stop_times = []
        _stop_times = d.pop("stopTimes")
        for stop_times_item_data in _stop_times:
            stop_times_item = StopTime.from_dict(stop_times_item_data)

            stop_times.append(stop_times_item)

        place = Place.from_dict(d.pop("place"))

        previous_page_cursor = d.pop("previousPageCursor")

        next_page_cursor = d.pop("nextPageCursor")

        stoptimes_response_200 = cls(
            stop_times=stop_times,
            place=place,
            previous_page_cursor=previous_page_cursor,
            next_page_cursor=next_page_cursor,
        )

        stoptimes_response_200.additional_properties = d
        return stoptimes_response_200

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
