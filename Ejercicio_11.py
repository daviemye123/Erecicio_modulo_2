def validar_cedula(cedula_str):
    """
    Valida un número de cédula basándose en que la suma de sus dígitos
    sea par.

    Args:
        cedula_str (str): El número de cédula como una cadena de texto.

    Returns:
        bool: True si la suma de los dígitos es par, False en caso contrario.
    """
    suma = 0
    # Bucle 'for' para iterar sobre cada carácter del string 'cedula_str'
    for digito_str in cedula_str:
        suma += int(digito_str)

    return suma % 2 == 0

cedula_valida = False


while not cedula_valida:
    cedula_ingresada = input("Por favor, ingrese su número de cédula: ")


    if cedula_ingresada.isdigit():

        cedula_valida = validar_cedula(cedula_ingresada)

        if cedula_valida:
            print("¡Cédula válida! La suma de sus dígitos es un número par.")
        else:
            print("Cédula inválida. La suma de sus dígitos es impar. Intente de nuevo.")
    else:
        print("Entrada inválida. Por favor, ingrese solo números.")

