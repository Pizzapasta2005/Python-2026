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