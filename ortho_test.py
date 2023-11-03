import matplotlib.pyplot as plt
import math

points = []

for i in range(1, 2):
    name = input('Anfangspunkt: ')
    s = float(input('Hochwert: '))
    h = float(input('Rechtswert: '))
    points.append([name, s, h])

count = int(input('Punkte, die berechnet werden müssen: '))

for i in range(1, count + 1):
    name = input(f'{i}. Punktname: ')
    s = float(input('Hochwert: '))
    h = float(input('Rechtswert: '))
    points.append([name, s, h])

for i in range(1, 2):
    name = input('Endpunkt: ')
    s = float(input('Hochwert: '))
    h = float(input('Rechtswert: '))
    points.append([name, s, h])

start_y = float(input(f'Anfangspunkt ({points[0][0]}) - Y-Koordinate: '))
start_x = float(input(f'Anfangspunkt ({points[0][0]}) - X-Koordinate: '))
end_y = float(input(f'Endpunkt ({points[-1][0]}) - Y-Koordinate: '))
end_x = float(input(f'Endpunkt ({points[-1][0]}) - X-Koordinate: '))

points[0].append(start_y)
points[0].append(start_x)
points[-1].append(end_y)
points[-1].append(end_x)


delta_y = round((points[-1][3] - points[0][3]), 2)
delta_x = round((points[-1][4] - points[0][4]), 2)

class Precalculations():
    def __init__(self, delta_y, delta_x):
        self.y = delta_y
        self.x = delta_x
    def dist_gauged(self):
        global dist_gauged
        dist_gauged = round((points[-1][1] - points[0][1]), 2)
        return dist_gauged
    def dist_computed(self):
        global dist_computed
        dist_computed = round(math.sqrt((self.y**2) + (self.x**2)), 2)
        return dist_computed
    def ordinate(self):
        ordinate = round((points[-1][2] - points[0][2]), 2)
        return ordinate
    def deviation(self):
        global dist_gauged, dist_computed
        deviation = round(float(abs(dist_gauged - dist_computed)), 2)
        return deviation
    def tolerance(self):
        tolerance = round((0.05 + 0.0003 * dist_computed + 0.008 * math.sqrt(dist_computed)), 2)
        return tolerance
    
p1 = Precalculations(delta_y, delta_x)

dist_gauged = p1.dist_gauged()
dist_computed = p1.dist_computed()
ordinate = p1.ordinate()
deviation = p1.deviation()
tolerance = p1.tolerance()

for p in [p1]:
    print('-' * 15)
    print('Δy: ', delta_y)
    print('Δx: ', delta_x)
    print('Gemessene Strecke: ', dist_gauged)
    print('Gerechnete Strecke: ', dist_computed)
    print('Rechtswertdifferenz: ', ordinate)
    print('Differenz: ', deviation)
    print('Zulässig: ', tolerance)


value_o = round((delta_y) / dist_gauged, 6)
value_a = round((delta_x) / dist_gauged, 6)

print('-' * 15)
print('Variable o: ', value_o)
print('Variable a: ', value_a)

sum_a_o = ((value_o)**2) + ((value_a)**2)
deviation_a_o = abs(0.005)
target = 1

if sum_a_o - target <= deviation_a_o:
    print('Variablen a und o sind ≈ 1.')
else:
    print('Variablen a und o sind nicht ≈ 1.')

print('-'* 15)

delta_s = []

def calculate_delta_s(points):
    for i in range(1, len(points)):
        current_point = points[i]
        previous_point = points[i-1]
        difference = round((current_point[1] - previous_point[1]), 2)
        print(f'Δs für die Rechnung {points[i][0]} - {points[i-1][0]}: {difference}')
        delta_s.append(difference)

calculate_delta_s(points)
print('-'* 15)

delta_h = []

def calculate_delta_h(points):
    for i in range(1, len(points)):
        current_point = points[i]
        prevoius_point = points[i-1]
        difference = round((current_point[2] - prevoius_point[2]), 2)
        print(f'Δh für die Rechnung {points[i][0]} - {points[i-1][0]}: {difference}')
        delta_h.append(difference)

calculate_delta_h(points)
print('-'* 15)

sum_delta_s = round(sum(delta_s), 2)
sum_delta_h = round(sum(delta_h), 2)

if sum_delta_s == dist_gauged:
    print(f'Die Summe der S-Werte stimmt mit der gemessenen Strecke (= {dist_gauged}) überein.')
else:
    print(f'Die Summe der S-Werte stimmt nicht mit der gemessenen Strecke (= {dist_gauged}) überein.')

if sum_delta_h == 0:
    print('Die Summe der H-Werte ergibt 0.')
else:
    print('Die Summe der H-Werte ergibt nicht 0.')


point_delta_y = []

def calc_delta_y():
    for i in range(0, len(points) - 1):
        current_point = points[i]
        delta_y = round((value_o * delta_s[i]) + (value_a * delta_h[i]), 3)
        point_delta_y.append(delta_y)

calc_delta_y()

point_delta_x = []

def calc_delta_x():
    for i in range(0, len(points) - 1):
        current_point = points[i]
        delta_x = round((value_a * delta_s[i]) - (value_o * delta_h[i]), 3)
        point_delta_x.append(delta_x)

calc_delta_x()

sum_point_delta_y = round(sum(point_delta_y), 2)
sum_point_delta_x = round(sum(point_delta_x), 2)

if sum_point_delta_y == delta_y:
    print('-' * 15)
    print(f'Die Summe der Y-Differenzen ergibt Δy (= {delta_y}).')
else:
    print('-' * 15)
    print(f'Die Summe der Y-Differenzen ergibt nicht Δy (= {delta_y}).')

if sum_point_delta_x == delta_x:
    print(f'Die Summe der X-Differenzen ergibt Δx (= {delta_x}).')
    print('-' * 15)
else:
    print(f'Die Summe der X-Differenzen ergibt nicht Δx (= {delta_x}).')
    print('-' * 15)


new_y_values = []

value = points[0][3]
new_y_values.append(value)

for i in range(0, len(point_delta_y)):
    value = round((value + point_delta_y[i]), 3)
    value_rounded = round((value), 2)
    new_y_values.append(value_rounded)

print(f'Letzter Y-Wert: {new_y_values[-1]}.')

if new_y_values[-1] == points[-1][3]:
    print('Y-Koordinate kontrolliert.')
    print('-' * 15)
else:
    print('Y-Koordinate nicht kontrolliert.')
    print('-' * 15)

new_x_values = []

value_2 = points[0][4]
new_x_values.append(value_2)

for i in range(0, len(point_delta_x)):
    value_2 = round((value_2 + point_delta_x[i]), 3)
    value_rounded = round((value_2), 2)
    new_x_values.append(value_rounded)

print(f'Letzter X-Wert: {new_x_values[-1]}.')

if new_x_values[-1] == points[-1][4]:
    print('X-Koordinate kontrolliert.')
    print('-' * 15)
else:
    print('X-Koordinate nicht kontrolliert.')
    print('-' * 15)


point_names = []

for i in range(0, len(points)):
    names = points[i][0]
    point_names.append(names)

completed_points = [(point, y, x) for point, y, x in
                    zip(point_names, new_y_values, new_x_values)]

for i in range(1, len(completed_points) - 1):
    print(f'Der Punkt {points[i][0]} hat die Koordinaten {completed_points[i][1]} | {completed_points[i][2]}.')


plt.plot([new_y_values], [new_x_values], color='red', marker='o', markersize=10)
plt.plot([new_y_values[0], new_y_values[-1]], [new_x_values[0], new_x_values[-1]],
         linestyle='dotted', color='black')

plt.grid(True)
plt.show()
