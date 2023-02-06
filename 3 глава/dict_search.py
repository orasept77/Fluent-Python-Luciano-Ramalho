my_dict = {}

# Верно (поиск происходит 1 раз)
my_dict.setdefault('test', []).append('success')

# Не верно (поиск по словарю происходит 3 раза)
if 'test' not in my_dict:
    my_dict['test'] = []
my_dict['test'].append('success')

print(my_dict.get('t', None))
print(my_dict)

