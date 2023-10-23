points = []

for i in range(1, 3):
    name = input(f'Name: ')
    x_coord = float(input('X-Koordinate: '))
    y_coord = float(input('Y-Koordinate: '))
    z_coord = float(input('Z-Koordinate: '))
    points.append((name, x_coord, y_coord, z_coord))

(x1, y1, z1) = points[0][1:]
(x2, y2, z2) = points[1][1:]
solution = (x1*x2) + (y1*y2) + (z1*z2)

print(f'Das Skalarprodukt {points[0][0]}-{points[1][0]} ist {solution}.')
if solution < 0:
    print('Der Winkel φ ist ein stumpfer Winkel.')
elif solution > 0:
    print('Der Winkel φ ist ein spitzer Winkel.')
else:
    print('Beide Vektoren sind zueinander rechtwinklig/orthogonal.')
