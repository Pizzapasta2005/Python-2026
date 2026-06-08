#Tuplas

estudiantes = ("Matias", "Francisco", "Alan", "Maykol")
print(type(estudiantes))
print(f"TUPLA: (estudiantes)")
#Creando una tupla compleja con datos estructurados
datos = ([1,2,3,4,5], ("Queilen", "Castro"), ("Universidad  de Los Lagos", "AIEP"))

#Tambien se puede consultar la posicion de un elemento al igual que la lista

print(datos[0])
print(f"TUPLA:",datos)

#Con Las listas se puede eliminar elementos
lista_asignaturas = ["Programacion", "Quimica", "Introduccion a las matematicas"]
print(f"LISTA:", (lista_asignaturas))

lista_asignaturas.pop()
print(f"LISTA CON ULTIMO ELEMENTO ELIMINADO: {lista_asignaturas}")

#¿Que pasa si quiero eliminar el ultimo elemento de una tupla?
#Respuesta: como es inmutable no se puede eliminar elementos en una tupla
"""estudiantes.pop()
print(f"TUPLA CON ULTIMO ELEMENTO ELIMINADO: (estudiantes)")"""

#Ocuparemos el metodo index para consultar la posicion de un elemento

print(estudiantes.index('Alan')) #se encuentra en la posicion 2

#Metodo Sorted() para ordenar elementos de una tupla

print(sorted(estudiantes))

#set = conjuntos