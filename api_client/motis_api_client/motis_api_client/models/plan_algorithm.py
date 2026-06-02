from enum import Enum


class PlanAlgorithm(str, Enum):
    PONG = "PONG"
    RAPTOR = "RAPTOR"
    TB = "TB"

    def __str__(self) -> str:
        return str(self.value)
