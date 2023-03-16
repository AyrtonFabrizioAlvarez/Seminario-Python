from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print("Desea jugar? 1: SI  - Presione cualquier otra tecla para salir")
ejecutar = input()
while ejecutar == "1":
    print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
    for i in range(0, times):
    # Se eligen números y operador al azar
        number_1 = randrange(10)
        number_2 = randrange(10)
        operator = choice(operators)
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
    incorrectas = 0
    while not acierto:
        if result == x:
            print("El resultado es correcto")
            acierto = True
        else:
            print("El resultado es incorrecto")
            incorrectas += 1
            # Se imprime la cuenta.
            print(f"{i+1}- ¿Volvamos a intentar... ¿Cuánto es {number_1} {operator} {number_2}?")
            # Le pedimos al usuario el resultado
            result = int(input("resultado: "))
    print("Incorrectas: ", incorrectas)
    print("Desea seguir jugando? 1: SI  - Presione cualquier otra tecla para salir")
    ejecutar = input()
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")