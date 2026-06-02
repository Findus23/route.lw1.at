from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.location_type import LocationType
from ..models.mode import Mode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.area import Area


T = TypeVar("T", bound="Match")


@_attrs_define
class Match:
    """GeoCoding match

    Attributes:
        type_ (LocationType): location type
        tokens (list[list[float]]): list of non-overlapping tokens that were matched
        name (str): name of the location (transit stop / PoI / address)
        id (str): unique ID of the location
        lat (float): latitude
        lon (float): longitude
        areas (list[Area]): list of areas
        score (float): score according to the internal scoring system (the scoring algorithm might change in the future)
        category (str | Unset): Experimental. Type categories might be adjusted.

            For OSM stop locations: the amenity type based on
            https://wiki.openstreetmap.org/wiki/OpenStreetMap_Carto/Symbols
        level (float | Unset): level according to OpenStreetMap
            (at the moment only for public transport)
        street (str | Unset): street name
        house_number (str | Unset): house number
        country (str | Unset): ISO3166-1 country code from OpenStreetMap
        zip_ (str | Unset): zip code
        tz (str | Unset): timezone name (e.g. "Europe/Berlin")
        modes (list[Mode] | Unset): available transport modes for stops
        importance (float | Unset): importance of a stop, normalized from [0, 1]
    """

    type_: LocationType
    tokens: list[list[float]]
    name: str
    id: str
    lat: float
    lon: float
    areas: list[Area]
    score: float
    category: str | Unset = UNSET
    level: float | Unset = UNSET
    street: str | Unset = UNSET
    house_number: str | Unset = UNSET
    country: str | Unset = UNSET
    zip_: str | Unset = UNSET
    tz: str | Unset = UNSET
    modes: list[Mode] | Unset = UNSET
    importance: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        tokens = []
        for tokens_item_data in self.tokens:
            tokens_item = tokens_item_data

            tokens.append(tokens_item)

        name = self.name

        id = self.id

        lat = self.lat

        lon = self.lon

        areas = []
        for areas_item_data in self.areas:
            areas_item = areas_item_data.to_dict()
            areas.append(areas_item)

        score = self.score

        category = self.category

        level = self.level

        street = self.street

        house_number = self.house_number

        country = self.country

        zip_ = self.zip_

        tz = self.tz

        modes: list[str] | Unset = UNSET
        if not isinstance(self.modes, Unset):
            modes = []
            for modes_item_data in self.modes:
                modes_item = modes_item_data.value
                modes.append(modes_item)

        importance = self.importance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "tokens": tokens,
                "name": name,
                "id": id,
                "lat": lat,
                "lon": lon,
                "areas": areas,
                "score": score,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if level is not UNSET:
            field_dict["level"] = level
        if street is not UNSET:
            field_dict["street"] = street
        if house_number is not UNSET:
            field_dict["houseNumber"] = house_number
        if country is not UNSET:
            field_dict["country"] = country
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if tz is not UNSET:
            field_dict["tz"] = tz
        if modes is not UNSET:
            field_dict["modes"] = modes
        if importance is not UNSET:
            field_dict["importance"] = importance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.area import Area

        d = dict(src_dict)
        type_ = LocationType(d.pop("type"))

        tokens = []
        _tokens = d.pop("tokens")
        for tokens_item_data in _tokens:
            tokens_item = cast(list[float], tokens_item_data)

            tokens.append(tokens_item)

        name = d.pop("name")

        id = d.pop("id")

        lat = d.pop("lat")

        lon = d.pop("lon")

        areas = []
        _areas = d.pop("areas")
        for areas_item_data in _areas:
            areas_item = Area.from_dict(areas_item_data)

            areas.append(areas_item)

        score = d.pop("score")

        category = d.pop("category", UNSET)

        level = d.pop("level", UNSET)

        street = d.pop("street", UNSET)

        house_number = d.pop("houseNumber", UNSET)

        country = d.pop("country", UNSET)

        zip_ = d.pop("zip", UNSET)

        tz = d.pop("tz", UNSET)

        _modes = d.pop("modes", UNSET)
        modes: list[Mode] | Unset = UNSET
        if _modes is not UNSET:
            modes = []
            for modes_item_data in _modes:
                modes_item = Mode(modes_item_data)

                modes.append(modes_item)

        importance = d.pop("importance", UNSET)

        match = cls(
            type_=type_,
            tokens=tokens,
            name=name,
            id=id,
            lat=lat,
            lon=lon,
            areas=areas,
            score=score,
            category=category,
            level=level,
            street=street,
            house_number=house_number,
            country=country,
            zip_=zip_,
            tz=tz,
            modes=modes,
            importance=importance,
        )

        match.additional_properties = d
        return match

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
