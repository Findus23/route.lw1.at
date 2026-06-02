from enum import Enum


class FareMediaType(str, Enum):
    CONTACTLESS_EMV = "CONTACTLESS_EMV"
    MOBILE_APP = "MOBILE_APP"
    NONE = "NONE"
    PAPER_TICKET = "PAPER_TICKET"
    TRANSIT_CARD = "TRANSIT_CARD"

    def __str__(self) -> str:
        return str(self.value)
