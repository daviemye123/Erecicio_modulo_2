def procesar_numero(entrada):
    """
    Procesa un número y determina si es par/impar y divisible por 5.

    Args:
        entrada (str): El número como una cadena de texto.

    Returns:
        str: El mensaje de resultado o de error.
    """
    try:
        entrada_sin_espacios = entrada.replace(" ", "")
        numero = int(entrada_sin_espacios)

        resultado = "par" if numero % 2 == 0 else "impar"

        mensaje = f"El numero {numero} es {resultado}."

        if numero % 5 == 0:
            mensaje += " El numero es divisible por 5."

        return mensaje

    except ValueError:
        return "Entrada no valida."


def numero():
    """
    Función principal que solicita la entrada del usuario y muestra el resultado.
    """
    entrada = input("Ingresa un numero: ")
    print(procesar_numero(entrada))


if __name__ == "__main__":
    numero()