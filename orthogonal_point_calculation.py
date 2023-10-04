import math

print('- Anfangs- und Endpunkt der Messlinie -')
for i in range(1):
    print('Name des Anfangspunkts')
    name_st_point = int(input())
    print('Hochmaß:')
    st_point_s = float(input())
    print('Seitenmaß:')
    st_point_h = float(input())
    print('y-Koordinate:')
    st_point_y = float(input())
    print('x-Koordinate:')
    st_point_x = float(input())

    print('Name des Endpunkts')
    name_en_point = int(input())
    print('Hochmaß:')
    en_point_s = float(input())
    print('Seitenmaß:')
    en_point_h = float(input())
    print('y-Koordinate:')
    en_point_y = float(input())
    print('x-Koordinate:')
    en_point_x = float(input())

print('Punkte der Messungslinie')
print(f'Name: {name_st_point}, Δs = {st_point_s}, Δh = {st_point_h}, y = {st_point_y}, x = {st_point_x}')
print(f'Name: {name_en_point}, Δs = {en_point_s}, Δh = {en_point_h}, y = {en_point_y}, x = {en_point_x}')

print('Wieviele Punkte sollen berechnet werden?')
points = int(input())

values = []

for i in range(1, points + 1):
    print(f'Name des {i}. Punkts')
    name = int(input())
    print('Hochmaß:')
    vertical = float(input())
    print('Seitenmaß:')
    horizontal = float(input())

    # Add the following print statements to display the values for each point
    print(f'Point {i}: Name = {name}, Hochmaß = {vertical}, Seitenmaß = {horizontal}')
    
    # Append the values to the 'values' list
    values.append({'name': name, 's': vertical, 'h': horizontal})



# 1st calculation (Δy, Δx, Sgem, Sger, Diff, zul.)
Δy = en_point_y - st_point_y
print(f'Δy = ' + str(round(Δy, 2)))

Δx = en_point_x - st_point_x
print(f'Δx = ' + str(round(Δx, 2)))

Sgem = en_point_s - st_point_s
print(f'Sgem. = {Sgem}')

Sger = math.sqrt((Δy)**2 + (Δx)**2)
print('Sger. = ' + str(round(Sger, 2)))

difference = Sgem - Sger
print('Diff. = ' + str(abs(round(difference, 2))))

tol_diff = 0.05 + 0.0003 * Sgem + 0.008 * math.sqrt(Sgem)
print('zul. = ' + str(abs(round(tol_diff, 2))))
if difference > tol_diff:
    print('Die Differenz ist zu groß.')
else:
    print('Die Differenz ist oke.')



# 2nd calculation (o, a)
o = (en_point_y - st_point_y) / Sgem
a = (en_point_x - st_point_x) / Sgem
print('Variable o = ' + str(round(o, 6)))
print('Variable a = ' + str(round(a, 6)))

control_o_a = (o**2) + (a**2)
print('Die Summe von o und a ergibt ' + str(round(control_o_a, 6)) + '.')



# 3rd calculation (ΣΔs, ΣΔh)
sum_Δs = Sgem
sum_Δh = 0

# Loop through all points in the 'values' list and print 'Δs' and 'Δh'
for i in range(1, len(values) - 1):
    before = values[i-1]
    current = values[i]

    Δs = current['s'] - before['s']
    Δh = current['h'] - before['h']

    current['Δs'] = Δs
    current['Δh'] = Δh

for point in values:
    Δs = point['Δs']
    Δh = point['Δh']
    print(f'Δs: {Δs}, Δh: {Δh}')

if sum_Δs == Sgem:
    print(f'ΣΔs stimmt überein. ΣΔs = {sum_Δs}.')
else:
    print('ΣΔs stimmt nicht.')

if sum_Δh == 0:
    print(f'ΣΔh stimmt überein. ΣΔh = {sum_Δh}.')
else:
    print('ΣΔh stimmt nicht.')
