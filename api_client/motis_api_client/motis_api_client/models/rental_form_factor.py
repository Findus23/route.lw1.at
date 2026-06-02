from enum import Enum


class RentalFormFactor(str, Enum):
    BICYCLE = "BICYCLE"
    CAR = "CAR"
    CARGO_BICYCLE = "CARGO_BICYCLE"
    MOPED = "MOPED"
    OTHER = "OTHER"
    SCOOTER_SEATED = "SCOOTER_SEATED"
    SCOOTER_STANDING = "SCOOTER_STANDING"

    def __str__(self) -> str:
        return str(self.value)
