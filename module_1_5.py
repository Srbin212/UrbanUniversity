mutable_var = 1, 13, 'string', 2.5
print('immutable_var:', mutable_var)
#mutable_var[1] = 200 - Кортеж относится к неизменяемым типам данных
# и не поддерживает обращение по элементам.
mutable_list = ['apple', 2, 'coconut', 'banana', 5]
mutable_list.append(True)
mutable_list.extend(['string', 2.5])
mutable_list.remove(2.5)
mutable_list[2] = 200
print('mutable_list:', mutable_list)