from colorama import init, Fore
init() #inicializando el siguiente colorama

print(Fore.YELLOW + '===== BUCLES =====')

#Bucle While
edad = 15 
num = 0 

#Bucle infinito
#while edad < 18
# print ('eres menor de edad, no puedes manejar)
#impresion de numeros 
while True:
    print(num)
    num = num + 2
print(Fore.RED + "Primer Bucle Terminado!")

#Impresion de numeros de 100 a 200 + Condicion ELSE

while num >= 200:
    print(num)
    num += 2
else:
    print("Mi condicion es igual o mayor a 200")
print(Fore.CYAN + "Segundo Bucle Terminado!")

# Combinar While con un if dentro
while num <= 300:
    print(num)
    num += 2
    if num == 250:
        print("Mi condicion es igual a 250")
print(Fore.GREEN + "Tercer Buvle Terminado!")

#siempre poner python [nombre del archivo]
#RECOMENDABLE ejecutar desde [open integrated terminal]

#utilizando el break
while num <= 400:
    print(num)
    num += 2
    if num == 350:
        print(Fore.MAGENTA + "Se detiene el bucle")
        break #Break rompe el ciclo 
print(num)
print(Fore.MAGENTA + "Cuarto Bucle Terminado!")

#utilizar el continue

num = 0
while num <= 50:
    num += 1
    if num == 40:
        continue
    print(num)
print(num)


#bucle infinito + break

while True:
    parametro = input(">")
    if parametro == "exit":
        break
    else:
        print(parametro)


# BUCLE FOR
# For N1
print(Fore.GREEN + "===== BUCLES FOR =====")
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)
print(Fore.CYAN + "\n2° Bucle for")
#iterando una lista
listita = [1,2,3,4,5,6,7,8,9,10]

for i in listita:
    print(i)
print(Fore.MAGENTA + "\n3° Bucle For")

#iterando de una tercer forma (3° for)

for i in range(1,11):
    print(i)

#range es el metodo de rango