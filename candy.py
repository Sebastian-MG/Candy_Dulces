# libreria para manejar matrices
# pip install numpy
import numpy as np


def crear_matriz(n_filas):
    # se leen las lineas de entrada
    lista_entrada = [input().split() for i in range(int(n_filas))]
    # se convierten a enteros
    lista_enteros = [[int(elem) for elem in lista] for lista in lista_entrada]
    # se crea la matriz
    matriz = np.array(lista_enteros)
    return matriz

def elegircajas(matriz):
    # logica para escoger las cajas
    # se hallan las dimensiones de la matriz
    dimensiones = matriz.shape
    fila = dimensiones[0]
    columna = dimensiones[1]
    matriz_ceros = np.zeros((fila,2))
    matriz = np.concatenate((matriz_ceros,matriz),axis = 1)
    for i in range(fila):
        for j in range(2,columna + 2):
            matriz[i][j] = max(matriz[i][j-1], matriz[i][j] + matriz[i][j-2])
    dulces_maximos = [0,0]
    for i in range(fila):
        dulces_maximos.append(matriz[i][columna + 1])
    for i in range(2,fila + 2):
        dulces_maximos[i] = max(dulces_maximos[i-1], dulces_maximos[i] + dulces_maximos[i-2])
    return int(dulces_maximos[-1])

def main():
    # filas, columnas de la matriz
    fila, columnas = input().split()
    while (fila and columnas) != "0":
        matriz = crear_matriz(fila)
        dulces = elegircajas(matriz)
        print(dulces)
        fila, columnas = input().split()

main()