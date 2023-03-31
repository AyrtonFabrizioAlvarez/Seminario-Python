phrase = input("Ingrese una frase: ")

word = input("Ingrese la palabra que desea contabilizar: ")

reps = phrase.lower().count(word.lower())

print(f"La cantidad de veces que se repitio la palabra es {reps}")