from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])

with open('floats.bin', 'wb') as f:
    floats.tofile(f)

floats2 = array('d')

with open('floats.bin', 'rb') as f:
    floats2.fromfile(f, 10 ** 7)

print(floats2[-1])
print(floats2 == floats2)

print(len(memoryview(floats)))

print(floats.typecode)