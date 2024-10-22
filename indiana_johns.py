# первое число всегда меньше второго
# первые числа в сумме возрастают от 1

def get_all_dividers(val):                      # функция возвращает все делители для числа
    lst = []
    for i in range(1, int(val**0.5 + 2)):       # берем числа для нахождения делителей(удобно брать до корня - так быстрее если число большое)
        if val % i == 0:
            lst.extend([i, val // i])           # добавляем сразу 2 делителя

    return sorted(set(lst))

def find_sums(value):                           # функция возвращает нужное число (после преобразования)
    lst = get_all_dividers(value)               # получаем делители
    sums = []                                   # список из списков(в каждом 3 значения)
    for i in lst:
        for j in range(1, i):
            k = i - j                           # k - это второе число, j - первое. Их сумма это делитель(i)
            if k <= j:                          # при этом j  соотвтествии с условием меньше k
                break
            else:

                sums.extend([[f'{j}{k}', j, k]])    # если все хорошо добавляем данный список

    sums = sorted(sums, key = lambda x: x[1])                   # сортируем наш список по первому числу суммы. На этом можно остановиться и соеденить строковые значения, но если брать большие числа то порядок может быть неправильный
    sums_keys = set([sums[i][1] for i in range(len(sums))])     # чтобы быть уверенным в правильном порядке возьмем значения по которым сортировали список

    dict_ = {}              # и создадим словарь где ключи - первое число суммы
    for i in sums_keys:
        for j in sums:
            if i == j[1]:   # проверяем равен ли ключ первому числу
                try:
                    dict_[i].append(j)  # и добавляем соответстующий список

                except:
                    dict_[i] = [j]      # если ключа еще не существует, то создаем его

    for key in dict_.keys():
        dict_[key] = sorted(dict_[key], key = lambda x: x[2])   # сортируем уже по 2 числу суммы

    general_str = ''

    for key in sorted(dict_.keys()):
        for i in range(len(dict_[key])):
            general_str += dict_[key][i][0]     # добавляем к конечной строке числа сумм

    return general_str

control_nums = '''3 - 12

4 - 13

5 - 1423

6 - 121524

7 - 162534

8 - 13172635

9 - 1218273645

10 - 141923283746

11 - 11029384756

12 - 12131511124210394857

13 - 112211310495867

14 - 1611325212343114105968

15 - 1214114232133124115106978

16 - 1317115262143531341251161079

17 - 11621531441351261171089

18 - 12151811724272163631545414513612711810

19 - 118217316415514613712811910

20 - 13141911923282183731746416515614713812911'''

control_nums = control_nums.split('\n\n')       # приводим
for num, val in enumerate(control_nums):        # к удобному
    control_nums[num] = val.split(' - ')[1]     # виду

right_values = 0
for i in range(3, 21):
    if find_sums(i) == control_nums[i-3]:   # сверяем значения
        right_values += 1

if right_values == len(control_nums):       # проверяем количество правильных ответов
    print('You Are Alive!')

get_new = int(input('Введите число для преобразования: '))      # для остальных чисел
print(find_sums(get_new))