def numero():
    """
    saber si un nuemro es par o divisible por 5
    usadno un try para almencar el codigo y si dijita otro valor no sea valido
    usando replace para los espacios
    :return
    no retorna
    """
    try:

        entrada = input("Ingresa un numero: ")

        entrada_sin_espacios = entrada.replace(" ", "")

        numero = int(entrada_sin_espacios)

        resultado = "par" if numero % 2 == 0 else "impar"

        print(f"El numero {numero} es {resultado}.")

        if numero % 5 == 0:
            print("El numero es divisible por 5.")

    except ValueError:
        print("Entrda no valida.")
if __name__ == "__main__":
    numero()