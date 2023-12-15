# Función que recibe una lista y devuelve otra eliminando sus duplicados (función y pruebas)
def sin_duplicados(lista):
    lista_limpia=[]
    for elem in lista:
        if elem not in lista_limpia:
            lista_limpia.append(elem)
    return lista_limpia
        
        
print (sin_duplicados([1,3,4,3,5,5,2,1,3,2,7,8,5]))

print (sin_duplicados(["verde","azul","gris","azul","rojo","negro","rojo"]))
