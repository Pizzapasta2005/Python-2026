#Solicitamos al usuario ingresar el codigo identificador mediante la terminal

Codigo = input("ingrese el codigo de identificacion")

#Eliminamos los espacios blancos de los extremos usando un metodo de python, en este caso .strip

Codigosinespaciosblancos = Codigo.strip()


#Reemplazamos los guiones bajos por un string vacio utilizando un metodo de python, en este caso .replace
Codigosinguionbajo = Codigosinespaciosblancos.replace("_", "")

#Convertimos todo el texto restante a mayusculas utilizando un metodo de python y luego calculamos el largo de caracteres

Codigoenmayusculas = Codigosinguionbajo.upper()

longitudcaracteres = Codigoenmayusculas.count(Codigoenmayusculas)



#Finalmente desplegamos el codigo limpio y su longitud de caracteres

print("Codigo Identificador final:", Codigoenmayusculas )
print("Longitud de caracteres", longitudcaracteres)