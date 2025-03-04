texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que el de una mujer es de $45.000. Además, las mujeres tienen menos posibilidades de acceder a puestos de liderazgo en las empresas.
  """


separate = texto.split()


upper = [letter for word in separate for letter in word if letter.isupper()]
lower = [letter for word in separate for letter in word if letter.islower()]
chars = [letter for word in separate for letter in word if not(letter.isalpha())]

            
print(upper)
print(f"la cantidad de letras mayusculas es: {len(upper)}\n")
print(lower)
print(f"la cantidad de letras minusculas es: {len(lower)}\n")
print(chars)
print(f"la cantidad de letras especiales es: {len(chars)}\n")
print(f"la cantidad de palabras es: {len(separate)}")
