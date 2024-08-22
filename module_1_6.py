my_dict = {'Sergey': 1995, 'Alex': 1998, 'George': 1997}
print('Dict:', my_dict)
print('Existing value:', my_dict['Sergey'])
print('Not existing value:', my_dict.get ('Artem'))
my_dict.update({'Anton': 1988,
               'Viktoriy': 1976})
a = my_dict.pop('Viktoriy')
print('Deleted value:', a)
print('Modified dictionary', my_dict)

my_set = {True, 1.5, 3, 'Sergey', 12, 1.5, True, 'Sergey', False, 10, 12}
print('Set:', my_set)
my_set.add('George')
my_set.add((8,13,23))
my_set.discard(True)
print('Modified set:',my_set)