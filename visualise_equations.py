import math

limit_lower = float(input('Lower limit: '))
limit_upper = float(input('Upper limit: '))
incre = float(input('In steps: '))
steps = []

if 0 < incre <= 1:
    limit = limit_lower
    while limit <= limit_upper:
        steps.append(limit)
        limit += incre
else:
    print('Incre value is not between 0 and 1.')

func = input('Equation: ')

if 'cos' in func:
    func = func.replace('cos', 'math.cos')
if 'arccos' in func:
    func = func.replace('arccos', 'math.acos')
if 'sin'in func:
    func = func.replace('sin', 'math.sin')
if 'arcsin' in func:
    func = func.replace('arcsin', 'math.asin')
if 'tan'in func:
    func = func.replace('tan', 'math.tan')
if 'arctan' in func:
    func = func.replace('arctan', 'math.atan')
if 'pi' in func:
    func = func.replace('pi', 'math.pi')
if 'e' in func:
    func = func.replace('e', 'math.e')

plot_values = []

for limit in steps:
    x = limit
    func_result = round(eval(func), 4)
    plot_values.append((x, func_result))

print(plot_values)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for i in range(0, len(plot_values)):
    ax.scatter(plot_values[i][0], plot_values[i][1], color='red', marker='o')

for i in enumerate(plot_values):
    for i in range(0, len(plot_values)):
        ax.annotate(i, (plot_values[i][0], plot_values[i][1]))

#ax.set_aspect('equal')
plt.xlim(limit_lower - 1, limit_upper + 1)
plt.ylim(min([i[1] for i in plot_values]) - 1, max([i[1] for i in plot_values]) + 1)
plt.axhline(y = 0, color='black')
plt.axvline(x = 0, color='black')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid()
plt.show()
