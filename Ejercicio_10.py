def calcular_transpuesta(matriz):
    """
    Calcula la matriz transpuesta de una matriz dada.

    Args:
        matriz (list of lists): La matriz original.

    Returns:
        list of lists: La matriz transpuesta.
    """
    if not matriz or not matriz[0]:
        return []

    # La transpuesta se crea cambiando las filas por las columnas
    transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
    return transpuesta


def matriz():
    """
    Función principal que usa la función de apoyo para transponer y mostrar la matriz.
    """
    matriz_original = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    transpuesta = calcular_transpuesta(matriz_original)
    print(transpuesta)


if __name__ == '__main__':
    matriz()