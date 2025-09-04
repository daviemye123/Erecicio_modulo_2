def matriz():
    """
    usadno una matriz predeterminada
    hacemos un cambio entre los nuemros, usando un for range para que leyera la matriz
    usando (matriz[0]))] donde i tomara los valores de 0,1y2
    [[fila[i] for fila in matriz] crea una nueva lista para cada valor que este en i
    :return:
    no retorna
    """
    matriz = [
        [1, 2, 3],
        [4, 5, 6]]
    transpuesta = [[fila[i] for fila in matriz]for i in range(len(matriz[0]))]
    print(transpuesta)
if __name__ == '__main__':
    matriz()