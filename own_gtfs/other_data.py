from enum import StrEnum


class RouteType(StrEnum):
    FERRY = "FERRY"


ROUTE_TYPES_GTFS = {
    RouteType.FERRY: 4,
}
