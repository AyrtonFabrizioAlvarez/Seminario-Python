letterValues = {'aeioulnrst':1,
                'dg':2,
                'bcmp':3,
                'fhvwy':4,
                'k':5,
                'jx':8,
                'qz':10}

word = input('Ingresa una palabra: ')
counter = 0
for key in letterValues:
    for letter in word:
        if letter in key:
            counter += letterValues[key]

print(f'La palabra {word} vale: {counter}')