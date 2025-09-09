from random import choice


def determinar_ganador(user_choice, computer_choice):
    """
    Determina el resultado de una ronda.
    Devuelve 'ganaste', 'perdiste', 'empate' o 'invalido'.
    """
    opciones = ["piedra", "papel", "tijera"]

    if user_choice not in opciones:
        return 'invalido'

    if user_choice == computer_choice:
        return 'empate'

    if (user_choice == 'piedra' and computer_choice == 'tijera') or \
            (user_choice == 'papel' and computer_choice == 'piedra') or \
            (user_choice == 'tijera' and computer_choice == 'papel'):
        return 'ganaste'
    else:
        return 'perdiste'


def juego():
    """
    Simula un juego de piedra, papel, tijera con interacción del usuario.
    """
    vic = 0
    vicp = 0
    opciones = ["piedra", "papel", "tijera"]

    while vic < 3 and vicp < 3:
        computador = choice(opciones)
        user = input("piedra \n"
                     "papel \n"
                     "tijera \n"
                     "escribir: ").lower()

        resultado = determinar_ganador(user, computador)

        if resultado == 'ganaste':
            vic += 1
            print("ganaste")
        elif resultado == 'perdiste':
            vicp += 1
            print("¡Perdiste!")
        elif resultado == 'empate':
            print("empate")
        elif resultado == 'invalido':
            print("Valor no válido. Por favor, intente de nuevo.")
            continue

        print(f"Marcador: Tú {vic} - {vicp} Computadora")

    if vic == 3:
        print("\n ganaste definitivamente!")
    else:
        print("\n perdiste")


if __name__ == '__main__':
    juego()