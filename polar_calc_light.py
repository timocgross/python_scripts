#ref_name = input('Name des Referenzpunktes: ')
#pos_name = input('Name des Standpunktes: ')
#point_name = input('Name des gesuchten Punktes: ')
#dist_pos_point = float(input('Streckenlänge vom Standpunkt zum gesuchten Punkt: '))
#angle_pos_point = float(input('Gib den Winkel vom Standpunkt zum Punkt an: '))

# Eingabe der Koordinaten
#ref_y = input(f'Y-Koordinate für den Punkt {ref_name}: ')
#ref_x = input(f'X-Koordinate für den Punkt {ref_name}: ')
#pos_y = input(f'Y-Koordinate für den Punkt {pos_name}: ')
#pos_x = input(f'X-Koordinate für den Punkt {pos_name}: ')

import math

ref_name = 10
pos_name = 12
point_name = 'N'
dist_pos_point = 40.408
angle_pos_point = 75.6723
ref_y = 17630.34
ref_x = 13485.64
pos_y = 17470.53
pos_x = 13320.74

points = [[ref_y, ref_x], [pos_y, pos_x]]

def first_t():
    global t_pos_ref
    pre_calc = math.atan((points[0][0] - points[1][0]) / (points[0][1] - points[1][1]))
    t_pos_ref = round(((pre_calc * 200) / math.pi), 4)

def check_t_pos_ref(t_pos_ref):
    if 0 <= t_pos_ref < 100:
        print('Der Winkel geht in den I. Quadranten, also word nichts addiert.')
        return t_pos_ref
    elif 100 <= t_pos_ref < 200:
        print('Der Winkel geht in den II. Quadranten, also werden 200 gon addiert.')
        return t_pos_ref + 200
    elif 200 <= t_pos_ref < 300:
        print('Der Winkel geht in den III. Quadranten, also werden 200 gon addiert.')
        return t_pos_ref + 200
    elif 300 <= t_pos_ref < 400:
        print('Der Winkel geht in den IV. Quadranten, also werden 400 gon addiert.')
        return t_pos_ref + 400
    elif t_pos_ref < 0:
        print('Der Winkel ist negativ und braucht 400 gon mehr.')
        return t_pos_ref + 400

first_t()
t_pos_ref = check_t_pos_ref(t_pos_ref)

print(f'Der Richtungswinkel t({pos_name}_{ref_name}) beträgt {t_pos_ref} gon.')

def second_t():
    global t_pos_point
    t_pos_point = round(t_pos_ref + float(angle_pos_point), 4)
    return t_pos_point

second_t()
print(f'Der Richtungswinkel t({pos_name}_{point_name}) beträgt {t_pos_point} gon.')

def diff_y():
    global difference_y
    pre_calc_1 = t_pos_point * (0.9) # Bogenmaß -> Grad
    pre_calc_2 = pre_calc_1 * (math.pi / 180) # Grad -> Gon
    difference_y = round(dist_pos_point * math.sin(pre_calc_2), 3)
    return difference_y

diff_y()
print(f'Die Y-Differenz des Punktes {point_name} beträgt {difference_y}.')

def diff_x():
    global difference_x
    pre_calc_1 = t_pos_point * (0.9)
    pre_calc_2 = pre_calc_1 * (math.pi / 180)
    difference_x = round(dist_pos_point * math.cos(pre_calc_2), 3)
    return difference_x

diff_x()
print(f'Die X-Differenz des Punktes {point_name} beträgt {difference_x}.')

def distance_control():
    global calc_distance
    calc_distance = round(math.sqrt((difference_y)**2 + (difference_x)**2), 3)

distance_control()

print(f'Die gerechnete Strecke beträgt {calc_distance}.')

if calc_distance == dist_pos_point:
    print(True)
else:
    print(False)

def final_coords():
    global y_coord, x_coord
    y_coord = round((pos_y + difference_y), 2)
    x_coord = round((pos_x + difference_x), 2)
    return y_coord, x_coord

final_coords()

print(f'Der Punkt {point_name} hat die Koordinaten ({y_coord} | {x_coord}).')
