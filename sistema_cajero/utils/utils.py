from decimal import Decimal

def limpiar_string(texto: str) -> str:
    if not texto:
        return ""
    
    return texto.strip()

def validar_decimales(numero: float) -> Decimal:
    if not isinstance(numero, (float, int)):
        raise ValueError("El tipo de dato es incorrecto. Debe ser un número.")
    
    if numero <= 0:
        raise ValueError("El numero debe ser mayor igual a 0")
    
    return Decimal(str(numero))