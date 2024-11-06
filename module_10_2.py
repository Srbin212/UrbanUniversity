from time import sleep
import threading


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def thread1(self):
        counter = 100
        for i in range(counter):
            if counter == 0:
                print(f'{self.name} одержал победу спустя {i} дней (дня)!')
                break
            else:
                counter = counter - int(self.power)
                print(f'{str(self.name)}, сражается {i + 1} дней, осталось {counter} воинов.')
            sleep(1)

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.thread1()

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')