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
    pass

def main():
    # filas, columnas de la matriz
    fila, columnas = input().split()
    while (fila and columnas) != "0":
        matriz = crear_matriz(fila)
        dulces = elegircajas(matriz)
        print(dulces)
        fila, columnas = input().split()

main()