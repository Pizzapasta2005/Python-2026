
Hashable = "Objeto cuyo valor hash nunca cambia y puede ser clave"
Inmutable = "Objeto con valor fijo que no se puede modificar"
Interpretado = "Lenguaje donde el codigo se ejecuta linea a linea"
Iterable = "Objeto capaz de devolver sus elementos uno a la vez"

conceptos_repetidos = ['inmutable', 'iterable', 'inmutable', 'hashable', 'interpretado', 'iterable']

# hacemos el diccionario con las definiciones de cada termino
glosario = {Hashable : "Objeto cuyo valor hash nunca cambia y puede ser clave",
            Inmutable: "Objeto con valor fijo que no se puede modificar",
            Interpretado: "Lenguaje donde el codigo se ejecuta linea a linea",
            Iterable: "Objeto capaz de devolver sus elementos uno a la vez"
            }

input("Por Favor ingrese un concepto a buscar")

Resultado_Busqueda = ()

if Resultado_Busqueda is Hashable:
    print("Definicion", Hashable)
elif Resultado_Busqueda is Inmutable:
        print("Definicion", Inmutable)
elif Resultado_Busqueda is Interpretado:
        print("Definicion", Interpretado)
elif Resultado_Busqueda is Iterable:
        print("Definicion", Iterable)