from banco import Banco
from abc import ABC, abstractmethod
from datetime import date

class Persona(ABC):
    def __init__(self, nombre: str, dni: str, telefono: str, correo: str):
        super().__init__()
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.correo = correo

class Cliente(Persona):
    _contador = 1

    def __init__(self, nombre: str, dni: str, telefono: str, correo: str, numero_cuenta: str, tipo_cuenta: str, saldo: float, banco: Banco):
        super().__init__(nombre, dni, telefono, correo)
        self.id_cliente = f"P{Cliente._contador:03d}"
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo
        self.fecha_registro = date.today()
        self.banco = banco
        self.activo: bool = True
        Cliente._contador += 1