# Работа со списковыми включениями

import string
from random import choice

symbols = list(string.ascii_letters + string.digits)
result = ''.join([choice(symbols) for i in range(10)])

# Замена filter + lambda
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
res = sum([i for i in l if i % 2 == 0])

# Если поменять на for size in sizes for color in colors, то результат будет упорядочен по другому
colors = ['red', 'white', 'blue']
sizes = ['M', 'S', 'XL']
for thirt in (f'{c} {s}' for c in colors for s in sizes):
    print(thirt)
