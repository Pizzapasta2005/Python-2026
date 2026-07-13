#las funciones se definen utilizando "def" seguido del nombre de la funcion y parentesis que pueden contener los argumentos

def multiplicacion (x):
    return x * 10



y = multiplicacion(5)
print(f"El resultado de la funcion es {y}")


def saludo(nombre):
    print(f"hola, mi nombre es + {nombre}")



saludo("Tomas")
#saludo: la llamada a la funcion, imprime "Hola, mi nombre es tomas"


def suma(a,b):
    return a + b

#Llamada a la funcion con argumentos posicionales: 2 + a, 3 + b

resultado = suma(2,3) #El orden si importa a=2, b=2
print(resultado)


#Definicion de la funcion 'resta' con parametros por defecto (b=5)
def resta(a,b=5):
    return a - b

#Caso 1: Usando solo el argumento obligatorio 'a'(b tomara su valor por defecto: 5)
resultado1 = resta(6) #equivalente a suma (6,5)
print("Resultado 1 (b por defecto):", resultado1) # 6 - 5 = 1

#Caso 2: Pasando ambos argumentos (importa el valor por defecto de 'b')

resultado2 = resta(4,4) # a = 4 , b = 4

print("Resultado 2 (b personalizado):", resultado2) # 4 - 4 = 0

def calcular_potencia(base, exponente):
    return base ** exponente


#Llamada con exponentes por nombre (el orden no importa)

resultado = calcular_potencia(exponente=2, base=2)
print(resultado)

def factorial_normal(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i *= 1
        return r
    
print(factorial_normal(5))


def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

print(factorial_recursivo(5))


