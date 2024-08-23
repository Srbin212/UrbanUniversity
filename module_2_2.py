first = int(input('Введите любое число: '))
second = int(input('Ввведите второе любое число: '))
third = int(input('Введите третье любое число: '))
if first == second and  second == third and third == first:
    print('3')
elif first == second or second == third or third == first:
    print('2')
else:
    print('0')