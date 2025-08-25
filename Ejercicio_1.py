listado_clientes = []
precio_actual = {
    "12": 10000,
    "17": 15000,
    "18": 20000
}
def costo():
    """
    Calcula y muestra el precio regular basado en el rango de edad del cliente.
    Esta función presenta un menú para que el usuario seleccione un rango de edad.
    Según la opción elegida, imprime el precio correspondiente del diccionario
    `precio_actual`.
    """
    while True:
        try:
            user_input = int(input(
                "Colocar 1 si la edad es menor de 12\n"
                "Colocar 2 si la edad esta entre 12 y 17\n"
                "Colocar 3 si tiene 18 años en adelante\n"
                "colocar 4 para salir\n"
                "Seleccionar una opcion: "
            ))
            match user_input:
                case 1:
                    print(f"El precio es de ${precio_actual["12"]:.2f}")
                case 2:
                    print(f"El precio es de ${precio_actual["17"]:.2f}")
                case 3:
                    print(f"El precio es de ${precio_actual["18"]:.2f}")
                case 4:
                    print("Saliendo del sistema.")
                    return selec()
                case _:
                    print("Comando no valido. Por favor, ingrese 1, 2, o 3.")
        except ValueError:
            print("Entrada no valida. Por favor, ingrese un numero.")
def costo2():
    """
    Calcula y muestra el precio con descuento para estudiantes.

    Esta función aplica un 10% de descuento sobre el precio regular
    basado en el rango de edad. Presenta un menú similar a `costo()`
    e imprime el precio con el descuento aplicado.
    """
    while True:
        try:
            user_input = int(input(
                "Colocar 1 si la edad es menor de 12\n"
                "Colocar 2 si la edad esta entre 12 y 17\n"
                "Colocar 3 si tiene 18 años en adelante\n"
                "colocar 4 para salir\n"
                "Seleccionar una opcion: "
            ))
            match user_input:
                case 1:
                    descuento = precio_actual["12"] * 0.90
                    print(f"El precio es de ${descuento:.2f}")
                case 2:
                    descuento = precio_actual["17"] * 0.90
                    print(f"El precio es de ${descuento:.2f}")
                case 3:
                    descuento = precio_actual["18"] * 0.90
                    print(f"El precio es de ${descuento:.2f}")
                case 4:
                    print("Saliendo del sistema.")
                    return selec()
                case _:
                    print("Comando no valido. Por favor, ingrese 1, 2, o 3.")
        except ValueError:
            print("Entrada no valida. Por favor, ingrese un numero.")
def actualizar_precio():
    """
    Permite al usuario actualizar los precios en el sistema.

    El usuario puede ingresar nuevos precios para cada una de las
    categorías de edad. Los cambios se guardan en el diccionario
    global `precio_actual` y en la lista `listado_clientes`.
    """
    global listado_clientes
    while True:
        try:
            option = int(input("Ingrese 1 para actualizar precio de menores de 12 años\n"
                               "Ingrese 2 para actualizar precio de entre 12 y 17 años\n"
                               "Ingrese 3 para actualizar precio de 18 años en adelante\n"
                               "Ingrese 4 para salir\n"
                               "Seleccionar una opcion: "))
            match option:
                case 1:
                    new_price = float(input("Ingrese el nuevo precio para menores de 12 años: "))
                    precio_actual["12"] = new_price
                    listado_clientes.append(("Menores de 12 años", new_price))
                    print(f"Precio actualizado a ${new_price:.2f} para menores de 12 años.")
                case 2:
                    new_price = float(input("Ingrese el nuevo precio para entre 12 y 17 años: "))
                    precio_actual["17"] = new_price
                    listado_clientes.append(("Entre 12 y 17 años", new_price))
                    print(f"Precio actualizado a ${new_price:.2f} para entre 12 y 17 años.")
                case 3:
                    new_price = float(input("Ingrese el nuevo precio para 18 años en adelante: "))
                    precio_actual["18"] = new_price
                    listado_clientes.append(("18 años en adelante", new_price))
                    print(f"Precio actualizado a ${new_price:.2f} para 18 años en adelante.")
                case 4:
                    print("Saliendo del sistema de actualización de precios.")
                    return selec()
                case _:
                    print("Comando no valido. Por favor, ingrese 1, 2, o 3.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
def selec():
    """
    Menú principal del sistema de gestión de precios.
    Esta función es el punto de entrada del programa. Permite al usuario
    seleccionar si desea ver los precios regulares, precios de estudiantes,
    actualizar los precios, o salir del programa.
    """
    while True:
        try:
            study = int(input(
                "colocar 1 si no es estudiante\ncolocar 2 si es estudiante\ncolocar 3 para actualizar precios \ncolocar 4 para salir\n selecioonar una opcion: "))
            match study:
                case 1:
                    costo()
                case 2:
                    costo2()
                case 3:
                    actualizar_precio()
                case 4:
                    print("Saliendo del sistema.")
                    return
                case _:
                    print("comando no valido")
                    return
        except ValueError:
            print("Entrada no valida. Por favor, ingrese un numero.")
if __name__ == "__main__":
    selec()