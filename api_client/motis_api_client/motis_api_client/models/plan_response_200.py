from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.itinerary import Itinerary
    from ..models.place import Place
    from ..models.plan_response_200_debug_output import PlanResponse200DebugOutput
    from ..models.plan_response_200_request_parameters import PlanResponse200RequestParameters


T = TypeVar("T", bound="PlanResponse200")


@_attrs_define
class PlanResponse200:
    r"""
    Attributes:
        request_parameters (PlanResponse200RequestParameters): the routing query
        debug_output (PlanResponse200DebugOutput): debug statistics
        from_ (Place):
        to (Place):
        direct (list[Itinerary]): Direct trips by `WALK`, `BIKE`, `CAR`, etc. without time-dependency.
            The starting time (`arriveBy=false`) / arrival time (`arriveBy=true`) is always the queried `time` parameter
            (set to \"now\" if not set).
            But all `direct` connections are meant to be independent of absolute times.
        itineraries (list[Itinerary]): list of itineraries
        previous_page_cursor (str): Use the cursor to get the previous page of results. Insert the cursor into the
            request and post it to get the previous page.
            The previous page is a set of itineraries departing BEFORE the first itinerary in the result for a depart after
            search. When using the default sort order the previous set of itineraries is inserted before the current result.
        next_page_cursor (str): Use the cursor to get the next page of results. Insert the cursor into the request and
            post it to get the next page.
            The next page is a set of itineraries departing AFTER the last itinerary in this result.
    """

    request_parameters: PlanResponse200RequestParameters
    debug_output: PlanResponse200DebugOutput
    from_: Place
    to: Place
    direct: list[Itinerary]
    itineraries: list[Itinerary]
    previous_page_cursor: str
    next_page_cursor: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_parameters = self.request_parameters.to_dict()

        debug_output = self.debug_output.to_dict()

        from_ = self.from_.to_dict()

        to = self.to.to_dict()

        direct = []
        for direct_item_data in self.direct:
            direct_item = direct_item_data.to_dict()
            direct.append(direct_item)

        itineraries = []
        for itineraries_item_data in self.itineraries:
            itineraries_item = itineraries_item_data.to_dict()
            itineraries.append(itineraries_item)

        previous_page_cursor = self.previous_page_cursor

        next_page_cursor = self.next_page_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestParameters": request_parameters,
                "debugOutput": debug_output,
                "from": from_,
                "to": to,
                "direct": direct,
                "itineraries": itineraries,
                "previousPageCursor": previous_page_cursor,
                "nextPageCursor": next_page_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.itinerary import Itinerary
        from ..models.place import Place
        from ..models.plan_response_200_debug_output import PlanResponse200DebugOutput
        from ..models.plan_response_200_request_parameters import PlanResponse200RequestParameters

        d = dict(src_dict)
        request_parameters = PlanResponse200RequestParameters.from_dict(d.pop("requestParameters"))

        debug_output = PlanResponse200DebugOutput.from_dict(d.pop("debugOutput"))

        from_ = Place.from_dict(d.pop("from"))

        to = Place.from_dict(d.pop("to"))

        direct = []
        _direct = d.pop("direct")
        for direct_item_data in _direct:
            direct_item = Itinerary.from_dict(direct_item_data)

            direct.append(direct_item)

        itineraries = []
        _itineraries = d.pop("itineraries")
        for itineraries_item_data in _itineraries:
            itineraries_item = Itinerary.from_dict(itineraries_item_data)

            itineraries.append(itineraries_item)

        previous_page_cursor = d.pop("previousPageCursor")

        next_page_cursor = d.pop("nextPageCursor")

        plan_response_200 = cls(
            request_parameters=request_parameters,
            debug_output=debug_output,
            from_=from_,
            to=to,
            direct=direct,
            itineraries=itineraries,
            previous_page_cursor=previous_page_cursor,
            next_page_cursor=next_page_cursor,
        )

        plan_response_200.additional_properties = d
        return plan_response_200

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
