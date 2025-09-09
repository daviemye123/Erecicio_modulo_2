import pytest
from Ejercicio_14 import validar_intento, mostrar_tablero


@pytest.fixture
def letras_adivinadas():
    return ['p', 'y', 't', 'h']


@pytest.fixture
def letras_incorrectas():
    return {'a', 'e', 'o'}


def test_entrada_valida(letras_adivinadas, letras_incorrectas):
    """Prueba que una entrada de una sola letra válida es True."""
    assert validar_intento('c', letras_adivinadas, letras_incorrectas) is True
    assert validar_intento('r', letras_adivinadas, letras_incorrectas) is True


def test_entrada_no_letra():
    """Prueba que la entrada con números o símbolos es False."""
    assert validar_intento('5', [], set()) is False
    assert validar_intento('$', [], set()) is False


def test_entrada_multiple_caracteres():
    """Prueba que una entrada con más de un carácter es False."""
    assert validar_intento('hola', [], set()) is False
    assert validar_intento('ab', [], set()) is False


def test_letra_ya_adivinada(letras_adivinadas, letras_incorrectas):
    """Prueba que una letra que ya ha sido adivinada es False."""
    assert validar_intento('p', letras_adivinadas, letras_incorrectas) is False
    assert validar_intento('y', letras_adivinadas, letras_incorrectas) is False


def test_letra_ya_incorrecta(letras_adivinadas, letras_incorrectas):
    """Prueba que una letra que ya fue incorrecta es False."""
    assert validar_intento('a', letras_adivinadas, letras_incorrectas) is False
    assert validar_intento('e', letras_adivinadas, letras_incorrectas) is False


def test_mostrar_tablero_inicio():
    """Prueba que el tablero se muestra correctamente al inicio del juego."""
    palabra_secreta = "python"
    letras_adivinadas = []
    assert mostrar_tablero(palabra_secreta, letras_adivinadas) == "_ _ _ _ _ _"


def test_mostrar_tablero_progreso():
    """Prueba que el tablero se actualiza correctamente al adivinar letras."""
    palabra_secreta = "python"
    letras_adivinadas = ['p', 'o']
    assert mostrar_tablero(palabra_secreta, letras_adivinadas) == "p _ _ _ o _"


def test_mostrar_tablero_ganado():
    """Prueba que el tablero se muestra completo al adivinar todas las letras."""
    palabra_secreta = "python"
    letras_adivinadas = ['p', 'y', 't', 'h', 'o', 'n']
    assert mostrar_tablero(palabra_secreta, letras_adivinadas) == "p y t h o n"