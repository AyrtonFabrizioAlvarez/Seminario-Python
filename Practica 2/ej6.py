word = input("Ingresa una palabra: ")

match 'a' in word, 'n' in word :
    case True, True:
        print(f"La palabra {word} tiene letras 'a' y 'n'")
    case True, _:
        print(f"La palabra {word} tiene letra 'a'")
    case _, True:
        print(f"La palabra {word} tiene letra 'n'")
    case _:
        print(f"La palabra {word} no tiene letras 'a' ni 'n'")