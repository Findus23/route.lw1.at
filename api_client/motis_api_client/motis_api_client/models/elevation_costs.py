from enum import Enum


class ElevationCosts(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
