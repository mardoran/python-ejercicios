""" # Función que recibe una lista y devuelve otra eliminando sus duplicados (función y pruebas)
def sin_duplicados(lista):
    lista_limpia=[]
    for elem in lista:
        if elem not in lista_limpia:
            lista_limpia.append(elem)
    return lista_limpia
        
        
print (sin_duplicados([1,3,4,3,5,5,2,1,3,2,7,8,5]))

print (sin_duplicados(["verde","azul","gris","azul","rojo","negro","rojo"])) """

# Method : Using loop This task can be performed in brute force manner using loops. 
# In this, we just iterate the list of list using loop and check for the already presence of element, 
# and append in case it’s new element, and construct a non-duplicate matrix. 

# #Función que recibe una matriz (una lista de listas) y devuelve otra eliminando sus duplicados
# initialize list 
matriz = [[5, 6, 8], [8, 5, 3], [9, 10, 3]]
 
 
 
# printing original list
print("The original list is : " + str(matriz))
 
# Removing duplicates in Matrix
# using loop
matriz_sin_duplicar = []
lista_compare = [] #declaramos una list para almacenar en paralelo todos los elementos de nuestra matriz resultante y que así sea más sencillo comparar
index = 0 #necesitamos una variable para saber las filas que vamos insertando en nuestra matriz resultante

for lista in matriz: #nos quedamos con cada fila de la matriz
    matriz_sin_duplicar.append([]); # por cada fila de la matriz añadiremos una lista vacía a nuestra matriz a devolver
    for elem in lista: #por cada elemento de la fila de la matriz original
        
        #la idea será a la vez que ir creando nuestra matriz con los elementos por cada fila de la original
        #ir metiendo en una lista sencilla esos mismos elementos, de modo que comparemos con la lista sencilla si ya están
        #en lugar de con nuestra matriz
        
        if elem not in lista_compare:
            matriz_sin_duplicar[index].append(elem)
            lista_compare.append(elem)
    index += 1
 
# printing result
print("The Matrix after duplicates removal is : " + str(matriz_sin_duplicar))


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


# lista = [1,2,4,5,6,7,2,3,3,4,4]
# diccionario = {}
# for elem in lista:
#     if elem in diccionario:
#         diccionario[elem]+=1
#     else:
#         diccionario[elem]=1
        
# print (diccionario)
    
    