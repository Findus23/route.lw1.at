from enum import Enum


class RoutePathSource(str, Enum):
    NONE = "NONE"
    ROUTED = "ROUTED"
    TIMETABLE = "TIMETABLE"

    def __str__(self) -> str:
        return str(self.value)
