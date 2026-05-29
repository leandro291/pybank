from banco import Banco

class ATM:
    _contador = 1

    def __init__(self, ubicacion: str, dinero_disponible: float, banco: Banco):
        self.id_atm = f"ATM{ATM._contador:03d}"
        self.ubicacion = ubicacion
        self.dinero_disponible = dinero_disponible
        self.banco = banco
        self.activo: bool = True
        ATM._contador += 1