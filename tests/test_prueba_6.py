import pytest
from Ejercicio_6 import encontrar_indices, es_frase_valida  # Asegúrate de importar desde el nombre de tu archivo.


def test_encontrar_indices_letra_existente():
    """Prueba encontrar índices de una letra que aparece varias veces."""
    frase = "banana"
    letra = "a"
    assert encontrar_indices(frase, letra) == [1, 3, 5]


def test_encontrar_indices_letra_no_existente():
    """Prueba con una letra que no está en la frase."""
    frase = "manzana"
    letra = "x"
    assert encontrar_indices(frase, letra) == []


def test_es_frase_valida_correcta():
    """Prueba una frase que solo contiene letras y espacios."""
    assert es_frase_valida("hola mundo") is True
    assert es_frase_valida("programacion") is True


def test_es_frase_valida_con_numeros():
    """Prueba una frase con números, que debería ser inválida."""
    assert es_frase_valida("frase123") is False
    assert es_frase_valida("12345") is False


def test_es_frase_valida_con_simbolos():
    """Prueba una frase con símbolos. La función solo valida que no haya dígitos."""
    assert es_frase_valida("hola-mundo!") is True


def test_es_frase_valida_cadena_vacia():
    """Prueba una cadena vacía, que debe ser inválida."""
    assert es_frase_valida("") is False