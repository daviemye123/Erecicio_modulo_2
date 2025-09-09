import pytest

from Ejercicio_1 import obtener_precio_base, calcular_precio_final

def test_obtener_precio_base():

    assert obtener_precio_base(5) == 10000
    assert obtener_precio_base(12) == 10000.0


    assert obtener_precio_base(13) == 15000.0
    assert obtener_precio_base(17) == 15000.0


    assert obtener_precio_base(18) == 20000.0
    assert obtener_precio_base(25) == 20000.0

def test_calcular_precio_final():

    precio_adulto = 20000.0
    precio_adolescente = 15000.0


    precio_final_adulto_estudiante = calcular_precio_final(precio_adulto, True)
    assert precio_final_adulto_estudiante == 18000.0


    precio_final_adolescente_no_estudiante = calcular_precio_final(precio_adolescente, False)
    assert precio_final_adolescente_no_estudiante == 15000.0
