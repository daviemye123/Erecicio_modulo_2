def obtener_precio_base(edad: int) -> float:
    """
    Calcula el precio base de la entrada de cine según la edad del cliente.

    Args:
      edad del cliente de manera entera

    Returns:
       precio de la entrada
    """
    if edad <= 0:
        raise ValueError("No puedes ingresar una edad menor o igual a cero.")
    elif edad <= 12:
        return 10000.0
    elif 12 < edad < 18:
        return 15000.0
    else:
        return 20000.0

def calcular_precio_final(precio_base: float, es_estudiante: bool) -> float:
    """
    Calcula el precio final de la entrada aplicando el descuento del estudiante.

    Args:
        precio_base (float): siendo el precio  sin descuento.
        es_estudiante (bool): valida si es estudiante o no .

    Returns:
        float: El precio final de la entrada con el descuento aplicado.
    """
    if es_estudiante:
        descuento = precio_base * 0.10
        print(f"Tienes un descuento de ${descuento:,.2f}.")
        return precio_base - descuento
    else:
        return precio_base


def gestionar_compra_entradas():
    """
    Gestiona el flujo de compra de entradas de cine, solicitando datos al usuario
    y mostrando el precio final.
    """
    try:
        edad= int(input("indica tu edad: "))

        respuesta_estudiante = input("¿Eres estudiante? (s/n): ").lower()
        es_estudiante = respuesta_estudiante == 's'

        precio_base = obtener_precio_base(edad)
        precio_final = calcular_precio_final(precio_base, es_estudiante)

        print(f"El valor de tu entrada es: ${precio_final:,.2f}.")
    except ValueError :
        print("Error valor no valido")
    except Exception :
        print("Ocurrió un error inesperado")

if __name__ == "__main__":
    gestionar_compra_entradas()