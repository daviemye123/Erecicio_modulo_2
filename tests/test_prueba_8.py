import pytest
from Ejercicio_8 import create_lists  # Make sure to import from the correct file name.

def test_listas_con_numeros_mixtos():
    """
    Prueba con una lista que tiene números positivos y negativos.
    """
    numeros = [-5, 10, -15, 20, -25, 30]
    positivos, cuadrados, tipos = create_lists(numeros)

    assert positivos == [10, 20, 30]
    assert cuadrados == [25, 100, 225, 400, 625, 900]
    assert tipos == ["negativo", "positivo", "negativo", "positivo", "negativo", "positivo"]

def test_listas_solo_negativos():
    """
    Prueba con una lista que solo tiene números negativos.
    """
    numeros = [-1, -2, -3]
    positivos, cuadrados, tipos = create_lists(numeros)

    assert positivos == []
    assert cuadrados == [1, 4, 9]
    assert tipos == ["negativo", "negativo", "negativo"]

def test_listas_vacias():
    """
    Prueba con una lista de entrada vacía.
    """
    numeros = []
    positivos, cuadrados, tipos = create_lists(numeros)

    assert positivos == []
    assert cuadrados == []
    assert tipos == []

def test_listas_con_cero():
    """
    Prueba que el número cero se maneje correctamente (no es positivo).
    """
    numeros = [0, 5, -5]
    positivos, cuadrados, tipos = create_lists(numeros)

    assert positivos == [5]
    assert cuadrados == [0, 25, 25]
    assert tipos == ["negativo", "positivo", "negativo"]