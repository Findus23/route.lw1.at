from enum import Enum


class VertexType(str, Enum):
    BIKESHARE = "BIKESHARE"
    NORMAL = "NORMAL"
    TRANSIT = "TRANSIT"

    def __str__(self) -> str:
        return str(self.value)
