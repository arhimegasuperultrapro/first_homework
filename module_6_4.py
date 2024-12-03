from pymsgbox import password
import math

class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (r in range(0, 256)) + (g in range(0, 256)) + (b in range(0, 256)) == 3:
            return True

    def set_color(self, r, g, b):
        self.__color = (r, g, b) if self.__is_valid_color(r, g, b) else self.__color

    def __is_valid_sides(self, *sides):
        if all(i > 0 for i in sides) and len(sides) == len(self.__sides): return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *new_sides):
        if len(new_sides) == len(self.__sides): self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) != Circle.sides_count:
            sides = 1

        super().__init__(color, sides)

        self.__radius = (0.5 * sides[0]) / math.pi

    def get_square(self):
        return math.pi * self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) != Triangle.sides_count:
            sides = [1, 1, 1]

        super().__init__(color, sides)

    def get_square(self):
        a, b, c = self._Figure__sides[0], self._Figure__sides[1], self._Figure__sides[2]
        p = 0.5 * (a + b + c)
        return (p*(p-a)*(p-c)*(p-b))**0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0] for x in range(12)]

        elif len(sides) != Cube.sides_count:
            sides = [1 for x in range(12)]

        super().__init__(color, sides)

    def get_volume(self):
        return self._Figure__sides[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)



# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится

print(cube1.get_color())



# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится

print(cube1.get_sides())

circle1.set_sides(15) # Изменится

print(circle1.get_sides())



# Проверка периметра (круга), это и есть длина:

print(len(circle1))



# Проверка объёма (куба):

print(cube1.get_volume())




