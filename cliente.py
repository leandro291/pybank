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

    @abstractmethod
    def verificar_pin(self, pin: str) -> bool:
        pass

    @abstractmethod
    def desactivar_cuenta(self):
        pass

    @abstractmethod
    def activar_cuenta(self):
        pass

class Cliente(Persona):

    _contador = 1
    MAX_INTENTOS = 3

    def __init__(self, nombre: str, dni: str, telefono: str, correo: str, numero_cuenta: str, tipo_cuenta: str, saldo: float, pin: str, banco: Banco):
        super().__init__(nombre, dni, telefono, correo)
        self.id_cliente: str = f"P{Cliente._contador:03d}"
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo
        self.__pin = pin
        self.__intentos: int = 0
        self.__bloqueado: bool = False
        self.fecha_registro = date.today()
        self.banco = banco
        self.activo: bool = True
        Cliente._contador += 1

    def __verificar_estado(self) -> bool:
        return self.activo
    
    def __definir_estado(self) -> str:
        return "Activo" if self.activo else "Inactivo"

    def verificar_pin(self, pin: str) -> bool:
        """Metodo para verificar el PIN del Cliente"""

        if not self.activo:
            print("Su cuenta se encuentra inactiva")
            return False

        if self.__bloqueado:
            print("Su cuenta se encuentra bloqueada")
            return False
        
        if self.__pin == pin:
            self.__intentos = 0
            return True
        
        self.__intentos += 1
        restantes = self.MAX_INTENTOS - self.__intentos

        if self.__intentos >= self.MAX_INTENTOS:
            print(f"Se bloqueo su cuenta por varios intentos fallidos")
            self.__bloqueado = True
            return False
        else:
            print(f"Intento fallido, intentos restantes {restantes}")
            return False
        
    def desactivar_cuenta(self):
        """Metodo para desactivar la cuenta de un Cliente"""

        estado_cuenta = self.__verificar_estado()

        if estado_cuenta:
            self.activo = False
            print(f"Cuenta de {self.nombre} desactivada")
        else:
            print(f"La cuenta ya se encuentra inactiva")

    def activar_cuenta(self):
        """Metodo para activar la cuenta de un Cliente"""

        estado_cuenta = self.__verificar_estado()

        if not estado_cuenta:
            self.activo = True
            print(f"Cuenta de {self.nombre} activada")
        else:
            print(f"La cuenta ya se encuentra activa")
        
    def __str__(self) -> str:
        estado = self.__definir_estado()
        return (
            f"==== Datos del Cliente ====\n"
            f"  ID Cliente       : {self.id_cliente}\n"
            f"  Número de Cuenta : {self.numero_cuenta}\n"
            f"  Tipo de Cuenta   : {self.tipo_cuenta}\n"
            f"  Saldo            : S/. {self.saldo:.2f}\n"
            f"  Fecha de Registro: {self.fecha_registro}\n"
            f"  Banco            : {self.banco.nombre}\n"
            f"  Estado           : {estado}\n"
        )

if __name__ == "__main__":

    banco1 = Banco("Banco de la Nacion", "2415210244", "Av Tarapaca 123", "932905379")

    cliente1 = Cliente(
        nombre="Leandro Rojas",
        dni="60746923",
        telefono="932905312",
        correo="lenadrito1@gmail.com",
        numero_cuenta="VISA-123",
        tipo_cuenta="Ahorro",
        saldo=1500.00,
        pin="123456",
        banco=banco1
    )

    print(cliente1)