import matplotlib.pyplot as plt
import numpy as np
import math

point_start = input('Name des Anfangspunktes: ')
point_end = input('Name des Endpunktes: ')
print(f'Die Messungslinie heißt {point_start} - {point_end}.')
print('-' * 15)

# 1 - Existierende Maße/Koordinaten eingeben
point_start_y = float(input(f'Y-Koordinate von {point_start}: '))
point_start_x = float(input(f'X-Koordinate von {point_start}: '))
point_end_y = float(input(f'Y-Koordinate von {point_end}: '))
point_end_x = float(input(f'X-Koordinate von {point_end}: '))
print('-' * 15)

# X und Y für die Ansicht vertauschen:
main_coordinates_x = [point_start_y, point_end_y]
main_coordinates_y = [point_start_x, point_end_x]

# X und Y umdrehen, damit die Achsen mehr Sinn ergeben:
plt.plot(main_coordinates_x, main_coordinates_y, color = 'k', linestyle = '--')

plt.scatter([942.11, 929.99], [2944.49, 3018.63], color = 'k')

plt.show()
