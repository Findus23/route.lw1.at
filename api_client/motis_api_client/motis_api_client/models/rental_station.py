from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rental_form_factor import RentalFormFactor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encoded_polyline import EncodedPolyline
    from ..models.rental_station_vehicle_docks_available import RentalStationVehicleDocksAvailable
    from ..models.rental_station_vehicle_types_available import RentalStationVehicleTypesAvailable


T = TypeVar("T", bound="RentalStation")


@_attrs_define
class RentalStation:
    """
    Attributes:
        id (str): Unique identifier of the rental station
        provider_id (str): Unique identifier of the rental provider
        provider_group_id (str): Unique identifier of the rental provider group
        name (str): Public name of the station
        lat (float): latitude
        lon (float): longitude
        is_renting (bool): true if vehicles can be rented from this station, false if it is temporarily out of service
        is_returning (bool): true if vehicles can be returned to this station, false if it is temporarily out of service
        num_vehicles_available (int): Number of vehicles available for rental at this station
        form_factors (list[RentalFormFactor]): List of form factors available for rental and/or return at this station
        vehicle_types_available (RentalStationVehicleTypesAvailable): List of vehicle types currently available at this
            station (vehicle type ID -> count)
        vehicle_docks_available (RentalStationVehicleDocksAvailable): List of vehicle docks currently available at this
            station (vehicle type ID -> count)
        bbox (list[float]): Bounding box of the area covered by this station,
            [west, south, east, north] as [lon, lat, lon, lat]
        address (str | Unset): Address where the station is located
        cross_street (str | Unset): Cross street or landmark where the station is located
        rental_uri_android (str | Unset): Rental URI for Android (deep link to the specific station)
        rental_uri_ios (str | Unset): Rental URI for iOS (deep link to the specific station)
        rental_uri_web (str | Unset): Rental URI for web (deep link to the specific station)
        station_area (list[list[EncodedPolyline]] | Unset): A multi-polygon contains a number of polygons, each
            containing a number
            of rings, which are encoded as polylines (with precision 6).

            For each polygon, the first ring is the outer ring, all subsequent rings
            are inner rings (holes).
    """

    id: str
    provider_id: str
    provider_group_id: str
    name: str
    lat: float
    lon: float
    is_renting: bool
    is_returning: bool
    num_vehicles_available: int
    form_factors: list[RentalFormFactor]
    vehicle_types_available: RentalStationVehicleTypesAvailable
    vehicle_docks_available: RentalStationVehicleDocksAvailable
    bbox: list[float]
    address: str | Unset = UNSET
    cross_street: str | Unset = UNSET
    rental_uri_android: str | Unset = UNSET
    rental_uri_ios: str | Unset = UNSET
    rental_uri_web: str | Unset = UNSET
    station_area: list[list[EncodedPolyline]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        provider_id = self.provider_id

        provider_group_id = self.provider_group_id

        name = self.name

        lat = self.lat

        lon = self.lon

        is_renting = self.is_renting

        is_returning = self.is_returning

        num_vehicles_available = self.num_vehicles_available

        form_factors = []
        for form_factors_item_data in self.form_factors:
            form_factors_item = form_factors_item_data.value
            form_factors.append(form_factors_item)

        vehicle_types_available = self.vehicle_types_available.to_dict()

        vehicle_docks_available = self.vehicle_docks_available.to_dict()

        bbox = self.bbox

        address = self.address

        cross_street = self.cross_street

        rental_uri_android = self.rental_uri_android

        rental_uri_ios = self.rental_uri_ios

        rental_uri_web = self.rental_uri_web

        station_area: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.station_area, Unset):
            station_area = []
            for componentsschemas_multi_polygon_item_data in self.station_area:
                componentsschemas_multi_polygon_item = []
                for componentsschemas_multi_polygon_item_item_data in componentsschemas_multi_polygon_item_data:
                    componentsschemas_multi_polygon_item_item = componentsschemas_multi_polygon_item_item_data.to_dict()
                    componentsschemas_multi_polygon_item.append(componentsschemas_multi_polygon_item_item)

                station_area.append(componentsschemas_multi_polygon_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "providerId": provider_id,
                "providerGroupId": provider_group_id,
                "name": name,
                "lat": lat,
                "lon": lon,
                "isRenting": is_renting,
                "isReturning": is_returning,
                "numVehiclesAvailable": num_vehicles_available,
                "formFactors": form_factors,
                "vehicleTypesAvailable": vehicle_types_available,
                "vehicleDocksAvailable": vehicle_docks_available,
                "bbox": bbox,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if cross_street is not UNSET:
            field_dict["crossStreet"] = cross_street
        if rental_uri_android is not UNSET:
            field_dict["rentalUriAndroid"] = rental_uri_android
        if rental_uri_ios is not UNSET:
            field_dict["rentalUriIOS"] = rental_uri_ios
        if rental_uri_web is not UNSET:
            field_dict["rentalUriWeb"] = rental_uri_web
        if station_area is not UNSET:
            field_dict["stationArea"] = station_area

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encoded_polyline import EncodedPolyline
        from ..models.rental_station_vehicle_docks_available import RentalStationVehicleDocksAvailable
        from ..models.rental_station_vehicle_types_available import RentalStationVehicleTypesAvailable

        d = dict(src_dict)
        id = d.pop("id")

        provider_id = d.pop("providerId")

        provider_group_id = d.pop("providerGroupId")

        name = d.pop("name")

        lat = d.pop("lat")

        lon = d.pop("lon")

        is_renting = d.pop("isRenting")

        is_returning = d.pop("isReturning")

        num_vehicles_available = d.pop("numVehiclesAvailable")

        form_factors = []
        _form_factors = d.pop("formFactors")
        for form_factors_item_data in _form_factors:
            form_factors_item = RentalFormFactor(form_factors_item_data)

            form_factors.append(form_factors_item)

        vehicle_types_available = RentalStationVehicleTypesAvailable.from_dict(d.pop("vehicleTypesAvailable"))

        vehicle_docks_available = RentalStationVehicleDocksAvailable.from_dict(d.pop("vehicleDocksAvailable"))

        bbox = cast(list[float], d.pop("bbox"))

        address = d.pop("address", UNSET)

        cross_street = d.pop("crossStreet", UNSET)

        rental_uri_android = d.pop("rentalUriAndroid", UNSET)

        rental_uri_ios = d.pop("rentalUriIOS", UNSET)

        rental_uri_web = d.pop("rentalUriWeb", UNSET)

        _station_area = d.pop("stationArea", UNSET)
        station_area: list[list[EncodedPolyline]] | Unset = UNSET
        if _station_area is not UNSET:
            station_area = []
            for componentsschemas_multi_polygon_item_data in _station_area:
                componentsschemas_multi_polygon_item = []
                _componentsschemas_multi_polygon_item = componentsschemas_multi_polygon_item_data
                for componentsschemas_multi_polygon_item_item_data in _componentsschemas_multi_polygon_item:
                    componentsschemas_multi_polygon_item_item = EncodedPolyline.from_dict(
                        componentsschemas_multi_polygon_item_item_data
                    )

                    componentsschemas_multi_polygon_item.append(componentsschemas_multi_polygon_item_item)

                station_area.append(componentsschemas_multi_polygon_item)

        rental_station = cls(
            id=id,
            provider_id=provider_id,
            provider_group_id=provider_group_id,
            name=name,
            lat=lat,
            lon=lon,
            is_renting=is_renting,
            is_returning=is_returning,
            num_vehicles_available=num_vehicles_available,
            form_factors=form_factors,
            vehicle_types_available=vehicle_types_available,
            vehicle_docks_available=vehicle_docks_available,
            bbox=bbox,
            address=address,
            cross_street=cross_street,
            rental_uri_android=rental_uri_android,
            rental_uri_ios=rental_uri_ios,
            rental_uri_web=rental_uri_web,
            station_area=station_area,
        )

        rental_station.additional_properties = d
        return rental_station

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
