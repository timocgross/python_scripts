import matplotlib.pyplot as plt
import math

pos_name = input('Name des Standpunktes: ')
pos_y = float(input(f'Y-Koordinate für den Punkt {pos_name}: '))
pos_x = float(input(f'X-Koordinate für den Punkt {pos_name}: '))
ref_name = input('Name des Referenzpunktes: ')
ref_y = float(input(f'Y-Koordinate für den Punkt {ref_name}: '))
ref_x = float(input(f'X-Koordinate für den Punkt {ref_name}: '))
point1_name = input('Name des 1. Punktes: ')
dist_pos_point1 = float(input('Streckenlänge vom Standpunkt zum 1. Punkt: '))
angle_pos_point1 = float(input('Gib den Winkel vom Standpunkt zum 1. Punkt an: '))
point2_name = input('Name des 2. Punktes: ')
dist_pos_point2 = float(input('Streckenlänge vom Standpunkt zum 2. Punkt: '))
pre_angle2 = float(input('Gib den Winkel vom Standpunkt zum 2. Punkt an: '))
angle_pos_point2 = angle_pos_point1 + pre_angle2

points = [[ref_y, ref_x], [pos_y, pos_x]]

def first_t():
    global numerator, denominator, t_pos_ref
    numerator = points[0][0] - points[1][0]
    denominator = points[0][1] - points[1][1]
    pre_calc = math.atan(numerator / denominator)
    t_pos_ref = round(((pre_calc * 200) / math.pi), 4)

def quadrant(t_pos_ref):
    if numerator > 0 and denominator > 0:
        print('Der Winkel geht in den I. Quadranten.')
        return t_pos_ref
    elif numerator > 0 and denominator < 0:
        print('Der Winkel geht in den II. Quadranten.')
        return t_pos_ref + 200
    elif numerator < 0 and denominator < 0:
        print('Der Winkel geht in den III. Quadranten.')
        return t_pos_ref + 200
    elif numerator < 0 and denominator > 0:
        print('Der Winkel geht in den IV. Quadranten.')
        return t_pos_ref + 400

first_t()
t_pos_ref = quadrant(t_pos_ref)

print(f'Der Richtungswinkel t({pos_name}_{ref_name}) beträgt {t_pos_ref} gon.')

def second_t():
    global t_pos_point1
    t_pos_point1 = round(t_pos_ref + float(angle_pos_point1), 4)

def check_second_t(t_pos_point1):
    if t_pos_point1 > 400:
        return round((t_pos_point1 - 400), 4)
    else:
        return t_pos_point1

second_t()
t_pos_point1 = check_second_t(t_pos_point1)

print(f'Der Richtungswinkel t({pos_name}_{point1_name}) beträgt {t_pos_point1} gon.')

def third_t():
    global t_pos_point2
    t_pos_point2 = round(t_pos_ref + float(angle_pos_point2), 4)

def check_third_t(t_pos_point2):
    if t_pos_point2 > 400:
        return round((t_pos_point2 - 400), 4)
    else:
        return t_pos_point2
    
third_t()
t_pos_point2 = check_third_t(t_pos_point2)

print(f'Der Richtungswinkel t({pos_name}_{point2_name}) beträgt {t_pos_point2} gon.')

def diff_y_point1():
    global difference_y_point1
    pre_calc_1 = t_pos_point1 * (0.9) # Bogenmaß -> Grad
    pre_calc_2 = pre_calc_1 * (math.pi / 180) # Grad -> Gon
    difference_y_point1 = round(dist_pos_point1 * math.sin(pre_calc_2), 3)
    return difference_y_point1

diff_y_point1()
print(f'Die Y-Differenz des Punktes {point1_name} beträgt {difference_y_point1}.')

def diff_x_point1():
    global difference_x_point1
    pre_calc_1 = t_pos_point1 * (0.9)
    pre_calc_2 = pre_calc_1 * (math.pi / 180)
    difference_x_point1 = round(dist_pos_point1 * math.cos(pre_calc_2), 3)
    return difference_x_point1

diff_x_point1()
print(f'Die X-Differenz des Punktes {point1_name} beträgt {difference_x_point1}.')

def diff_y_point2():
    global difference_y_point2
    pre_calc_1 = t_pos_point2 * (0.9) # Bogenmaß -> Grad
    pre_calc_2 = pre_calc_1 * (math.pi / 180) # Grad -> Gon
    difference_y_point2 = round(dist_pos_point2 * math.sin(pre_calc_2), 3)
    return difference_y_point2

diff_y_point2()
print(f'Die Y-Differenz des Punktes {point2_name} beträgt {difference_y_point2}.')

def diff_x_point2():
    global difference_x_point2
    pre_calc_1 = t_pos_point2 * (0.9)
    pre_calc_2 = pre_calc_1 * (math.pi / 180)
    difference_x_point2 = round(dist_pos_point2 * math.cos(pre_calc_2), 3)
    return difference_x_point2

diff_x_point2()
print(f'Die X-Differenz des Punktes {point2_name} beträgt {difference_x_point2}.')

def distance_control_point1():
    global calc_distance_point1
    calc_distance_point1 = round(math.sqrt((difference_y_point1)**2 + (difference_x_point1)**2), 3)

distance_control_point1()
print(f'Die gerechnete Strecke beträgt {calc_distance_point1} m.')

if calc_distance_point1 == dist_pos_point1:
    print('Kontrolliert: True')
else:
    print('Kontrolliert: False')

def distance_control_point2():
    global calc_distance_point2
    calc_distance_point2 = round(math.sqrt((difference_y_point2)**2 + (difference_x_point2)**2), 3)

distance_control_point2()
print(f'Die gerechnete Strecke beträgt {calc_distance_point2} m.')

if calc_distance_point2 == dist_pos_point2:
    print('Kontrolliert: True')
else:
    print('Kontrolliert: False')

def final_coords_point1():
    global y_coord_point1, x_coord_point1
    y_coord_point1 = round((pos_y + difference_y_point1), 2)
    x_coord_point1 = round((pos_x + difference_x_point1), 2)
    return y_coord_point1, x_coord_point1

final_coords_point1()
print(f'Der Punkt {point1_name} hat die Koordinaten ({y_coord_point1} | {x_coord_point1}).')


def final_coords_point2():
    global y_coord_point2, x_coord_point2
    y_coord_point2 = round((pos_y + difference_y_point2), 2)
    x_coord_point2 = round((pos_x + difference_x_point2), 2)
    return y_coord_point2, x_coord_point2

final_coords_point2()
print(f'Der Punkt {point2_name} hat die Koordinaten ({y_coord_point2} | {x_coord_point2}).')

# Linie Standpunkt - Referenzpunkt, Standpunkt - Punkt 1, Standpunkt - Punkt 2
plt.plot([pos_y, ref_y], [pos_x, ref_x], color='k', linestyle='-', zorder=-1)
plt.plot([pos_y, y_coord_point1], [pos_x, x_coord_point1], color='r', linestyle='-', zorder=-1)
plt.plot([pos_y, y_coord_point2], [pos_x, x_coord_point2], color='r', linestyle='-', zorder=-1)

# Standpunkt mit Beschriftung
plt.scatter([pos_y], [pos_x], color='k', marker='^')
plt.text(pos_y - 3, pos_x, f'{pos_name}', fontsize=12, ha='right', va='center')

# Referenzpunkt mit Beschriftung
plt.scatter([ref_y], [ref_x], color='k', marker='^')
plt.text(ref_y + 3, ref_x, f'{ref_name}', fontsize=12, ha='left', va='center')

# Punkt 1 mit Beschreibung
plt.scatter([y_coord_point1], [x_coord_point1], color='r', marker='o')
plt.text(y_coord_point1 + 3, x_coord_point1,
         f'{point1_name}', color='r', fontsize=12, ha='left', va='center')

# Punkt 2 mit Beschriftung
plt.scatter([y_coord_point2], [x_coord_point2], color='r', marker='o')
plt.text(y_coord_point2 + 3, x_coord_point2,
         f'{point2_name}', color='r', fontsize=12, ha='left', va='center')

plt.grid()
plt.show()
