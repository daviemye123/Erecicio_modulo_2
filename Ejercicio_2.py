def juego(user_input=int):
    """
    en la clase de juego user es donde se almacenan el menu para la selecion del usuario
    con match seleciona opcion
    mostrandola como mensaje
    :return:
    case 1
    case 2
    case 3
    """
    while True:
        try:
            user_input = int(input("Ingresar 1 para guardar\n"
                                   "Ingresar 2 para cargar\n"
                                   "Ingresar 3 para ssalir\n"
                                   "Ingresar opcion: "

            ))
            match user_input:
                case 1:
                    print("Guardado correctamente")
                case 2:
                    print("Cargado correctamente")
                case 3:
                    print("saliendo correctamente")
                    break
                case _:
                    print("opcion invalida")
        except ValueError:
            print("opcion invalida")
if __name__ == "__main__":
    juego()