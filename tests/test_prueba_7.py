import pytest
from Ejercicio_7 import crear_diccionario_estudiantes # Reemplaza 'tu_modulo' con el nombre de tu archivo.

def test_creacion_diccionario_basico():
    """
    Prueba que el diccionario se cree correctamente con datos básicos.
    """
    estudiantes = ["el rosas", "elyan"]
    notas = ["3.0", "5.0"]
    resultado_esperado = {"el rosas": "3.0", "elyan": "5.0"}
    assert crear_diccionario_estudiantes(estudiantes, notas) == resultado_esperado

def test_listas_desordenadas():
    """
    Prueba que el orden de las listas se respete en el diccionario.
    """
    estudiantes = ["david", "el carlos"]
    notas = ["4.0", "5.0"]
    resultado_esperado = {"david": "4.0", "el carlos": "5.0"}
    assert crear_diccionario_estudiantes(estudiantes, notas) == resultado_esperado

def test_listas_con_diferente_longitud():
    """
    Prueba que `zip` maneje listas de diferente longitud correctamente.
    """
    estudiantes = ["elyan", "david", "el carlos"]
    notas = ["5.0", "4.0"] # La lista de notas es más corta
    resultado_esperado = {"elyan": "5.0", "david": "4.0"}
    assert crear_diccionario_estudiantes(estudiantes, notas) == resultado_esperado

def test_listas_vacias():
    """
    Prueba que el diccionario esté vacío si las listas de entrada están vacías.
    """
    estudiantes = []
    notas = []
    resultado_esperado = {}
    assert crear_diccionario_estudiantes(estudiantes, notas) == resultado_esperado