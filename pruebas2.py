""" # Función que recibe una lista y devuelve otra eliminando sus duplicados (función y pruebas)
def sin_duplicados(lista):
    lista_limpia=[]
    for elem in lista:
        if elem not in lista_limpia:
            lista_limpia.append(elem)
    return lista_limpia
        
        
print (sin_duplicados([1,3,4,3,5,5,2,1,3,2,7,8,5]))

print (sin_duplicados(["verde","azul","gris","azul","rojo","negro","rojo"])) """

#Función que recibe una matriz (una lista de listas) y devuelve otra eliminando sus duplicados
# temps = [[1,2,3,4], [5,6,7,8], [5,2,9,10]]
# #
# # The matrix is magically updated here.
# #
# print (temps[1][2])
# lista_limpia =[[]]

# for row in temps:
#     for col in row:
        
#     if row not in lista_limpia:
#         lista_limpia.append(row)

def valores_iguales_matriz(matriz1, matriz2):
    matriz_comparacion= []
    fila_comparacion = []
    for row in range(len(matriz1)):
        for col in range(len(matriz1[row])):
            if matriz1[row][col]==matriz2[row][col]:
                 fila_comparacion.append(1)
            else:
                 fila_comparacion.append(0)
        matriz_comparacion.append(fila_comparacion)
        fila_comparacion=[]
    return matriz_comparacion

# Tests
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3
matriz2 = [[1, 5, 6], [7, 5, 9], [1, 2, 9]] # Matriz 3x3
valores_iguales_matriz(matriz1, matriz2)

print(valores_iguales_matriz(matriz1, matriz2)) # Debería mostrar una matriz identidad
assert valores_iguales_matriz(matriz1, matriz2) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
