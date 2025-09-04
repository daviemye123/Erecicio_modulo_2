from random import choice

def juego():
    """
    Simula un juego de piedra, papel, tijera.
    """
    vic = 0
    vicp = 0
    opciones = ["piedra", "papel", "tijera"]
    while vic < 3 and vicp < 3:
        computador = choice(opciones)
        user = (input("piedra \n"
                      "papel \n"
                      "tijera \n"
                      "escribir: ")).lower()
        if user not in opciones:
            print("Valor no válido. Por favor, intente de nuevo.")
            continue
        if computador == user:
            print("empate")
        elif (user == 'piedra' and computador == 'tijera') or \
             (user == 'papel' and computador == 'piedra') or \
             (user == 'tijera' and computador == 'papel'):
            vic += 1
            print("ganaste")
        else:
            vicp += 1
            print("¡Perdiste!")
        print(f"Marcador: Tú {vic} - {vicp} Computadora")
    if vic == 3:
        print("\n ganaste definitivamente!")
    else:
        print("\n perdiste")
if __name__ == '__main__':
    juego()