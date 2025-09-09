import pytest
from Ejercicio_2 import juego

def test_juego_guardado_y_salida(monkeypatch, capsys):

    inputs = iter(['1', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))


    juego()


    captured = capsys.readouterr()

    assert "Guardado correctamente" in captured.out
    assert "saliendo correctamente" in captured.out


    assert "opcion invalida" not in captured.out


def test_juego_opcion_invalida(monkeypatch, capsys):

    inputs = iter(['99', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    juego()

    captured = capsys.readouterr()

    assert "opcion invalida" in captured.out
    assert "saliendo correctamente" in captured.out