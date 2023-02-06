# Верно:

board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

# Эквивалентно:
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)

# Не верно (список из 3 ссылок, ссылающихся на 1 объект)

board1 = [['_'] * 3] * 3
print(board1)
board1[1][2] = 'X'
print(board1)

# Эквивалентно:
row = ['_'] * 3
board1 = []
for i in range(3):
    board1.append(row)

# У изменяемых объектов ссылка будет вести на тот же объект. Сработает метод __iadd__ (т.е. a.extend(b)
l1 = list(range(10))
print(id(l1))
l1 += list(range(8, -1, -1))
print(id(l1))

# У неизменяемых объектов ссылка будет вести на новый объект. Сработает метод __add__ (т.е. a = a + b)
t1 = tuple(range(10))
print(id(t1))
t1 += tuple(range(8, -1, -1))
print(id(t1))
