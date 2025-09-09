import pytest
from Ejercicio_10 import calcular_transpuesta  # Asegúrate de importar desde el nombre correcto de tu archivo.

def test_transpuesta_matriz_2x3():
    """
    Prueba una matriz de 2x3.
    """
    matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    esperado = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]
    assert calcular_transpuesta(matriz) == esperado

def test_transpuesta_matriz_cuadrada():
    """
    Prueba una matriz de 3x3.
    """
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    esperado = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    assert calcular_transpuesta(matriz) == esperado

def test_transpuesta_matriz_fila():
    """
    Prueba una matriz de 1x4.
    """
    matriz = [[1, 2, 3, 4]]
    esperado = [[1], [2], [3], [4]]
    assert calcular_transpuesta(matriz) == esperado

def test_transpuesta_matriz_columna():
    """
    Prueba una matriz de 4x1.
    """
    matriz = [[1], [2], [3], [4]]
    esperado = [[1, 2, 3, 4]]
    assert calcular_transpuesta(matriz) == esperado

def test_transpuesta_matriz_vacia():
    """
    Prueba que se devuelva una lista vacía si la entrada también está vacía.
    """
    matriz = []
    esperado = []
    assert calcular_transpuesta(matriz) == esperado