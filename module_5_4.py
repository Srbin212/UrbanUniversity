class House:
    house_history = []

    def __new__(cls, *args, **kwargs):
        if len(args) > 0:
            cls.house_history.append(args[0])
        instance = super().__new__(cls)
        return  instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}.'

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.house_history)
h2 = House('ЖК Акация', 20)
print(House.house_history)
h3 = House('ЖК Матрешки', 20)
print(House.house_history)

del h2
del h3

print(House.house_history)