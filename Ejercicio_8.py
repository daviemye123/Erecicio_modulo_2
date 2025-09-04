def listCompregenshion():
    """Crea varias listas a partir de una lista de números usando
    list comprehensions.
    :return:
    no retorna
    """
    numeros = [-5, 10, -15, 20, -25, 30]
    positivos = [i for i in numeros if i > 0]
    print(f"La lista de números positivos es: {positivos}")
    cuadrados = [i ** 2 for i in numeros]
    print(f"La lista de cuadrados es: {cuadrados}")
    tipos = ["positivo" if i > 0 else "negativo" for i in numeros]
    print(f"La clasificación de los números es: {tipos}")
if __name__ == "__main__":
    listCompregenshion()