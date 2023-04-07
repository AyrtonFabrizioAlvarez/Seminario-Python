import os
import ej10

ruta = os.path.dirname(os.path.realpath("."))
print(ruta) 

palabra = "abc"

nuevo = []


for letra in palabra:
    nuevo.append(chr(ord(letra)+1))

listo = ''.join(nuevo)

print(listo)

print(ej10.promNotes([('coco', 2, 3), ('felipe', 3, 4)]))