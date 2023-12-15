""" # Función que recibe una lista y devuelve otra eliminando sus duplicados (función y pruebas)
def sin_duplicados(lista):
    lista_limpia=[]
    for elem in lista:
        if elem not in lista_limpia:
            lista_limpia.append(elem)
    return lista_limpia
        
        
print (sin_duplicados([1,3,4,3,5,5,2,1,3,2,7,8,5]))

print (sin_duplicados(["verde","azul","gris","azul","rojo","negro","rojo"])) """

# #Función que recibe una matriz (una lista de listas) y devuelve otra eliminando sus duplicados
# lista = [[1,2,3], [4,1,5], [1,2,3], [5,2,9]]
# # # #
# # # # The matrix is magically updated here.
# # # #
# # # print (temps[1][2])
# lista_nueva =[]
# matriz_nueva =[]
# for row in range(len(lista)):
#     for elem in range(lista[row]): #sacamos los elementos de la lista y tenemos que compararlos con los elementos de la nueva mía
#         for row_nueva in range(len(matriz_nueva)): #tendremos que recorrer todos los elementos de mi nueva matriz
#             if elem not in row_nueva: #recorremos toda nuestra nueva matriz

#         lista_nueva.append(elem)
#     matriz_nueva.append(lista_nueva)


# print(lista_nueva)


# temps = [[1,2,3], [5,7], [1], [5,2,9]]
# print (temps)

# Función que recibe dos matrices cuadradas (NxN) y devuelve una tercera matriz que contiene el valor 1 en las posiciones en que el valor de A y B coinciden y 0 en caso contrario.
# def valores_iguales_matriz(matriz1, matriz2):
#     matriz_comparacion= []
#     fila_comparacion = []
#     for row in range(len(matriz1)):
#         for col in range(len(matriz1[row])):
#             if matriz1[row][col]==matriz2[row][col]:
#                  fila_comparacion.append(1)
#             else:
#                  fila_comparacion.append(0)
#         matriz_comparacion.append(fila_comparacion)
#         fila_comparacion=[]
#     return matriz_comparacion

# # Tests
# matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3
# matriz2 = [[1, 5, 6], [7, 5, 9], [1, 2, 9]] # Matriz 3x3
# valores_iguales_matriz(matriz1, matriz2)

# print(valores_iguales_matriz(matriz1, matriz2)) # Debería mostrar una matriz identidad
# assert valores_iguales_matriz(matriz1, matriz2) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Función que recibe una lista y devuelve un diccionario con el número de veces que aparece cada elemento (las claves del diccionario deben 
# ser los elementos de la lista y los valores deben ser el número de veces que aparece dicho elemento en la lista)

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# words = ['cat', 'lion', 'horse']

# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "is not in dictionary")

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# for key in dictionary.keys():
#     print(key, "->", dictionary[key]


lista = [1,2,4,5,6,7,2,3,3,4,4]
diccionario = {}
for elem in lista:
    if elem in diccionario:
        diccionario[elem]+=1
    else:
        diccionario[elem]=1
        
print (diccionario)
    
    