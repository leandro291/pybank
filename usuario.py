from abc import ABC, abstractmethod
from datetime import date
from typing import Dict, TYPE_CHECKING


class Persona(ABC):
    def __init__(self, nombre: str, dni: str, telefono: str, correo: str, fecha_nacimiento: date):
        super().__init__()
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str):

        nombre_limpio = valor.strip()

        if nombre_limpio == "":
            raise ValueError("El nombre no puede estar vacio")
        
        if not nombre_limpio.replace(" ", "").isalpha():
            raise ValueError("El nombre solo debe contener letras")

        self._nombre =  nombre_limpio
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, valor: str):

        dni_limpio = valor.strip()

        if len(dni_limpio) != 8:
            raise ValueError("El DNI debe contener un total de 8 digitos")
        
        if not dni_limpio.isdigit():
            raise ValueError("El DNI solo debe contener digitos")
    
        self._dni = dni_limpio

    @property
    def telefono(self):
        
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):

        telefono_limpio = valor.strip()

        if len(telefono_limpio) != 9:
            raise ValueError("El telefono debe contener un total de 9 digitos")
        
        if not telefono_limpio.isdigit():
            raise ValueError("El telefono solo debe contener digitos")
        
        self._telefono = telefono_limpio

    @property
    def correo(self):
        return self._correo
    
    @correo.setter
    def correo(self, valor: str):

        correo_limpio = valor.strip()

        if "@" not in correo_limpio or "." not in correo_limpio:
            raise ValueError("El correo ingresado no es valido")
        
        self._correo = correo_limpio
    
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, valor: date):

        if valor >= date.today():
            raise ValueError("La fecha de nacimiento no es valida")
            
        edad = date.today().year - valor.year
        if edad < 18:
            raise ValueError("Debe ser mayor de 18 años para registrarse")
    
        self._fecha_nacimiento = valor

    @abstractmethod
    def __str__(self):
        pass

class Usuario(Persona):

    _contador = 1

    def __init__(self, nombre: str, dni: str, telefono: str, correo: str, fecha_nacimiento: date):
        super().__init__(nombre, dni, telefono, correo, fecha_nacimiento)
        self.id_usuario: str = f"U{Usuario._contador:03d}"
        self.cuentas: Dict[str, "Cuenta"]  = {}
        self.fecha_registro = date.today()
        Usuario._contador += 1

    @staticmethod
    def limpiar_string(texto: str):
        return texto.strip()

    def vincular_cuenta(self, cuenta: "Cuenta") -> bool:

        if not cuenta:
            return False
        
        if cuenta.numero_cuenta in self.cuentas:
            raise ValueError("Esta cuenta ya se encuentra registrada")
        
        self.cuentas[cuenta.numero_cuenta] = cuenta
        return True

    def obtener_cuenta(self, numero_cuenta: str) -> "Cuenta":
        
        numero_limpio = self.limpiar_string(numero_cuenta)
        cuenta = self.cuentas.get(numero_limpio, None)

        if not cuenta:
            raise ValueError("Numero de cuenta invalido")
    
        return cuenta

    def __str__(self) -> str:
        return (
            f"==== Datos del Cliente: {self.nombre} ====\n"
            f"  Id del Usuario   : {self.id_usuario}\n"
            f"  Nombre           : {self.nombre}\n"
            f"  DNI              : {self.dni}\n"
            f"  Teléfono         : {self.telefono}\n"
            f"  Correo           : {self.correo}\n"
            f"  Fecha Nacimiento : {self.fecha_nacimiento}\n"
            f"  Fecha Registro   : {self.fecha_registro}\n"
        )

def main() -> None:

    try:
        usuario1 = Usuario(nombre="Leandro", dni="60746986", telefono="932002123", correo="lenadrito1@gmail.com", fecha_nacimiento=date(2005, 2, 14))

        ahorro1 = FabricaCuenta.crear_cuenta(
            tipo="ahorro",
            numero_cuenta="CTA-001",
            saldo=1500.00,
            usuario=usuario1,
            pin=123,
            limite_retiros=5,
            tasa_interes=0.035
        )

        ahorro2 = FabricaCuenta.crear_cuenta(
            tipo="ahorro",
            numero_cuenta="CTA-001",
            saldo=2500.00,
            usuario=usuario1,
            pin=123,
            limite_retiros=5,
            tasa_interes=0.035
        )

        corriente = FabricaCuenta.crear_cuenta(
            tipo="corriente",
            numero_cuenta="CTA-002",
            saldo=1200.00,
            usuario=usuario1,
            pin=1234,
            sobregiro=200
        )

        usuario1.vincular_cuenta(ahorro1)
        usuario1.vincular_cuenta(ahorro2)
        usuario1.vincular_cuenta(corriente)
        print(usuario1.obtener_cuenta("CTA-002"))

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    from cuenta import Cuenta, FabricaCuenta
    main()
