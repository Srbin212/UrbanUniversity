import requests
import numpy as np
import matplotlib.pyplot as plt



# requests
# Отправляем GET-запрос
response = requests.get('https://jsonplaceholder.typicode.com/posts')
# Проверяем статус-код
if response.status_code == 200:
    print(response.json())  # Выводим данные в консоль



# numpy
# Создание массива из чисел
array = np.array([1, 2, 3, 4, 5])
# Выполнение математических операций
sum_result = np.sum(array)
mean_result = np.mean(array)
std_result = np.std(array)
# Вывод результатов
print("Массив:", array)
print("Сумма:", sum_result)
print("Среднее:", mean_result)
print("Стандартное отклонение:", std_result)



# matplotlib
# Пример данных
vals = [24, 17, 53, 21, 35]
labels = ["Opel", "Toyota", "BMW", "Changan", "Lada"]
# Круговая диаграмма
plt.pie(vals, labels=labels)
plt.title("Распределение марок автомобилей на дороге")
plt.show()