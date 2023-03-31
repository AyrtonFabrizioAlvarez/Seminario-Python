import string

texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que el de una mujer es de $45.000. Además, las mujeres tienen menos posibilidades de acceder a puestos de liderazgo en las empresas.
  """


separate = texto.split()
print(separate)

qty = 0
upper = []
lower = []
chars = []
for word in separate:
    qty += 1
    for letter in word:
            if letter.isupper():
                upper.append(letter)
            elif letter.islower():
                lower.append(letter)
            else:
                chars.append(letter)
        
       
            

print(f"la cantidad de letras mayusculas es: {upper}")
print(f"la cantidad de letras minusculas es: {lower}")
print(f"la cantidad de letras especiales es: {chars}")
print(f"la cantidad de palabras es: {qty}")
