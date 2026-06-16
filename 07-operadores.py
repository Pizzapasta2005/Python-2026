# Operadores en python 

a = 10 
b = 5
c = 4
d = 10 





print("===OPERADORES ARITMETICOS===")
print(f"La suma entre la variable a y b es: {a + b}") #operador de suma
print(f"la resta entre la variable a y b es: {a - b}") #operador de resta
print(f"La multiplicacion entre la variable a y b es: {a * b}") # operador de producto
print(f"la division entre la variable a y b es: {a/b}") #operacion de division 
print(f"el modulo entre la variable a y b es: {a%b}") #operacion de modulo
print(f"el coeficiente entre la variable b y c es: {b//c}") #operacion de division entera
print(f"el resultado de b elevado a c (5^4): {b**c}") #operacion de potencia -> pow()


# se puede hacer una operacion? 
print("Hola" * (int((10*2) / 5)), "\n")

print("===OPERADORES DE COMPARACION===") #La salida es un booleano (True o False)
print(a==b) #op igualdad
print(a != b) #op desigual, distinto o diferente
print(a > b) #op mayor que
print(a < b) #op menor que
print(c>=d) #op mayor o igual que
print(c<=d) #op menor o igual que

print("===OPERADORES LOGICOS===")
"""Trabajaremos von el siguiente ejemplo:
    Tenemos un vehiculo que tiene bencina (variable bencina) y una opcion
    que dice si esta encendido o no el vehiculo (variable vehiculo).
    Dependiendo del estado de cada variable, se ira cambiando por False o True.
"""
#variables Booleanas

bencina = True
encendido = True
edad = 19

#if = si 
#else = no



# Utilizando el operador AND
if bencina and encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")

# Utilizando el operador Or

if bencina or encendido:
    print("el vehiculo puede arrancar")
else:
    print("El vehiculo nno puede arrancar")


#utilizando el operador NOT junto al AND

if not bencina and encendido:
    print("EL vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")


#Utilizando el operador NOT junto al OR

if not bencina or encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")


#Utilizando el operador NOT junto al operador AND y OR

if (not bencina or encendido) or (encendido and edad >= 18):
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")


