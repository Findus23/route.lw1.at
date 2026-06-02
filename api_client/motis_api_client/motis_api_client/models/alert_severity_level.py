from enum import Enum


class AlertSeverityLevel(str, Enum):
    INFO = "INFO"
    SEVERE = "SEVERE"
    UNKNOWN_SEVERITY = "UNKNOWN_SEVERITY"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
