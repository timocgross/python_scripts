import math

print('Gib die Koordinaten der zwei Punkte an, die die Linie definieren.')

points = []
for i in range(2):
    point_name = input(f'Name des Punktes {i + 1}: ')
    point_y = float(input(f'y-Koordinate von Punkt {i + 1}: '))
    point_x = float(input(f'x-Koordinate von Punkt {i + 1}: '))
    points.append({'Name': point_name, 'y': point_y, 'x': point_x})

target = float(input('Gib die Länge der Grenze ein: '))

Δy = points[1]['y'] - points[0]['y']
Δx = points[1]['x'] - points[0]['x']
length = math.sqrt((Δy)**2 + (Δx)**2)
print(f'Die berechnete Grenze ist {length:.3f} m lang.')

tolerance = 1  # Adjust the tolerance as needed.
if abs(length - target) <= abs(tolerance):
    print('Die Grenze ist im Toleranzbereich.')
else:
    offset = length - target
    print(f'Die Grenze weich zu sehr ab. Die Differenz ist {offset:.3f}.')
