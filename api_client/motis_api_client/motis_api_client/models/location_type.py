from enum import Enum


class LocationType(str, Enum):
    ADDRESS = "ADDRESS"
    PLACE = "PLACE"
    STOP = "STOP"

    def __str__(self) -> str:
        return str(self.value)
