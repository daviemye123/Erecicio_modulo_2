def encontrar_indices(frase, letra):
    """
    le pide al usuario digitar una frase
    usando un for para repetir el ciclo y poder leer la frese escrita con la variabel i
    :return
    la frase
    Returns:

    """
    indices_encontrados = []
    for i, caracter in enumerate(frase):
        if caracter == letra:
            indices_encontrados.append(i)
    return indices_encontrados
frase = input("Escriba una frase: ").lower()
letra = "a"
posiciones = encontrar_indices(frase, letra)
print(f"Los índices para la letra '{letra}' en la frase '{frase}' son: {posiciones}")
if __name__ == "__main__":
    encontrar_indices(frase, letra)