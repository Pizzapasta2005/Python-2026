#Datos numericos

#Numeros Enteros

edad = 32
annio_nacimiento = 1993





#numeros foltantes (Reales)
estatura = 1.75 # el decimal se utiliza punto y no coma

#  Numeros complejos
num_complejo = 4 + 2j  #primera forma de crear un numero complejo
otro_complejo = complex(4,2) # segunda forma de crear un numero complejo

print (num_complejo)
print (otro_complejo)
PI= 3.14159
base = 8
altura = 12.52

area= (base * altura) / 2

print(f"el area del triangulo es de {area} cm")



# formato de salida de numeros


# salida del numero PI con 4 decimales
print(f"El numero PI tiene un valor de {PI:.4f}")

#el metodo de redondeo
print(round(PI, 3))
print(f"El area del triangulo es de {round(area)}cm")


#transformaciones

print(float(edad))


#Cadenas de texto (strings)

carrera = "ingenieria Civil en Informatica"
institucion = "Universidad de Los Lagos"

print (carrera[0]) #se imprime la primera letra
print (carrera[0]) #se imprime la ultima letra
print( "hola" * 4) #multiplicacion de un string por un entero

print(carrera [0:10]) #obteniendo una sub cadena (cortando strings)


#arreglos (listas)
print("------- ARREGLOS (LISTAS) -------")
colores = ["Azul", "Rojo", "Verde", "Amarillo"] # Arreglo de Strings
numeros = [1,2,3,4,5,6] # Arreglo Numerico 
lista_Mixta = ["Gato", 2, 67.0, True]
print(colores[0])
print(numeros[0])


luz_electrica = True
interruptor = False 



print("-------BOOLEANOS--------")
print(luz_electrica)
print(interruptor)


print(f"El tipo de dato es {type(carrera)}")