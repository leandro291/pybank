from abc import ABC, abstractmethod
from decimal import Decimal
from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from usuario import Usuario

class Cuenta(ABC):

    _contador = 1

    def __init__(self, numero_cuenta: str, saldo: float, usuario: "Usuario"):
        super().__init__()
        self.id_cuenta = f"C00{Cuenta._contador:03d}"
        self.usuario = usuario
        self.numero_cuenta = numero_cuenta
        self.saldo = Decimal(str(saldo))
        self.activo: bool = True
        Cuenta._contador += 1

    def _definir_estado(self) -> bool:
        return "Activo" if self.activo else "Inactivo"

    def desactivar_estado(self) -> bool:

        if self.activo:
            self.activo = False
            return True
        else:
            return False
        
    def activar_estado(self) -> bool:

        if not self.activo:
            self.activo = True
            return True
        else:
            return False

    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod
    def retirar(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class CuentaAhorro(Cuenta):
    def __init__(self, numero_cuenta: str, saldo: float, usuario: "Usuario", limite_retiros: int, tasa_interes: float):
        super().__init__(numero_cuenta, saldo, usuario)
        self.limite_retiros = limite_retiros
        self.tasa_interes = tasa_interes
    
    def depositar(self):
        pass

    def retirar(self):
        pass

    def __str__(self):
        return (
            f"==== Datos de la Cuenta: {self.numero_cuenta} ====\n"
            f"  Id de la Cuenta    : {self.id_cuenta}\n"
            f"  Saldo              : {self.saldo}\n"
            f"  Usuario            : {self.usuario.nombre}\n"
            f"  Limite retiros     : {self.limite_retiros}\n"
            f"  Tasa de interes    : {self.tasa_interes}\n"
        )

class CuentaCorriente(Cuenta):
    def __init__(self, numero_cuenta: str, saldo: float, usuario: "Usuario", sobregiro: float):
        super().__init__(numero_cuenta, saldo, usuario)
        self.sobregiro = sobregiro

    def depositar(self):
        pass

    def retirar(self):
        pass

    def __str__(self):
        return (
            f"==== Datos de la Cuenta: {self.numero_cuenta} ====\n"
            f"  Id de la Cuenta    : {self.id_cuenta}\n"
            f"  Saldo              : {self.saldo}\n"
            f"  Usuario            : {self.usuario.nombre}\n"
            f"  Sobregiro          : {self.sobregiro}\n"
        )

class FabricaCuenta:

    _tipos = {
        "ahorro" : CuentaAhorro,
        "corriente" : CuentaCorriente
    }

    @classmethod
    def crear_cuenta(cls, tipo: str, numero_cuenta: str, saldo: float, usuario: "Usuario", **parametros):
        clase = cls._tipos.get(tipo, None)

        if not clase:
            raise ValueError("No se encontro el tipo de cuenta")
        
        return clase(numero_cuenta, saldo, usuario, **parametros)

if __name__ == "__main__":
    from usuario import Usuario
    from banco import Banco

    try:

        banco1 = Banco("Banco del Peru", "20252024123", "Av Ferreñafe 288", "932932123")
        cliente1 = Usuario(
            nombre="Leandro Rojas",
            dni="60746923",
            telefono="932905312",
            correo="lenadrito1@gmail.com",
            fecha_nacimiento=date(2006, 6, 15),  
            banco=banco1
        )

        ahorro = FabricaCuenta.crear_cuenta(
            tipo="ahorro",
            numero_cuenta="CTA-001",
            saldo=1500.00,
            usuario=cliente1,
            limite_retiros=5,
            tasa_interes=0.035
        )


        print(ahorro)

    except ValueError as e:
        print(f"Error {e}")
    


        