#LISTAS

#primera forma de declaracion de listas
lista1 = ['Victor', 32, True, "Victor", "Victor", "Victor"]
ramos = [] #lista vacia
ramitos = list([])


#segunda forma de declaracion de listas
n = list([1,2,3,4,5])
print(type(n))
print(type(lista1))

#Metodos para las listas
#imprime el primer elemento de la lista1
print(lista1[0])

#01-COUNT()
#Contar la cantidad de concurrencias de un elemento
print(lista1.count('Victor'))

#agregar un elemento al final de la lista

ramos.append('Quimica')

ramos.append('Habilidades Comunicativas')
print(ramos)

ramos.append('Programacion')
print(ramos)