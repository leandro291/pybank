from banco import Banco
from cliente import Cliente
from atm import ATM

class SistemaBanco:
    def __init__(self, banco: Banco, cliente: Cliente, atm: ATM):
        self._banco = banco
        self._cliente = cliente
        self._atm = atm