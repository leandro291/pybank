from typing import TYPE_CHECKING
from decimal import Decimal
from utils.utils import validar_decimales

if TYPE_CHECKING:
    from models.cuenta import Cuenta

class Cajero:
    _contador = 1

    def __init__(self, ubicacion: str, dinero_disponible: float):
        self.id_atm = f"ATM{Cajero._contador:03d}"
        self.ubicacion = ubicacion
        self.dinero_disponible = Decimal(str(dinero_disponible))
        Cajero._contador += 1
        
    def _validar_dinero_disponible(self, monto: float) -> None:

        monto_validado = validar_decimales(monto)

        if monto_validado > self.dinero_disponible:
            raise ValueError("Dinero no disponible")
        
    def hacer_retiro(self, cuenta: "Cuenta", monto: float, pin: str):

        self._validar_dinero_disponible(monto)
        cuenta.validar_contraseña(pin)
        monto_validado = validar_decimales(monto)
        cuenta.retirar(monto_validado)
        self.dinero_disponible -= monto_validado
        
    def __str__(self) -> str:

        return (
            f"==== Datos del ATM: {self.id_atm} ====\n"
            f"  Ubicacion              : {self.ubicacion}\n"
            f"  Dinero Disponible      : {self.dinero_disponible}\n"
        )

if __name__ == "__main__":
    print()
