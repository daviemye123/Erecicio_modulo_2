import pytest
import random
from Ejercicio_12 import simular_lanzamiento_dados  # Replace 'tu_modulo' with your file's name.



@pytest.fixture
def fijar_semilla_aleatoria():
    random.seed(42)


def test_total_lanzamientos(fijar_semilla_aleatoria):
    """
    Verifica que el número total de resultados sea igual al número de lanzamientos.
    """
    num_lanzamientos = 100
    frecuencias = simular_lanzamiento_dados(num_lanzamientos)
    total_lanzamientos = sum(frecuencias.values())
    assert total_lanzamientos == num_lanzamientos


def test_rango_de_sumas(fijar_semilla_aleatoria):
    """
    Verifica que las sumas de los dados estén en el rango de 2 a 12.
    """
    frecuencias = simular_lanzamiento_dados(100)
    sumas = list(frecuencias.keys())
    for suma in sumas:
        assert 2 <= suma <= 12


def test_caso_extremo_un_lanzamiento(fijar_semilla_aleatoria):
    """
    Verifica el comportamiento con solo un lanzamiento.
    """
    num_lanzamientos = 1
    frecuencias = simular_lanzamiento_dados(num_lanzamientos)
    assert len(frecuencias) == 1
    assert sum(frecuencias.values()) == 1


def test_simulacion_con_cero_lanzamientos():
    """
    Verifica que se devuelva un diccionario vacío para 0 lanzamientos.
    """
    num_lanzamientos = 0
    frecuencias = simular_lanzamiento_dados(num_lanzamientos)
    assert frecuencias == {}