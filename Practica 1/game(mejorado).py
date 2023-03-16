from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
correctas = 0
incorrectas = 0
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    while operator == "/" and number_2 == 0:
        number_2 = randrange(10)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = int(input("resultado: "))
    match operator:
        case "+":
            x = (number_1 + number_2)
        case "-":
            x = (number_1 - number_2)
        case "*":
            x = (number_1 * number_2)
        case "/":
            x = (number_1 // number_2)
    acierto = False
    while not acierto:
        if result == x:
            print("El resultado es correcto")
            acierto = True
            correctas += 1
        else:
            print("El resultado es incorrecto")
            incorrectas += 1
            # Se imprime la cuenta.
            print(f"{i+1}- ¿Volvamos a intentar... ¿Cuánto es {number_1} {operator} {number_2}?")
            # Le pedimos al usuario el resultado
            result = int(input("resultado: "))
print("Correctas: ", correctas)
print("Incorrectas: ", incorrectas)


# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")