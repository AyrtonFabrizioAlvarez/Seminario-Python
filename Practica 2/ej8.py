word = input('Ingrese una palabra: ')

heterogram = True

for letter in word:
    if ( (word.count(letter) > 1) and (letter.isalpha()) ):
        heterogram = False

if heterogram:
    print('si')
else:
    print('no')