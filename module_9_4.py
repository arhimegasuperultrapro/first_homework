from random import choice

#1
first = 'Мама мыла раму'

second = 'Рамена мало было'
print(list(map(lambda x, y: x==y, first, second)))

#2
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, "a", encoding='utf-8')
        for i in data_set:
            file.write(str(i)), file.write('\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')

write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#3
class MysticBall:
    def __init__(self, *words):
        self.words_collection = words
    def __call__(self):
        return choice(self.words_collection)

first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())

print(first_ball())

print(first_ball())