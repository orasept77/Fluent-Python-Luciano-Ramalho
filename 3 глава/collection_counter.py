from collections import Counter

ct = Counter('Pavel Kozlov')
print(ct)

ct.update('Angelina Pos')
print(ct)

print(ct.most_common(3))