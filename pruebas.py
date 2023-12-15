""" def desplaza_elementos(cadena_lista, num):
    #separamos la lista introducida como cadena en elementos usando el separador por defecto " "
    lista = cadena_lista.split()
    #con slice vamos a coger los elementos que hay que mover empezando por la derecha (desplazamiento negativo)
    ultimos = lista[num*(-1):]# cogemos los n último número que han pedido por el final
    primeros = lista[:num*(-1)] # cogemos del primero al n-1 (end no incluído)
    #los devolvemos concatenados a la inversa
    return ultimos + primeros 

#num = int(input('Dime el número de elementos: '))
elementos = input('Dime los elementos de la lista: ')
desplazamiento= int(input('Dime el desplazamiento: '))

print (desplaza_elementos(elementos,desplazamiento))

#coge los n últimos que se hayan pedido
y = x[desplazamiento*(-1):]
#y= x[:desplazamiento]
print(y)
#cogemos desdel el primero hasta el n-1 que han pedido
z = x[:desplazamiento*(-1)]
print(z)
#juntamos lista de nuevo intercambiándolos
print (y+z) """

""" def multiplos(divisor, lista):
    # DONE: completar
    lista_multiplos= []
    for x in range(len(lista)):
        if lista[x]%divisor==0 :
            lista_multiplos.append(lista[x])
    return lista_multiplos

# Para probar
print(multiplos(3, [1,2,3,4,5,6,7,8,9,10])) # Debe mostrar [3, 6, 9]
print(multiplos(5, [1,2,3,4,5,6,7,8,9,10])) # Debe mostrar [5, 10] """

print ("hola"*2)