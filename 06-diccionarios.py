# Diccionarios

paciente = {
    'nombre':'benjamin bahamonde', #el : va afuera de los '' no dentro
    'edad' : 18,
    'ciudad' : 'ancud',
    'fechas_atencion': [5,8,12],
    'diagnostico' : ('resfrio comun')
}
#tambien se puede hacer en una linea pero no es recomendable pues se puede confundir con un set
print(type(paciente))
print(f"===== FICHA PACIENTE ===== \n{paciente}")













medico = "lol"






#con clear () elimina todos los elementos del diccionario, dejandolo vacio
medico2 = medico.copy()
print("\n===== DICCIONARIO COPIA (MEDICO2) ====== \n")
print(medico2)
medico2.clear()
print(medico2) # -> {}

#Metodos para datos iterables
print("\nMETODOS PARA DATOS ITERABLES")
a = [1,2,3,4,5]
b = ["A", "B", "C", "D"]

comprimir = list(zip(a,b))
print(comprimir)


