names = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás',  'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notes_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 
           13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 
           74, 60, 9, 65, 93, 63, 74]
notes_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8,
           87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31,
           39, 15, 74, 33, 57, 10]

#INCISO 1
def generateZip(names, notes_1, notes_2):
    fixedText = names.replace('\n','').replace(' ', '').replace("'", '').split(',')
    return {name: (note1, note2) for name, note1, note2 in zip(fixedText,notes_1, notes_2)}

#INCISO 2
def promNotes(D):
    '''Esta funcion recibe un diccionario {nombre: (nota1, nota2)} y retorna un diccionario donde {nombre: promedio}'''
    return {name: sum(notes)/2 for name, notes in D.items()}

#INCISO 3
def promGlobal(D):
    '''Esta funcion recibe un diccionario {nombre: (nota1, nota2)} y retorna un double con el promedio general de la clase'''
    return (sum(D.values()) / len(D))

#INCISO 4
def highestProm(D):
    '''Esta funcion recibe un diccionario {key = "nombre", value = "promedio"} y devuelve 1 tupla con 2 valores:
        (nombre, promedio)'''
    return max(D, key=D.get), max(D.values()) 

#INCISO 5
def lowestNote(D):
    '''Esta funcion recibe un Diccionario {key = "nombre", value = "promedio"} y devuelve 1 tupla con 2 valores:
         (nombre, nota) del estudiante con la nota mas baja'''
    return min(D, key= D.get), min(min(D.values()))


#INCISO 1
dictStuds = generateZip(names, notes_1, notes_2)
print(f'- Primera estructura: se hizo un diccionario nombre: (nota1, nota2) \n\n {dictStuds} \n')

#INCISO 2
promStuds = promNotes(dictStuds)
print(f'- Segunda estructura: se hizo un diccionario nombre: promedio \n\n {promStuds} \n\n')

#INCISO 3
promClass = promGlobal(promStuds)
print(f'- El promedio global de notas es {round(promClass, 2)}')

#INCISO 4
highStud, highProm= highestProm(promStuds)
print(f'- El alumno {highStud.upper()} es el de mayor promedio con {highProm}')

#INCISO 5
lowerStud, lowerNote = lowestNote(dictStuds)
print(f'- El alumno {lowerStud.upper()} es el de menor nota con {lowerNote}')
