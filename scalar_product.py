# Skalarprodukt (Winkel zweier Vektoren) #

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

def calculateScalar():
    return (X*x) + (Y*y) + (Z*z)

solution = calculateScalar()

print('Das Skalarprodukt ' + str(nameP1) + str(nameP2) + ' ist ' + str(solution) + '.')
if solution < 0:
    print('Der Winkel φ ist ein stumpfer Winkel.')
elif solution > 0:
    print('Der Winkel φ ist ein spitzer Winkel.')
else:
    print('Beide Vektoren sind zueinander rechtwinklig/orthogonal.')