import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        val = 100
        days = 0
        print(f"{self.name}, на нас напали!")
        while val > 0:
            days += 1
            time.sleep(1)
            val -= self.power
            print(f"{self.name} сражается {days} дней, осталось {val} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)

second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()