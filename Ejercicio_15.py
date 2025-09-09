import random

def crear_tablero(filas, columnas):
    """Crea un tablero de 5x5 con '~' para representar agua."""
    return [['~' for _ in range(columnas)] for _ in range(filas)]


def mostrar_tablero(tablero):
    """Imprime el tablero en la consola, incluyendo encabezados de coordenadas."""
    print("  A B C D E")
    for i, fila in enumerate(tablero):
        print(f"{i + 1} {' '.join(fila)}")


def colocar_barco(tablero, tamano_barco):
    """
    Coloca un barco de 3 casillas de forma aleatoria (horizontal o vertical).
    Retorna la lista de coordenadas del barco.
    """
    filas = len(tablero)
    columnas = len(tablero[0])

    orientacion = random.choice(["horizontal", "vertical"])
    coordenadas_barco = []

    if orientacion == "horizontal":
        fila_inicio = random.randint(0, filas - 1)
        col_inicio = random.randint(0, columnas - tamano_barco)
        for i in range(tamano_barco):
            coordenadas_barco.append((fila_inicio, col_inicio + i))
    else:  # Vertical
        fila_inicio = random.randint(0, filas - tamano_barco)
        col_inicio = random.randint(0, columnas - 1)
        for i in range(tamano_barco):
            coordenadas_barco.append((fila_inicio + i, col_inicio))

    return coordenadas_barco


def validar_disparo(disparo_str, disparos_realizados, filas, columnas):
    """
    Valida la entrada del usuario para un disparo.
    Retorna True y las coordenadas si es válido, de lo contrario False.
    """

    if len(disparo_str) != 2 or not disparo_str[0].isalpha() or not disparo_str[1].isdigit():
        return False, None, None

    col_disparo = ord(disparo_str[0].upper()) - ord('A')
    fila_disparo = int(disparo_str[1]) - 1

    if not (0 <= fila_disparo < filas and 0 <= col_disparo < columnas):
        return False, None, None

    if (fila_disparo, col_disparo) in disparos_realizados:
        return False, None, None

    return True, fila_disparo, col_disparo

def batalla_naval():
    """Función principal del juego."""
    filas, columnas = 5, 5
    turnos = 10
    barco_tamano = 3
    tocado_contador = 0

    tablero = crear_tablero(filas, columnas)
    coordenadas_barco = colocar_barco(tablero, barco_tamano)
    disparos_realizados = []

    print("Bienvenido a Batalla Naval. Tienes 10 turnos para hundir el barco.")

    while turnos > 0:
        print("\n" + "=" * 30)
        print(f"Turnos restantes: {turnos}")
        mostrar_tablero(tablero)

        disparo = input("Ingresa las coordenadas de tu disparo (ej. B3): ").upper()

        es_valido, fila_disparo, col_disparo = validar_disparo(disparo, disparos_realizados, filas, columnas)

        if not es_valido:
            print("Entrada inválida. Por favor, intenta de nuevo.")
            continue

        disparos_realizados.append((fila_disparo, col_disparo))

        if (fila_disparo, col_disparo) in coordenadas_barco:
            print("¡Tocado!")
            tablero[fila_disparo][col_disparo] = 'X'
            tocado_contador += 1
            if tocado_contador == barco_tamano:
                print("\n¡Felicitaciones! ¡Has hundido el barco y ganado el juego!")
                mostrar_tablero(tablero)
                break
        else:
            print("¡Agua!")
            tablero[fila_disparo][col_disparo] = 'O'

        turnos -= 1

    if turnos == 0 and tocado_contador < barco_tamano:
        print("\n¡Te has quedado sin turnos! Has perdido.")
        print("La ubicación del barco era:")
        for r, c in coordenadas_barco:
            tablero[r][c] = '*'
        mostrar_tablero(tablero)

if __name__ == "__main__":
    batalla_naval()