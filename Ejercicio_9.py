def calcular_precios_iva(productos):
    """
    Calcula el precio de los productos aplicando el 19% de IVA.

    Args:
        productos (list): Una lista de diccionarios con el nombre y precio de cada producto.

    Returns:
        dict: Un diccionario con los nombres de los productos como claves y sus precios con IVA como valores.
    """
    return {item["nombre"]: round(item["precio"] * 1.19, 2) for item in productos}

def datos():
    """
    Muestra los precios de los productos con y sin IVA.
    """
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000}
    ]
    precios_con_iva = calcular_precios_iva(productos)

    print(f"Precios sin IVA: {productos}")
    print(f"Precios con IVA: {precios_con_iva}")


if __name__ == "__main__":
    datos()