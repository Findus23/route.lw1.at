from enum import Enum


class FareTransferRule(str, Enum):
    AB = "AB"
    A_AB = "A_AB"
    A_AB_B = "A_AB_B"

    def __str__(self) -> str:
        return str(self.value)
