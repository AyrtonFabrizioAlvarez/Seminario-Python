import random
import json
import  clases 

archivos = ["datos1.json", "datos2.json", "datos3.json"]

with open(random.choice(archivos), "r") as archivo:
    datos = json.load(archivo)

lista_de_usuarios = []
for usuario in datos:
    objeto_usuario = clases.Usuario(usuario['nombre'], usuario["genero"])
    objeto_usuario.memes = usuario["memes"]
    
    lista_de_usuarios.append(objeto_usuario)

for i in range(len(lista_de_usuarios)):
    print(lista_de_usuarios[i])

print("FIN DEL PROGRAMA")