import pytest
from Ejercicio_3 import validar_contrasena  # Replace 'your_module' with the name of your file

def test_contrasena_valida():
    """Prueba una contraseña que cumple con todas las reglas."""
    es_valida, mensaje = validar_contrasena("Contrasena1")
    assert es_valida is True
    assert "Éxito" in mensaje

def test_contrasena_sin_mayuscula():
    """Prueba una contraseña sin mayúsculas."""
    es_valida, mensaje = validar_contrasena("contrasena1")
    assert es_valida is False
    assert "mayúscula" in mensaje

def test_contrasena_sin_minuscula():
    """Prueba una contraseña sin minúsculas."""
    es_valida, mensaje = validar_contrasena("CONTRASENA1")
    assert es_valida is False
    assert "minúscula" in mensaje

def test_contrasena_sin_numero():
    """Prueba una contraseña sin números."""
    es_valida, mensaje = validar_contrasena("Contrasena")
    assert es_valida is False
    assert "número" in mensaje

def test_contrasena_vacia():
    """Prueba una contraseña vacía."""
    es_valida, mensaje = validar_contrasena("")
    assert es_valida is False
    assert "vacía" in mensaje