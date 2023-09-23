values = [
    {'y': 30, 'x': 35},
    {'y': 40, 'x': 25},
    {'y': 35, 'x': 10},
    {'y': 17, 'x': 18},
]

values.append(values[0].copy())
values.append(values[1].copy())

for i in range(1, len(values) - 1):
    before = values[i-1]
    current = values[i]
    after = values[i+1]

    sub_y = after['y'] - before['y']
    product_x = current['x'] * (after['y'] - before['y'])
    sub_x = before['x'] - after['x']
    product_y = current['y'] * (before['x'] - after['x'])

    values[i]['sub_y'] = sub_y
    values[i]['product_x'] = product_x
    values[i]['sub_x'] = sub_x
    values[i]['product_y'] = product_y

for value in values:
    print(value)

