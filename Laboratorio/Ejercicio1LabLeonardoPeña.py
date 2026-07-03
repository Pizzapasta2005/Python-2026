#Primero solicitamos al usuario ingresar por terminal  una a  una las precipitaciones de las 5 muestras meteorologicas, los datos deben ser guardados como float

Precipitacion1 = input("Ingrese el numero de precipitacion de la muestra 1")

Precipitacion2 = input("Ingrese el numero de precipitacion de la muestra 2")

Precipitacion3 = input("Ingrese el numero de precipitacion de la muestra 3")

Precipitacion4 = input("Ingrese el numero de precipitacion de la muestra 4")

Precipitacion5 = input("Ingrese el numero de precipitacion de la muestra 5")

#los guardamos como decimales Float

Muestra1 = float(Precipitacion1,)

Muestra2 = float(Precipitacion2, )

Muestra3 = float(Precipitacion3, )

Muestra4 = float(Precipitacion4, )

Muestra5 = float(Precipitacion5, )

#almacenamos los 5 valores en una lista

registro_lluvia = (Muestra1, Muestra2, Muestra3, Muestra4, Muestra5)

#Accedemos a los elementos de la lista mediante sus indices fijos para calcular el promedio de precipitaciones caidas durante el evento

Sumapresipitaciones = Muestra1 + Muestra2 + Muestra3 + Muestra4 + Muestra5
promedioprecipitaciones = Sumapresipitaciones / 5

#identificamos el registro mas bajo y el mas alto y calculamos la brecha pluvial restando el valor maximo y minimo

brechapluvial = max(registro_lluvia) - min(registro_lluvia)

#por ultimo imprimimos la lista, el promedio y brecha pluvial
print("registro de lluvia", registro_lluvia)
print("Promedio de Precipitaciones:", promedioprecipitaciones)
print("Brecha Pluvial:", brechapluvial)

