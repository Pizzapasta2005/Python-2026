#Guardamos la informacion de la tabla 1 en un diccionario


censo_2017= {
    14: {
        'nombre region' : ('Los Rios'),
        'superficie':(18429),
        'habitantes':(404432)
    },
    12: {
        'nombre region':("Magallanes"),
        'superficie':(1382291),
        'habitantes':(166533)
    }
}
print (censo_2017)
#Utilizando un bucle iteramos los elementos del diccionario calcule de forma automatica

for region in censo_2017.values():
    densidad = region['habitantes']/ region['superficie']

#redondeamos a 1 y lo integramos al sub diccionario 
region['densidad'] = round(densidad, 1)

import pprint
pprint.pprint(censo_2017)