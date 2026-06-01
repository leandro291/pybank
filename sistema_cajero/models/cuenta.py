from decimal import Decimal
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from utils.utils import validar_decimales

class Cuenta(ABC):

    _contador = 1

    def __init__(self, numero_cuenta: str, saldo: float, pin: str):
        super().__init__()
        self.id_cuenta = f"C{Cuenta._contador:03d}"
        self.numero_cuenta = numero_cuenta
        self.saldo = Decimal(str(saldo))
        self.pin = pin
        Cuenta._contador += 1

    def validar_contraseña(self, pin: str) -> None:

        if self.pin != pin:
            raise ValueError("No se pudo ingresar a la cuenta")

    @abstractmethod
    def depositar(self, monto: float) -> None:
        pass

    @abstractmethod
    def retirar(self, monto: float) -> None:
        pass

    @abstractmethod
    def __str__(self):
        pass

class CuentaAhorro(Cuenta):
    def __init__(self, numero_cuenta: str, saldo: float, pin: str, limite_retiros: int, tasa_interes: float):
        super().__init__(numero_cuenta, saldo, pin)
        self.limite_retiros = limite_retiros
        self.tasa_interes = tasa_interes
        self._retiros_realizados = 0
    
    def depositar(self, monto: float) -> None:

        monto_depositado = validar_decimales(monto)

        self.saldo += monto_depositado

    def retirar(self, monto: float) -> None:

        monto_depositado = validar_decimales(monto)

        if self._retiros_realizados >= self.limite_retiros:
            raise ValueError(f"Se alcanzo el limite de {self.limite_retiros} retiros")
        
        if monto_depositado > self.saldo:
            raise ValueError("Saldo insuficiente")
        
        self.saldo -= monto_depositado
        self._retiros_realizados += 1

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
    def __init__(self, numero_cuenta: str, saldo: float, pin: str, sobregiro: float):
        super().__init__(numero_cuenta, saldo, pin)
        self.sobregiro = sobregiro

    def depositar(self, monto: float) -> None:

        monto_depositado = validar_decimales(monto)

        self.saldo += monto_depositado

    def retirar(self, monto: float) -> None:

        monto_depositado = validar_decimales(monto)
    
        if monto_depositado > self.saldo + self.sobregiro:
            raise ValueError("Excede el limite de sobregiro")
        
        self.saldo -= monto_depositado

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
    def crear_cuenta(cls, tipo: str, numero_cuenta: str, saldo: float, pin: str, **parametros):
        clase = cls._tipos.get(tipo, None)

        if not clase:
            raise ValueError("No se encontro el tipo de cuenta")
        
        return clase(numero_cuenta, saldo, pin, **parametros)
    
    


        