data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]


def get_sum(d):
    summa = 0

    for i in d:
        try:
            if not isinstance(i, str) and not isinstance(i, dict):
                summa += i
            elif not isinstance(i, dict):
                summa += len(i)
            else:
                summa += get_sum(i.items())     # после преобразования получаем список кортежов


        except TypeError:       # когда встречаем вложенную послежовательность
            summa += get_sum(i)

    return summa

print(get_sum(data_structure))
