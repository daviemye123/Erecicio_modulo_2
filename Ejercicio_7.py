def lista():
    """
    Combina dos listas para crear un diccionario de estudiantes.
    Las claves son los nombres y los valores son las notas

    :return:
    no retorna
    """
    estudiante = ["el rosas","elyan","david","el carlos"]
    nota=["3.0","5.0","4.0","5.0"]
    diccionario=dict(zip(estudiante,nota))
    for i,v in diccionario.items():
        print(f"El estudiante {i} tiene nota de ({v})")
if __name__ == "__main__":
    lista()