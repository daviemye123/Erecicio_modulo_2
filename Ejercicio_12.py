import random

def simular_lanzamiento_dados(num_lanzamientos):
    """
    Simula el lanzamiento de dos dados y cuenta la frecuencia de cada suma.

    Args:
        num_lanzamientos (int): El número de veces que se lanzarán los dados.

    Returns:
        dict: Un diccionario con las sumas como claves y sus frecuencias como valores.
    """
    frecuencias = {}
    for _ in range(num_lanzamientos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        frecuencias[suma] = frecuencias.get(suma, 0) + 1
    return frecuencias

NUM_LANZAMIENTOS = 10000

frecuencias_resultados = simular_lanzamiento_dados(NUM_LANZAMIENTOS)

print(f"--- Frecuencia de las sumas de los dados ({NUM_LANZAMIENTOS} lanzamientos) ---")
for suma in sorted(frecuencias_resultados.keys()):
    frecuencia = frecuencias_resultados[suma]
    print(f"Suma {suma}: {frecuencia} veces")

print("-" * 65)
