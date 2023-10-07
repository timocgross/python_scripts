import math

# Prompt the user for the coordinates of two points defining the line.
print('Gib die Koordinaten der zwei Punkte an, die die Linie definieren.')

# Use lists and loops to simplify input and calculations.
points = []
for i in range(2):
    point_name = input(f'Name des Punktes {i + 1}: ')
    point_y = float(input(f'y-Koordinate von Punkt {i + 1}: '))
    point_x = float(input(f'x-Koordinate von Punkt {i + 1}: '))
    points.append({'Name': point_name, 'y': point_y, 'x': point_x})

# Prompt the user for the desired boundary length.
target = float(input('Gib die Länge der Grenze ein: '))

# Calculate the difference in y and x coordinates.
Δy = points[1]['y'] - points[0]['y']
Δx = points[1]['x'] - points[0]['x']

# Calculate the Euclidean distance between the two points.
length = math.sqrt((Δy)**2 + (Δx)**2)

# Round and print the calculated distance.
print(f'Die berechnete Grenze ist {length:.3f} m lang.')

# Check if the calculated distance matches the target within a tolerance.
tolerance = 1  # Adjust the tolerance as needed.
if abs(length - target) <= abs(tolerance):
    print('Die Grenze ist im Toleranzbereich.')
else:
    offset = length - target
    print(f'Die Grenze weich zu sehr ab. Die Differenz ist {offset:.3f}.')
