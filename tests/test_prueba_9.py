import pytest
from Ejercicio_9 import calcular_precios_iva  # Asegúrate de importar desde el nombre correcto de tu archivo.

def test_calculo_iva_precios_base():
    """
    Prueba que los precios con IVA se calculen correctamente para los productos base.
    """
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000}
    ]
    precios_esperados = {
        "Camisa": 59500.0,
        "Pantalón": 95200.0,
        "Zapatos": 142800.0
    }
    assert calcular_precios_iva(productos) == precios_esperados

def test_calculo_iva_un_producto():
    """
    Prueba el cálculo de IVA para un solo producto.
    """
    productos = [{"nombre": "Gorra", "precio": 25000}]
    precios_esperados = {"Gorra": 29750.0}
    assert calcular_precios_iva(productos) == precios_esperados

def test_calculo_iva_lista_vacia():
    """
    Prueba que se devuelva un diccionario vacío si la lista de productos está vacía.
    """
    productos = []
    precios_esperados = {}
    assert calcular_precios_iva(productos) == precios_esperados

def test_calculo_iva_con_cero():
    """
    Prueba que el cálculo funcione correctamente para un precio de 0.
    """
    productos = [{"nombre": "Muestra", "precio": 0}]
    precios_esperados = {"Muestra": 0.0}
    assert calcular_precios_iva(productos) == precios_esperados