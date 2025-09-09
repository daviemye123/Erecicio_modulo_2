def es_frase_valida(frase):
    """
    Verifica si una frase no contiene números.
    """
    if not frase:
        return False

    for caracter in frase:
        if caracter.isdigit():
            return False
    return True

def encontrar_indices(frase, letra):
    """
    Encuentra todos los índices de una letra en una frase.
    """
    indices_encontrados = []
    for i, caracter in enumerate(frase):
        if caracter == letra:
            indices_encontrados.append(i)
    return indices_encontrados

def obtener_frase_valida():
    """
    Pide al usuario una frase y valida que no contenga números.
    """
    while True:
        frase = input("Escriba una frase (solo letras): ").lower()
        if es_frase_valida(frase):
            return frase
        else:
            print("Entrada no válida. Por favor, ingrese solo letras.")

if __name__ == "__main__":
    frase_valida = obtener_frase_valida()
    letra = "a"
    posiciones = encontrar_indices(frase_valida, letra)
    print(f"Los índices para la letra '{letra}' en la frase '{frase_valida}' son: {posiciones}")