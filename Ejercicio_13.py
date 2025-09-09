def manejar_entrada(habitacion_actual, tiene_llave, accion):
    """
    Procesa la entrada del jugador y actualiza el estado del juego.

    Args:
        habitacion_actual (str): La ubicación actual del jugador.
        tiene_llave (bool): True si el jugador tiene la llave, False en caso contrario.
        accion (str): La acción del jugador (ej. "norte", "abrir cofre").

    Returns:
        tuple: Una tupla con (nueva_habitacion, tiene_llave, juego_terminado, mensaje_salida).
    """
    nueva_habitacion = habitacion_actual
    juego_terminado = False
    mensaje_salida = ""

    if habitacion_actual == "entrada":
        if accion == "norte":
            nueva_habitacion = "pasillo"
        elif accion == "abrir cofre":
            mensaje_salida = "Encuentras una LLAVE oxidada en el cofre. "
            tiene_llave = True
        elif accion == "salir":
            mensaje_salida = "Has decidido abandonar el juego. "
            juego_terminado = True
        else:
            mensaje_salida = "Acción no válida. Inténtalo de nuevo."

    elif habitacion_actual == "pasillo":
        if accion == "este":
            nueva_habitacion = "sala del tesoro"
        elif accion == "sur":
            nueva_habitacion = "entrada"
        elif accion == "salir":
            mensaje_salida = "Has decidido abandonar el juego."
            juego_terminado = True
        else:
            mensaje_salida = "Acción no válida. Inténtalo de nuevo."

    elif habitacion_actual == "sala del tesoro":
        if accion == "abrir puerta":
            if tiene_llave:
                mensaje_salida = "Usas la llave para abrir la puerta! ¡Felicitaciones! ¡Has escapado con el tesoro!"
                juego_terminado = True
            else:
                mensaje_salida = "La puerta está cerrada. Necesitas una llave."
        elif accion == "sur":
            nueva_habitacion = "pasillo"
        elif accion == "salir":
            mensaje_salida = "Has decidido abandonar el juego."
            juego_terminado = True
        else:
            mensaje_salida = "Acción no válida. Inténtalo de nuevo."

    return nueva_habitacion, tiene_llave, juego_terminado, mensaje_salida

def imprimir_mensaje(habitacion_actual):
    """Imprime el mensaje de bienvenida y la descripción de la habitación."""
    print("\nEstás en la habitación de la", habitacion_actual.upper(), "---")
    if habitacion_actual == "entrada":
        print("Hay una puerta al NORTE. También ves un COFRE antiguo en el rincón.")
    elif habitacion_actual == "pasillo":
        print("Estás en un pasillo largo. Ves una puerta pesada al ESTE y una puerta que te lleva de vuelta al SUR.")
    elif habitacion_actual == "sala del tesoro":
        print("Frente a ti hay una puerta de hierro. Es el camino hacia la salida, ¡pero está cerrada!")
        print("La única forma de abrirla es con una llave.")

def jugar_aventura_texto():
    """
    Simula el juego completo de aventuras de texto.
    """
    habitacion_actual = "entrada"
    tiene_llave = False
    juego_terminado = False

    while not juego_terminado:
        imprimir_mensaje(habitacion_actual)
        habitacion_actual, tiene_llave, juego_terminado = manejar_entrada(habitacion_actual, tiene_llave)

if __name__ == "__main__":
    jugar_aventura_texto()