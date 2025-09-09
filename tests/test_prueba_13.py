import pytest
from Ejercicio_13 import manejar_entrada # Asegúrate de que el nombre del módulo sea correcto


def test_mover_norte_desde_entrada():
    """Prueba el movimiento hacia el norte desde la entrada."""
    nueva_habitacion, tiene_llave, juego_terminado, _ = manejar_entrada("entrada", False, "norte")
    assert nueva_habitacion == "pasillo"
    assert tiene_llave is False
    assert juego_terminado is False

def test_abrir_cofre_en_entrada():
    """Prueba la acción de abrir el cofre en la entrada para obtener la llave."""
    nueva_habitacion, tiene_llave, juego_terminado, _ = manejar_entrada("entrada", False, "abrir cofre")
    assert nueva_habitacion == "entrada"
    assert tiene_llave is True
    assert juego_terminado is False

def test_salir_desde_entrada():
    """Prueba la acción de salir del juego desde la entrada."""
    nueva_habitacion, tiene_llave, juego_terminado, _ = manejar_entrada("entrada", False, "salir")
    assert nueva_habitacion == "entrada"
    assert juego_terminado is True

def test_accion_invalida_en_entrada():
    """Prueba una acción no válida en la entrada."""
    nueva_habitacion, tiene_llave, juego_terminado, mensaje = manejar_entrada("entrada", False, "patata")
    assert nueva_habitacion == "entrada"
    assert "no válida" in mensaje
    assert juego_terminado is False


def test_mover_este_desde_pasillo():
    """Prueba el movimiento hacia el este desde el pasillo."""
    nueva_habitacion, _, _, _ = manejar_entrada("pasillo", False, "este")
    assert nueva_habitacion == "sala del tesoro"

def test_mover_sur_desde_pasillo():
    """Prueba el movimiento hacia el sur desde el pasillo."""
    nueva_habitacion, _, _, _ = manejar_entrada("pasillo", False, "sur")
    assert nueva_habitacion == "entrada"


def test_abrir_puerta_con_llave():
    """Prueba la victoria al abrir la puerta con la llave."""
    nueva_habitacion, tiene_llave, juego_terminado, mensaje = manejar_entrada("sala del tesoro", True, "abrir puerta")
    assert juego_terminado is True
    assert "escapado" in mensaje
    assert nueva_habitacion == "sala del tesoro"

def test_abrir_puerta_sin_llave():
    """Prueba el intento de abrir la puerta sin tener la llave."""
    nueva_habitacion, tiene_llave, juego_terminado, mensaje = manejar_entrada("sala del tesoro", False, "abrir puerta")
    assert juego_terminado is False
    assert "Necesitas una llave" in mensaje
    assert nueva_habitacion == "sala del tesoro"

def test_mover_sur_desde_sala_del_tesoro():
    """Prueba el movimiento hacia el sur desde la sala del tesoro."""
    nueva_habitacion, _, _, _ = manejar_entrada("sala del tesoro", False, "sur")
    assert nueva_habitacion == "pasillo"