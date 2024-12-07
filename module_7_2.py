def custom_write(file_name, strings:list):
    file = open(file_name, "w", encoding="utf-8")
    strings_positions = {}
    positions = []
    for num, i in enumerate(strings):
        positions.append((num+1, file.tell()))
        file.write(f"{i}\n")
    for num, i in enumerate(strings):
        strings_positions[positions[num]] = i
    return strings_positions

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]



result = custom_write('test.txt', info)

for elem in result.items():

    print(elem)