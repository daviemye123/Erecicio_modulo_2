def validar_cedula(cedula_str):
    """
    Valida un número de cédula basándose en que la suma de sus dígitos
    sea par.

    Args:
        cedula_str (str): El número de cédula como una cadena de texto.

    Returns:
        bool: True si la suma de los dígitos es par, False en caso contrario.
    """
    if not cedula_str:
        return True

    suma = 0
    for digito_str in cedula_str:
        suma += int(digito_str)

    return suma % 2 == 0

def validar_formato_cedula(cedula_str):
    """
    Valida que la cédula sea una cadena de 10 dígitos.

    Args:
        cedula_str (str): La cédula a validar.

    Returns:
        bool: True si el formato es correcto, False en caso contrario.
    """
    return cedula_str.isdigit() and len(cedula_str) == 10

def solicitar_cedula_al_usuario():
    """
    Gestiona el bucle interactivo para solicitar y validar la cédula.
    """
    while True:
        cedula_ingresada = input("Por favor, ingrese su número de cédula de 10 digitos: ")

        if validar_formato_cedula(cedula_ingresada):
            if validar_cedula(cedula_ingresada):
                print("Cédula válida! La suma de sus dígitos es un número par.")
                break
            else:
                print("Cédula inválida. La suma de sus dígitos es impar. Intente de nuevo.")
        else:
            print("Entrada inválida. Por favor, ingrese exactamente 10 dígitos numéricos.")

if __name__ == "__main__":
    solicitar_cedula_al_usuario()