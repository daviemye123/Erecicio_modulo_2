def validar_contrasena(user):
    """
    Valida una contraseña basada en varias reglas.

    Args:
        user (str): La contraseña a validar.

    Returns:
        tuple: (True, "Mensaje de éxito") si es válida, o (False, "Mensaje de error") si es inválida.
    """
    if not isinstance(user, str):
        return False, "La entrada no es una cadena de texto."

    if len(user) == 0:
        return False, "La contraseña no puede estar vacía."

    if not any(c.isupper() for c in user):
        return False, "Debe tener al menos una mayúscula."

    if not any(c.islower() for c in user):
        return False, "Debe tener al menos una minúscula."

    if not any(c.isdigit() for c in user):
        return False, "Debe tener al menos un número."

    return True, "Éxito. Contraseña válida."


def contra():
    """
    Función principal que solicita la contraseña al usuario y muestra el resultado.
    """
    while True:
        user = input("Ingresar contraseña: ")
        es_valida, mensaje = validar_contrasena(user)
        print(mensaje)
        if es_valida:
            break


if __name__ == '__main__':
    contra()