


mes = 4 # abril

match mes:
    case 12 | 1 | 2:
        print("Verano")
    case  3 | 4 | 5:
        print("Otoño")
    case 6 | 7 | 8:
        print("Invierno")
    case 9 | 10 | 11:
        print("Primavera")
    case _:
        print("Mes invalido")


# Ejemplo: Saludo segun hora del dia

hora = 18 # formato 24 horas

match hora:
    case h if 0 <= h < 6:
        print("Buenas madrugadas")
    case h if 6 <= h < 12:
        print("Buenos dias")
    case h if 12 <= h <18:
        print("Buenas tardes")
    case h if 18 <= h < 24:
        print("Buenas noches")
    case _:
        print("Hora invalida")




x = [1,2,3]
match x:
    case [a,b,c]:
        print(f"Elementos de la Lista X: {a}, {b}, {c}")

datos = {
    'nombre' : 'Victor',
    'edad' : 31
}


match datos:
    case {'nombre': n, 'edad': e}:
        print(f"Nombre: {n}, Edad: {e}")




#Guards
#Ejemplo: saber si un numero es par o impar

valor = 6 
match valor:
    case x if x % 2 == 0:
        print(f"{valor} es un numero par")
    case x if x % 2 != 0:
        print(f"{valor} es un numero impar")