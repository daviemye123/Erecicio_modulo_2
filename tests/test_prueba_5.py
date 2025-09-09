import pytest
from Ejercicio_5 import procesar_numero # Make sure to replace your_module_name

def test_numero_par():
    """Test a valid even number."""
    assert procesar_numero("10") == "El numero 10 es par. El numero es divisible por 5."
    assert procesar_numero("  12 ") == "El numero 12 es par."

def test_numero_impar():
    """Test a valid odd number."""
    assert procesar_numero("7") == "El numero 7 es impar."

def test_numero_divisible_por_5():
    """Test a number divisible by 5."""
    assert procesar_numero("25") == "El numero 25 es impar. El numero es divisible por 5."
    assert procesar_numero("  50 ") == "El numero 50 es par. El numero es divisible por 5."

def test_entrada_no_valida():
    """Test invalid input (letters or symbols)."""
    assert procesar_numero("abc") == "Entrada no valida."
    assert procesar_numero("12a") == "Entrada no valida."
    assert procesar_numero("") == "Entrada no valida."
    assert procesar_numero("   ") == "Entrada no valida."
    assert procesar_numero("@") == "Entrada no valida."

def test_flotante_invalido():
    """Test that a float is considered invalid."""
    assert procesar_numero("2.5") == "Entrada no valida."