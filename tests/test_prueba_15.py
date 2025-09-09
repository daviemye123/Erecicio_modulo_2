import pytest
from Ejercicio_15 import validar_disparo, crear_tablero, colocar_barco


@pytest.fixture
def tablero_5x5():
    return crear_tablero(5, 5)


@pytest.fixture
def disparos_realizados():
    return [(1, 2), (4, 4)]  # Coordenadas de C2 y E5


def test_formato_valido():
    """Prueba que el formato B3 es válido."""
    es_valido, _, _ = validar_disparo("B3", [], 5, 5)
    assert es_valido is True


def test_formato_invalido_longitud():
    """Prueba formatos con longitud incorrecta."""
    es_valido, _, _ = validar_disparo("B", [], 5, 5)
    assert es_valido is False
    es_valido, _, _ = validar_disparo("B33", [], 5, 5)
    assert es_valido is False


def test_formato_invalido_caracteres():
    """Prueba formatos con caracteres no válidos."""
    es_valido, _, _ = validar_disparo("3B", [], 5, 5)
    assert es_valido is False
    es_valido, _, _ = validar_disparo("C#", [], 5, 5)
    assert es_valido is False


def test_coordenadas_dentro_del_tablero():
    """Prueba que las coordenadas A1 y E5 son válidas."""
    es_valido, fila, col = validar_disparo("A1", [], 5, 5)
    assert es_valido is True
    assert (fila, col) == (0, 0)

    es_valido, fila, col = validar_disparo("E5", [], 5, 5)
    assert es_valido is True
    assert (fila, col) == (4, 4)


def test_coordenadas_fuera_del_tablero():
    """Prueba que coordenadas como F6 o A6 son inválidas."""
    es_valido, _, _ = validar_disparo("F6", [], 5, 5)
    assert es_valido is False
    es_valido, _, _ = validar_disparo("A6", [], 5, 5)
    assert es_valido is False


def test_disparo_repetido(disparos_realizados):
    """Prueba un disparo que ya fue realizado (ej. C2)."""
    es_valido, _, _ = validar_disparo("C2", disparos_realizados, 5, 5)
    assert es_valido is False


def test_disparo_no_repetido(disparos_realizados):
    """Prueba un disparo que no ha sido realizado (ej. D4)."""
    es_valido, _, _ = validar_disparo("D4", disparos_realizados, 5, 5)
    assert es_valido is True


def test_crear_tablero(tablero_5x5):
    """Prueba si el tablero se crea correctamente con el tamaño y valor inicial."""
    assert len(tablero_5x5) == 5
    assert len(tablero_5x5[0]) == 5
    assert all(all(celda == '~' for celda in fila) for fila in tablero_5x5)


def test_colocar_barco(tablero_5x5):
    """Prueba que el barco se coloca dentro de los límites y con el tamaño correcto."""
    tamano_barco = 3
    coordenadas = colocar_barco(tablero_5x5, tamano_barco)
    assert len(coordenadas) == tamano_barco

    for fila, col in coordenadas:
        assert 0 <= fila < 5
        assert 0 <= col < 5