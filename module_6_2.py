class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model:str, color:str, engine_power:int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        print(f"Model: {self.__model}")

    def get_horse_power(self):
        print(f"Power: {self.__engine_power}")

    def get_color(self):
        print(f"Color: {self.__color}")

    def print_info(self):
        self.get_model()
        self.get_horse_power()
        self.get_color()
        print(f"The owner: {self.owner}")

    def set_color(self, new_color:str):
        self.__color = new_color if new_color.lower() in Vehicle.__COLOR_VARIANTS else print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)



# Изначальные свойства

vehicle1.print_info()



# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'



# Проверяем что поменялось

vehicle1.print_info()