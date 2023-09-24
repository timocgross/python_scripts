print('Wieviele Punkte werden gebraucht?')
points = int(input())

if points < 3:
    print('Bitte drei Punkte eingeben!')
    quit()

values = []

for i in range(1, points + 1):
    print(f'{i}. Punkt')
    print('Y-Wert:')
    y = float(input())
    print('X-Wert:')
    x = float(input())

    values.append({'y': y, 'x': x})

values.append(values[0].copy())
values.append(values[1].copy())

sum_y = 0
sum_x = 0

for i in range(1, len(values) - 1):
    before = values[i-1]
    current = values[i]
    after = values[i+1]

    # calculating
    sub_y = after['y'] - before['y']
    product_x = current['x'] * (after['y'] - before['y'])
    sub_x = before['x'] - after['x']
    product_y = current['y'] * (before['x'] - after['x'])

    values[i]['sub_y'] = sub_y
    values[i]['product_x'] = product_x
    values[i]['sub_x'] = sub_x
    values[i]['product_y'] = product_y

    sum_y += product_y
    sum_x += product_x

if round(sum_y, 3) != round(sum_x, 3):
    print('Irgendwas ist schiefgelaufen...')
    quit()

half_sum_y = sum_y / 2.0
print(f'Die Fläche beträgt {half_sum_y}.')