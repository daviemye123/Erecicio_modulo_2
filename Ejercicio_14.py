import random


def mostrar_tablero(palabra_secreta, letras_adivinadas):
    """
    Muestra la palabra con guiones bajos para las letras no adivinadas.
    """
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()


def jugar_ahorcado():
    """
    Función principal para ejecutar el juego del ahorcado.
    """
    palabras = ["python", "programacion", "computadora", "ahorcado", "consola"]
    palabra_secreta = random.choice(palabras).lower()

    letras_adivinadas = []
    letras_incorrectas = set()
    vidas = 6

    print("¡Bienvenido al juego del Ahorcado!")
    print("Tienes que adivinar una palabra secreta. Tienes 6 vidas.")

    while vidas > 0:
        # Mostrar estado del juego
        print("\n" + "=" * 30)
        print(f"Vidas restantes: {vidas}")
        print(f"Letras incorrectas: {' '.join(sorted(list(letras_incorrectas)))}")

        tablero = mostrar_tablero(palabra_secreta, letras_adivinadas)
        print("Palabra: ", tablero)

        # Comprobar si el jugador ha ganado
        if "_" not in tablero:
            print("\n¡Felicidades! ¡Has adivinado la palabra correctamente!")
            print(f"La palabra era: {palabra_secreta}")
            break

        # Pedir una letra al jugador
        intento = input("Ingresa una letra: ").lower()

        # Validar la entrada del jugador
        if len(intento) != 1 or not intento.isalpha():
            print("Entrada inválida. Por favor, ingresa una sola letra.")
        elif intento in letras_adivinadas or intento in letras_incorrectas:
            print("Ya intentaste esa letra. Elige otra.")
        else:
            # Procesar el intento
            if intento in palabra_secreta:
                print("¡Correcto! La letra está en la palabra.")
                letras_adivinadas.append(intento)
            else:
                print("Incorrecto. Pierdes una vida.")
                letras_incorrectas.add(intento)
                vidas -= 1

    if vidas == 0:
        print("\n¡Oh no, te has quedado sin vidas! Has perdido.")
        print(f"La palabra secreta era: {palabra_secreta}")



if __name__ == "__main__":
    jugar_ahorcado()