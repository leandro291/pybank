from typing import TYPE_CHECKING
from decimal import Decimal

class Cajero:
    _contador = 1

    def __init__(self, ubicacion: str, dinero_disponible: float):
        self.id_atm = f"ATM{Cajero._contador:03d}"
        self.ubicacion = ubicacion
        self.dinero_disponible = dinero_disponible
        self.activo: bool = True
        Cajero._contador += 1

    def __str__(self) -> str:

        return (
            f"==== Datos del ATM: {self.id_atm} ====\n"
            f"  Ubicacion              : {self.ubicacion}\n"
            f"  Dinero Disponible      : {self.dinero_disponible}\n"
            f"  Activo                 : {self.activo}\n"
        )

