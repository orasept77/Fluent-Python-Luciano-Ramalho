DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'USA'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (81, 'Japan')
]

# Пары инвертированы (ключом выступает страна, значением код)
my_dict = {country: code for code, country in DIAL_CODES}
print(my_dict)

# Пары инвертированы обратно, страна переведена в верхний регистр, произведена фильтрация по коду
my_dict2 = {code: country.upper() for country, code in my_dict.items() if code < 66}
print(my_dict2)
