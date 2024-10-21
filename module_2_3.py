my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
other_list = [1, 2, 3]

while num != len(my_list):   # проверяем чтобы не было обращения к несуществующему индексу(после последнего)
    if my_list[num] >= 0:
        print(my_list[num])
        num += 1
        continue
    else:
        break

