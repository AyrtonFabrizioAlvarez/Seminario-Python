import csv

archivo_log = "log_completo.csv" 

def mi_funcion(datos, *args):
    dicci = {}
    for elem in args:
        dicci[elem] = len([x for x in datos if x[1]  == elem ])
    return dicci  

with open(archivo_log, encoding='utf-8') as data_set:
    reader = csv.reader(data_set, delimiter=',')
    encabezado_log, datos_log = next(reader), list(reader)
    
resultado1 = mi_funcion(datos_log, "Rhyhorn")
print(resultado1)

resultado2 = mi_funcion(datos_log, "Hypno", "Butterfree")
print(resultado2)
