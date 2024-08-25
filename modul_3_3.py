# Распаковка позиционных параметров
# 1. Функции с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(b=44)
print_params(0, 11, 22)
print_params('rrr', c=['False'])

# 2. Распаковка параметров
values_list = ['Привет', 33, True]
values_dict = {'a': 'Bye', 'b': 888, 'c': 0.123}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры
values_list_2 = [0.858, 'Help']
print_params(*values_list_2, 2.42)