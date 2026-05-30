from abc import ABC, abstractmethod
from datetime import date
from banco import Banco

class Persona(ABC):
    def __init__(self, nombre: str, dni: str, telefono: str, correo: str, fecha_nacimiento: date):
        super().__init__()
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = self.fecha_nacimiento

    @abstractmethod
    def __str__(self):
        pass

class Usuario(Persona):

    _contador = 1

    def __init__(self, nombre: str, dni: str, telefono: str, correo: str, banco: Banco):
        super().__init__(nombre, dni, telefono, correo)
        self.id_usuario: str = f"P{Usuario._contador:03d}"
        self.banco = banco
        self.activo: bool = True
        self.fecha_registro = date.today()
        Usuario._contador += 1

    def __definir_estado(self) -> bool:
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

    def __str__(self) -> str:
        estado = self.__definir_estado()
        return (
            f"==== Datos del Cliente: {self.nombre} ====\n"
            f"  Id del Usuario   : {self.id_usuario}\n"
            f"  Nombre           : {self.nombre}\n"
            f"  DNI              : {self.dni}\n"
            f"  Teléfono         : {self.telefono}\n"
            f"  Correo           : {self.correo}\n"
            f"  Fecha Nacimiento : {self.fecha_nacimiento}\n"
            f"  Fecha Registro   : {self.fecha_registro}\n"
            f"  Banco            : {self.banco.nombre}\n"
            f"  Estado           : {estado}\n"
        )

if __name__ == "__main__":
    print()