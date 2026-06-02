from enum import Enum


class RentalReturnConstraint(str, Enum):
    ANY_STATION = "ANY_STATION"
    NONE = "NONE"
    ROUNDTRIP_STATION = "ROUNDTRIP_STATION"

    def __str__(self) -> str:
        return str(self.value)
