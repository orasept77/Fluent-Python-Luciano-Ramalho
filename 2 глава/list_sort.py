fruits = ['grape', 'orange', 'banana', 'apple', 'raspberry']
# sorted() возвращает новый объект, не изменяя старый
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(fruits)

# .sort() изменяет исходный объект и возвращает None
fruits2 = ['grape', 'orange', 'banana', 'apple', 'raspberry']
print(fruits2)
fruits2.sort(reverse=True, key=len)
print(fruits2)

# Если элементы отсортированы по длинне, а длинна равна, то порядок этих элементов сохраняется
