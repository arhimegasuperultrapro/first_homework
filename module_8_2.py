
def personal_sum(numbers:(list, tuple, set, dict)):
    if not (isinstance(numbers, list) or isinstance(numbers, dict) or isinstance(numbers, set) or isinstance(numbers, tuple) or isinstance(numbers, str)):
        return 0
    result = 0
    incorrect_data = 0
    if isinstance(numbers, dict):
        for key in numbers.keys():
            try:
                result += numbers[key]
            except TypeError:
                incorrect_data += 1
    else:
        for i in numbers:
            try:
                result += i
            except TypeError:
                incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers:(list, tuple, set, dict)):
    try:
        res, inc = personal_sum(numbers)
    except TypeError:
        return None
    try:
        mean = res / (len(numbers) - inc)
    except ZeroDivisionError:
        return 0
    return mean

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип

print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3

print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция

print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать