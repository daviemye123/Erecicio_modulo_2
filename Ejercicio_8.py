def create_lists(numeros):
    """
    Crea varias listas a partir de una lista de números.

    Args:
        numeros (list): La lista de números de entrada.

    Returns:
        tuple: Una tupla que contiene (positivos, cuadrados, tipos).
    """
    positivos = [i for i in numeros if i > 0]
    cuadrados = [i ** 2 for i in numeros]
    tipos = ["positivo" if i > 0 else "negativo" for i in numeros]
    return positivos, cuadrados, tipos


def listCompregenshion():
    """
    Función principal que usa las funciones de apoyo para crear y mostrar las listas.
    """
    numeros = [-5, 10, -15, 20, -25, 30]
    positivos, cuadrados, tipos = create_lists(numeros)

    print(f"La lista de números positivos es: {positivos}")
    print(f"La lista de cuadrados es: {cuadrados}")
    print(f"La clasificación de los números es: {tipos}")


if __name__ == "__main__":
    listCompregenshion()