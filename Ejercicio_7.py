def crear_diccionario_estudiantes(estudiantes, notas):
    """
    Combina dos listas para crear un diccionario.

    Args:
        estudiantes (list): Lista de nombres de estudiantes.
        notas (list): Lista de notas correspondientes.

    Returns:
        dict: Un diccionario con los nombres como claves y las notas como valores.
    """
    return dict(zip(estudiantes, notas))


def lista():
    """
    Función principal que usa las funciones de apoyo para crear y mostrar el diccionario.
    """
    estudiante = ["el rosas", "elyan", "david", "el carlos"]
    nota = ["3.0", "5.0", "4.0", "5.0"]

    diccionario = crear_diccionario_estudiantes(estudiante, nota)

    for i, v in diccionario.items():
        print(f"El estudiante {i} tiene nota de ({v})")


if __name__ == "__main__":
    lista()