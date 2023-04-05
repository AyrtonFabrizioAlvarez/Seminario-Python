from collections import Counter

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

def generateZip(names, notes1, notes2):
    ''' Esta funcion retorna una lista de tuplas que fue un zip de 3 archivos (names <string>, notes1 <list>, notes2<list>)'''
    return list(zip(names.replace('\n','').replace(' ', '').replace("'", '').split(','),notes1, notes2))

def promNotes(L):
    '''Esta funcion retorna un diccionario donde key = "nombre", value = "promedio"'''
    promStud = {}
    totalCourse = 0
    for tup in L:
        total = tup[1] + tup[2]
        prom = total / 2
        promStud[tup[0]] = prom
    return promStud

def promGlobal(L):
    '''Esta funcion retorna un double con el promedio general de la clase'''
    totalCourse = 0
    for tup in L:
        totalCourse += tup[1] + tup[2]
    return round((totalCourse / len(L)), 2)

def highestProm(D):
    '''Esta funcion devuelve 2 valores (nombreEstudiante, promedio)'''
    max = -1
    for note in D:
        if D[note]> max:
            max = D[note]
            maxName = note
    return maxName, max

def lowestNote(L):
    '''Esta funcion devuelve 2 valores (nombreEstudiante, nota)'''
    min = 999
    for tup in L:
        if tup[1] < min:
            min = tup[1]
            minName = tup[0]
        if tup[2] < min:
            min = tup[2]
            minName = tup[0]
    return minName, min


zipedList = generateZip(names, notes_1, notes_2)
#print(zipedList)

promStuds = promNotes(zipedList)
print(promStuds)

promClass = promGlobal(zipedList)
#print(promClass)

highPromStud, prom = highestProm(promStuds)
#print(highPromStud, prom)

lowerNoteStud, note = lowestNote(zipedList)
#print(lowerNoteStud, note)