# Flächenberechnung von Rechtecken #

print('Wie lang ist die Seite a?')
a = float(input())

print('Oke, und wie lang ist die Seite b?')
b = float(input())

def calculateArea(a, b):
    return a*b

solution = calculateArea(a, b)

print(f'Also, dein Rechteck hat eine Fläche von {solution}.')