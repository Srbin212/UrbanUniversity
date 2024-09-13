# 1. Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params('string', 5, [15, 20, 10])
print_params()
print_params(b = 25)
print_params(c = [5, 3, 8])

# 2. Распаковка параметров:
values_list = [(3, 6, 9), 'WoRk', 32]
values_dict= {'a': 'SuN', 'b': [2, 4, 6], 'c': 2.5}
print_params(*values_list)
print_params(**values_dict)

# 3. Строка и отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)