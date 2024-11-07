def get_multiplied_numbers(number: int):
    string = str(number).replace('0', '1') # убираем сразу нули
    try:
        return int(string[0]) * get_multiplied_numbers(int(string[1:])) # просто умножаем по условию
    except ValueError:          # когда доходим до последнего числа то оно будет пытаться умножить себя на пустой символ(ValueError)
        return int(string) #  поэтому возвращаем само число

print(get_multiplied_numbers(40203))