invoice = 'Pavel Evgenyevich Kozlov'

NAME = slice(0, 5)
LASTNAME = slice(6, 17)
FAMILYNAME = slice(18, 24)

ONE_ARG = slice(2, None)

# Именованные срезы
print(invoice[NAME])
print(invoice[LASTNAME])
print(invoice[FAMILYNAME])

# Именованный срез с 1 аргументом
print(invoice[ONE_ARG])

l = list(range(10))
print(l)
# Заменить 2,3,4 элементы (2,3,4) на 20, 30
l[2:5] = [20, 30]
print(l)
# Удалить 5, 6 элементы (6,7)
del l[5:7]
print(l)
# Заменить элементы с 3, до конца списка, с шагом 2 (30,8) на 11,2
l[3::2] = [11, 22]
print(l)
# Заменит элементы 2,3,4 на 100
l[2:5] = [100]
print(l)
