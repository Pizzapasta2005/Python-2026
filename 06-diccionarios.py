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