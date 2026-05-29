from typing import Dict, TYPE_CHECKING
from cliente import Cliente

if TYPE_CHECKING:
    from cliente import Cliente
    from atm import ATM

class Banco:
    def __init__(self, nombre: str, ruc: str, direccion_central: str, telefono: str):
        self.nombre = nombre
        self.ruc = ruc
        self.direccion_central = direccion_central
        self.telefono = telefono
        self.clientes: Dict[str, Cliente] = {}
        self.atms: Dict[str, ATM] = {}

    def agregar_cliente(self, cliente: Cliente) -> bool:
        
        self.clientes[cliente.id_cliente] = cliente
        return True
    
    def buscar_cliente(self, dni: str) -> Cliente:

        for cliente in self.clientes.values():
            if cliente.dni == dni:
                return cliente
    
    def eliminar_cliente(self, dni: str) -> bool:

        for cliente in self.clientes.values():
            if cliente.dni == dni:
                cliente.desactivar_cuenta()
                return True
        
        return False
    

    def listar_cliente(self):
        for cliente in self.clientes.values():
            print(cliente)

if __name__ == "__main__":
    
    banco1 = Banco("Banco de la Nacion", "2415210244", "Av Tarapaca 123", "932905379")

    clientes = [
        Cliente(
            nombre="Leandro Rojas",
            dni="60746923",
            telefono="932905312",
            correo="lenadrito1@gmail.com",
            numero_cuenta="VISA-123",
            tipo_cuenta="Ahorro",
            saldo=1500.00,
            pin="123456",
            banco=banco1
        ),
        Cliente(
            nombre="Noelia Vargas",
            dni="71234567",
            telefono="987654321",
            correo="noelia.v@email.com",
            numero_cuenta="MC-456",
            tipo_cuenta="Corriente",
            saldo=2450.50,
            pin="892314",
            banco=banco1
        ),
        Cliente(
            nombre="Carlos Mendoza",
            dni="08451239",
            telefono="912345678",
            correo="carlos.mend@email.com",
            numero_cuenta="VISA-789",
            tipo_cuenta="Ahorro",
            saldo=840.00,
            pin="456789",
            banco=banco1
        ),
        Cliente(
            nombre="Andrea Flores",
            dni="45678901",
            telefono="956781234",
            correo="andrea.f@email.com",
            numero_cuenta="VISA-321",
            tipo_cuenta="Sueldo",
            saldo=3200.75,
            pin="112233",
            banco=banco1
        ),
        Cliente(
            nombre="Jorge Silva",
            dni="10293847",
            telefono="945612378",
            correo="jsilva.dev@email.com",
            numero_cuenta="MC-987",
            tipo_cuenta="Corriente",
            saldo=150.20,
            pin="554433",
            banco=banco1
        )
    ]

    for cliente in clientes:
        banco1.agregar_cliente(cliente=cliente)

    #banco1.listar_cliente()
    print(banco1.buscar_cliente("10293847"))