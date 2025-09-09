import pytest
from Ejercicio_4 import determinar_ganador

def test_ganar_ronda():
    """Prueba todos los casos en los que el usuario gana."""
    assert determinar_ganador('piedra', 'tijera') == 'ganaste'
    assert determinar_ganador('papel', 'piedra') == 'ganaste'
    assert determinar_ganador('tijera', 'papel') == 'ganaste'

def test_perder_ronda():
    """Prueba todos los casos en los que el usuario pierde."""
    assert determinar_ganador('piedra', 'papel') == 'perdiste'
    assert determinar_ganador('papel', 'tijera') == 'perdiste'
    assert determinar_ganador('tijera', 'piedra') == 'perdiste'

def test_empate_ronda():
    """Prueba los casos de empate."""
    assert determinar_ganador('piedra', 'piedra') == 'empate'
    assert determinar_ganador('papel', 'papel') == 'empate'
    assert determinar_ganador('tijera', 'tijera') == 'empate'

def test_eleccion_invalida():
    """Prueba cuando el usuario elige una opción no válida."""
    assert determinar_ganador('spock', 'piedra') == 'invalido'
    assert determinar_ganador('qwerty', 'papel') == 'invalido'