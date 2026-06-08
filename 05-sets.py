#SETS (CONJUNTOS)

#Creando los primeros conjuntos
colores_primarios = {'azul', 'rojo', 'amarillo'}
colores_secundarios = set({'naranja','verde', 'violeta'})

print(colores_primarios)
print(colores_secundarios)





#Creando un conjunto nuevo con duplicados
#Respuesta: en los sets no se consideran duplicados

colores_nuevos = {'azul', 'rojo', 'celeste', 'azul', 'rojo'}
print(f"CONJUNTO 3: {colores_nuevos}")

#agregando un nuevo elemento al set colores_nuevos.add()
colores_nuevos.add('cafe')
print(f"CONJUNTO 3 ACTUALIZADO: {colores_nuevos}")








#eliminando un elemento  del set colores nuevos discard()
colores_nuevos.discard('cafe')
print(f"CONJUNTO 3 ACTUALIZADO SIN EL COLOR CAFE: {colores_nuevos}")



#Aplicando el metodo interseccion 

interseccion = colores_primarios.intersection(colores_nuevos)
print(f"CONJUNTO INTERSECTADO: {interseccion}")






