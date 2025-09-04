def datos():
    """
    muestra dos lista una con iva y la otra sin iva
    usando datos predeterminados, un for para que haga la operacion con todos lo precios
    usando un pritn para mostra las lisatas
    :return:
    """
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000}
    ]
    pericio={productos["nombre"]:productos["precio"]*0.19 for productos in productos}
    print(f"precion sin iva {productos}")
    print(f"precio con iva es de: {pericio}")
if __name__ == "__main__":
    datos()
