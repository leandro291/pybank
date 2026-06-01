from decimal import Decimal
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.cuenta import Cuenta
    from models.cajero import Cajero

class Transaccion:

    _contador = 1

    def __init__(self, cuenta: "Cuenta", cajero: "Cajero", tipo: str, monto: float):
        self.id_transaccion = f"T{Transaccion._contador:03d}"
        self.cuenta = cuenta
        self.cajero = cajero
        self.tipo_transaccion = tipo
        self.monto = Decimal(str(monto))
        self.fecha = date.today()
        Transaccion._contador += 1

    def __str__(self) -> str:
        return (
            f"==== Transaccion: {self.id_transaccion} ====\n"
            f"  Tipo               : {self.tipo_transaccion}\n"
            f"  Monto              : {self.monto}\n"
            f"  Cuenta             : {self.cuenta.numero_cuenta}\n"
            f"  Titular            : {self.cuenta.usuario.nombre}\n"
            f"  Cajero             : {self.cajero.id_cajero}\n"
            f"  Ubicacion          : {self.cajero.ubicacion}\n"
            f"  Fecha              : {self.fecha}\n"
        )
    
def main():
    print()

if __name__ == "__main__":
    main()