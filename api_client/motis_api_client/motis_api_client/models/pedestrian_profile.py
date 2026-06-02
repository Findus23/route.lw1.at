from enum import Enum


class PedestrianProfile(str, Enum):
    FOOT = "FOOT"
    WHEELCHAIR = "WHEELCHAIR"

    def __str__(self) -> str:
        return str(self.value)
