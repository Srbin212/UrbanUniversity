class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return ''.join(file.readlines())
        except FileNotFoundError:
            return ''

    def add(self, *products):
        existing_products = self.get_products().strip().splitlines()

        with open(self.__file_name, 'a+') as file:
            file.seek(0)

            current_products = {line.split(',')[0] for line in existing_products}

            for product in products:
                product_str = str(product)
                if product.name in current_products:
                    print(f'Продукт {product_str} уже есть в магазине')
                else:
                    file.write(product_str + '\n')

# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)
print(s1.get_products())

# Проверка второго запуска
s1.add(p1, p2, p3)
print(s1.get_products())