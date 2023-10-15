import matplotlib.pyplot as plt
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
    global t_pos_point
    t_pos_point = round(t_pos_ref + float(angle_pos_point), 4)

def check_second_t(t_pos_point):
    if t_pos_point > 400:
        return round((t_pos_point - 400), 4)
    else:
        return t_pos_point

second_t()
t_pos_point = check_second_t(t_pos_point)

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
print(f'Die gerechnete Strecke beträgt {calc_distance} m.')

if calc_distance == dist_pos_point:
    print('Kontrolliert: True')
else:
    print('Kontrolliert: False')

def final_coords():
    global y_coord, x_coord
    y_coord = round((pos_y + difference_y), 2)
    x_coord = round((pos_x + difference_x), 2)
    return y_coord, x_coord

final_coords()
print(f'Der Punkt {point_name} hat die Koordinaten ({y_coord} | {x_coord}).')

# Anzeige
plt.plot([pos_y, ref_y], [pos_x, ref_x], color='k', linestyle='-', zorder=-1)
plt.plot([pos_y, y_coord], [pos_x, x_coord], color='r', linestyle='-', zorder=-1)

plt.scatter([pos_y], [pos_x], color='k', marker='^')
plt.text(pos_y - 3, pos_x, f'{pos_name}', fontsize=12, ha='right', va='center')

plt.scatter([ref_y], [ref_x], color='k', marker='^')
plt.text(ref_y + 3, ref_x, f'{ref_name}', fontsize=12, ha='left', va='center')

plt.scatter([y_coord], [x_coord], color='r', marker='o')
plt.text(y_coord + 3, x_coord, f'{point_name}', color='r', fontsize=12, ha='left', va='center')

plt.xlabel('Y-Koordinate')
plt.ylabel('X-Koordinate')
plt.title('Zeichnung')

plt.grid()
plt.show()
