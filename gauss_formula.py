# Gauß'sche Flächenformel #

print('Definiere deine Fläche.')
print('Anzahl der Punkte:')

numPoints = input()

print('- Koordinaten des 1. Punktes -')
print('Y-Wert:')
P1y = float(input())
print('X-Wert:')
P1x = float(input())

print('- 2.Punkt -')
print('Y-Wert:')
P2y = float(input())
print('X-Wert:')
P2x = float(input())

print('- 3.Punkt -')
print('Y-Wert:')
P3y = float(input())
print('X-Wert:')
P3x = float(input())

print('- 4.Punkt -')
print('Y-Wert:')
P4y = float(input())
print('X-Wert:')
P4x = float(input())

print('- 5.Punkt -')
print('Y-Wert:')
P5y = float(input())
print('X-Wert:')
P5x = float(input())

def column1_sumY():
    return (P3y - P1y) + (P4y - P2y) + (P5y - P3y) + (P1y - P4y) + (P2y - P5y)

solution1 = round(column1_sumY(), 2)

if solution1 != 0.0:
    print('Ups! Die Summe der Y-Werte ergibt nicht 0.')

def column2_factorXsumY():
    return ((P2x * (P3y - P1y)) + (P3x * (P4y - P2y)) + (P4x * (P5y - P3y)) + (P5x * (P1y - P4y)) + (P1x *(P2y - P5y))) / 2

solution2 = round(column2_factorXsumY(), 2)

def column3_sumX():
    return (P1x - P3x) + (P2x - P4x) + (P3x - P5x) + (P4x - P1x) + (P5x - P2x)

solution3 = round(column3_sumX(), 2)
if solution3 != 0.0:
    print('Ups! Die Summe der X-Werte ergibt nicht 0.')

def column4_factorYsumX():
    return ((P2y * (P1x - P3x)) + (P3y * (P2x - P4x)) + (P4y * (P3x - P5x)) + (P5y * (P4x - P1x)) + (P1y * (P5x - P2x))) / 2

solution4 = round(column4_factorYsumX(), 2)

if solution2 == solution4:
    print(f'Die Fläche beträgt {solution4}.')
else:
    print('Die Zwischenrechnungen stimmen nicht überrein. Probiere es nochmal.')