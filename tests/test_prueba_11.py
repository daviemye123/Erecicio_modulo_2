import pytest
from Ejercicio_11 import validar_cedula, validar_formato_cedula # Asegúrate de importar desde el nombre correcto de tu archivo.

# Pruebas para la función validar_cedula
def test_validar_cedula_suma_par():
    """Prueba una cédula cuya suma de dígitos es par."""
    assert validar_cedula("1234567891") is True  # Suma = 46 (par)

def test_validar_cedula_suma_impar():
    """Prueba una cédula cuya suma de dígitos es impar."""
    assert validar_cedula("1234567890") is False # Suma = 45 (impar)

def test_validar_cedula_cadena_vacia():
    """Prueba una cadena vacía."""
    assert validar_cedula("") is True

def test_validar_cedula_con_cero():
    """Prueba una cédula con todos ceros."""
    assert validar_cedula("0000000000") is True

# Pruebas para la función validar_formato_cedula
def test_validar_formato_longitud_correcta_y_digitos():
    """Prueba que el formato sea de 10 dígitos."""
    assert validar_formato_cedula("1234567890") is True

def test_validar_formato_longitud_incorrecta():
    """Prueba una cédula con menos de 10 dígitos."""
    assert validar_formato_cedula("12345") is False

def test_validar_formato_con_letras():
    """Prueba que no acepte letras."""
    assert validar_formato_cedula("123456789a") is False

def test_validar_formato_con_simbolos():
    """Prueba que no acepte símbolos."""
    assert validar_formato_cedula("123456789-") is False

def test_validar_formato_vacio():
    """Prueba una cadena vacía."""
    assert validar_formato_cedula("") is False