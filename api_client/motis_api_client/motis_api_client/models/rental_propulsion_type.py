from enum import Enum


class RentalPropulsionType(str, Enum):
    COMBUSTION = "COMBUSTION"
    COMBUSTION_DIESEL = "COMBUSTION_DIESEL"
    ELECTRIC = "ELECTRIC"
    ELECTRIC_ASSIST = "ELECTRIC_ASSIST"
    HUMAN = "HUMAN"
    HYBRID = "HYBRID"
    HYDROGEN_FUEL_CELL = "HYDROGEN_FUEL_CELL"
    PLUG_IN_HYBRID = "PLUG_IN_HYBRID"

    def __str__(self) -> str:
        return str(self.value)
