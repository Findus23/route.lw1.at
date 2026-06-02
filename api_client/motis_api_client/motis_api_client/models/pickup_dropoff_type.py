from enum import Enum


class PickupDropoffType(str, Enum):
    NORMAL = "NORMAL"
    NOT_ALLOWED = "NOT_ALLOWED"

    def __str__(self) -> str:
        return str(self.value)
