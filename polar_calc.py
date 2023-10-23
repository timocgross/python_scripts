# Aufgabe 1:
ref_name = 10
pos_name = 12
point_name = 'N'
dist_pos_point = 40.408
angle_pos_point = 75.6723
ref_y = 17630.34
ref_x = 13485.64
pos_y = 17470.53
pos_x = 13320.74

# Aufgabe 2 (alles):
ref_name = 31
pos_name = 30
point1_name = '1'
point2_name = '2'
dist_pos_point1 = 80.114
dist_pos_point2 = 120.670
angle_pos_point1 = 99.9804
angle_pos_point2 = angle_pos_point1 + 66.0423
ref_y = 16389.65
ref_x = 12812.74
pos_y = 16534.98
pos_x = 12653.77

# Aufgabe 2 (Punkt 1):
ref_name = 31
pos_name = 30
point_name = '1'
dist_pos_point = 80.114
angle_pos_point = 99.9804
ref_y = 16389.65
ref_x = 12812.74
pos_y = 16534.98
pos_x = 12653.77

# Aufgabe 2 (Punkt 2):
ref_name = 31
pos_name = 30
point_name = '2'
dist_pos_point = 120.670
angle_pos_point = 166.0227
ref_y = 16389.65
ref_x = 12812.74
pos_y = 16534.98
pos_x = 12653.77

# Aufgabe 4:
ref_name = 200
pos_name = 100
point1_name = '11'
point2_name = '12'
point3_name = '13'
dist_pos_point1 = 89.044
dist_pos_point2 = 68.002
dist_pos_point3 = 90.104
angle_pos_point1 = 69.1123
angle_pos_point2 = 210.1005
angle_pos_point3 = 325.0876
ref_y = 24865.45
ref_x = 21776.92
pos_y = 25002.95
pos_x = 21690.90

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
point3_name = input('Name des 3. Punktes: ')
dist_pos_point3 = float(input('Streckenlänge vom Standpunkt zum 3. Punkt: '))
pre_angle3 = float(input('Gib den Winkel vom Standpunkt zum 3. Punkt an: '))
angle_pos_point3 = angle_pos_point2 + pre_angle3

# Template (ein Punkt):
pos_name = input('Name des Standpunktes: ')
ref_name = input('Name des Referenzpunktes: ')
point_count = input('Anzahl der gesuchten Punkte: ')
point_name = input('Name des gesuchten Punktes: ')
dist_pos_point = float(input('Streckenlänge vom Standpunkt zum gesuchten Punkt: '))
angle_pos_point = float(input('Gib den Winkel vom Standpunkt zum Punkt an: '))
ref_y = float(input(f'Y-Koordinate für den Punkt {ref_name}: '))
ref_x = float(input(f'X-Koordinate für den Punkt {ref_name}: '))
pos_y = float(input(f'Y-Koordinate für den Punkt {pos_name}: '))
pos_x = float(input(f'X-Koordinate für den Punkt {pos_name}: '))

# Template (zwei Punkte):
pos_name = input('Name des Standpunktes: ')
ref_name = input('Name des Referenzpunktes: ')
point_count = input('Anzahl der gesuchten Punkte: ')
point1_name = input('Name des 1. Punktes: ')
point2_name = input('Name des 2. Punktes: ')
dist_pos_point1 = float(input('Streckenlänge vom Standpunkt zum 1. Punkt: '))
dist_pos_point2 = float(input('Streckenlänge vom Standpunkt zum 2. Punkt: '))
angle_pos_point1 = float(input('Gib den Winkel vom Standpunkt zum 1. Punkt an: '))
pre_angle2 = float(input('Gib den Winkel vom Standpunkt zum 2. Punkt an: '))
angle_pos_point2 = angle_pos_point1 + pre_angle2
ref_y = float(input(f'Y-Koordinate für den Punkt {ref_name}: '))
ref_x = float(input(f'X-Koordinate für den Punkt {ref_name}: '))
pos_y = float(input(f'Y-Koordinate für den Punkt {pos_name}: '))
pos_x = float(input(f'X-Koordinate für den Punkt {pos_name}: '))
