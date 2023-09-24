# Vektorberechnung aus zwei Punkten #

print('Name des ersten Punktes:')
nameP1 = input()

print('Gib die Werte des ersten Punktes ein.')
print('X-Wert:')
X = float(input())

print('Y-Wert:')
Y = float(input())

print('Z-Wert:')
Z = float(input())

print('Name des zweiten Punktes:')
nameP2 = input()

print('Gib die Werte des zweiten Punktes ein.')
print('X-Wert:')
x = float(input())

print('Y-Wert:')
y = float(input())

print('Z-Wert:')
z = float(input())

def calculateVector(X, Y, Z, x, y, z):
    return x-X, y-Y, z-Z

solution = calculateVector(X, Y, Z, x, y, z)

print('Der Vektor ' + str(nameP1) + str(nameP2) + ' ist ' + str(solution) + '.')