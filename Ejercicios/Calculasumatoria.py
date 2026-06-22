# Miembros: Leonardo y Maykol


Suma_Total = 0
Termino_A = 500 # con esto sube de 10 en 10  
Termino_B = 456 # se resta de 2 en 2

while Termino_A <= 800:
    #Sumamos el termino que sube (maximo hasta 800)
    Suma_Total += Termino_A

    #He aqui lo mismo pero en vez de suma es resta, con el numero disminuyendo en valor hasta que la suma llegue a 800
    if Termino_A < 800:
        Suma_Total += Termino_B

    Termino_A = Termino_A + 10
    Termino_B = Termino_B - 2
print("El total de la sumatoria es:", Suma_Total)