from cliente import Cliente
from atm import ATM
from typing import Dict

class Banco:
    def __init__(self, nombre: str, ruc: str, direccion_central: str, telefono: str):
        self.nombre = nombre
        self.ruc = ruc
        self.direccion_central = direccion_central
        self.telefono = telefono
        self.clientes: Dict[Dict[str, Cliente]] = {}
        self.atms: Dict[Dict[str, ATM]] = {}
