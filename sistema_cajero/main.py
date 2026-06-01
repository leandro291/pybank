from models.cajero import Cajero
from models.cuenta import Cuenta, FabricaCuenta
from models.usuario import Usuario
from datetime import date

def main():

    # CREACION DE USUARIOS

    user1 = Usuario(
        nombre="Leandro",
        dni="55566622",
        telefono="932905122",
        correo="lenadrito1@gmail.com",
        fecha_nacimiento=date(1992,2,12)
    )

    user2 = Usuario(
        nombre="Brandon",
        dni="12345678",
        telefono="999123123",
        correo="brandon@gmail.com",
        fecha_nacimiento=date(1922,1,15)
    )

    print(user1)
    print(user2)

    #CREACION DE CUENTAS

    cuenta1 = FabricaCuenta.crear_cuenta(
        tipo="ahorro",
        numero_cuenta="VISA-001",
        saldo=1500.00,
        usuario=user1,
        pin="leo123",
        limite_retiros=3,
        tasa_interes=0.10
    )

    print(cuenta1)


if __name__ == "__main__":
    main()