def jugar_aventura_texto():
    """
    usando el bucle while, tuplas y elecciones para validar las opciones del jugador
    :return
    no retorna
    """
    habitacion_actual = "entrada"
    tiene_llave = False
    juego_terminado = False

    while not juego_terminado:
        print("\nEstás en la habitación de la", habitacion_actual.upper(), "---")
        if habitacion_actual == "entrada":
            print("Hay una puerta al NORTE. También ves un COFRE antiguo en el rincón.")
            accion = input("¿Qué quieres hacer? (norte / abrir cofre / salir): ").lower()

            if accion == "norte":
                habitacion_actual = "pasillo"
            elif accion == "abrir cofre":
                print("Encuentras una LLAVE oxidada en el cofre. ")
                tiene_llave = True
            elif accion == "salir":
                print("Has decidido abandonar el juego. ")
                juego_terminado = True
            else:
                print("Acción no válida. Inténtalo de nuevo.")

        elif habitacion_actual == "pasillo":
            print("Estás en un pasillo largo. Ves una puerta pesada al ESTE y una puerta que te lleva de vuelta al SUR.")
            accion = input("¿Qué quieres hacer? (este / sur / salir): ").lower()

            if accion == "este":
                habitacion_actual = "sala del tesoro"
            elif accion == "sur":
                habitacion_actual = "entrada"
            elif accion == "salir":
                print("Has decidido abandonar el juego.")
                juego_terminado = True
            else:
                print("Acción no válida. Inténtalo de nuevo.")

        elif habitacion_actual == "sala del tesoro":
            print("Frente a ti hay una puerta de hierro. Es el camino hacia la salida, ¡pero está cerrada!")
            print("La única forma de abrirla es con una llave.")
            accion = input("¿Qué quieres hacer? (abrir puerta / sur / salir): ").lower()

            if accion == "abrir puerta":
                if tiene_llave:
                    print("¡Usas la llave para abrir la puerta! ¡Felicitaciones! ¡Has escapado con el tesoro!")
                    juego_terminado = True
                else:
                    print("La puerta está cerrada. Necesitas una llave.")
            elif accion == "sur":
                habitacion_actual = "pasillo"
            elif accion == "salir":
                print("Has decidido abandonar el juego.")
                juego_terminado = True
            else:
                print("Acción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    jugar_aventura_texto()