# 2
immutable_var = (1, 'rrr', True)
print(immutable_var)

# 3
# Кортеж неизменяемый тип данных - поэтому возникнет исключение
try:
    immutable_var[0] = 111
except:
    print('Нельзя менять элемент кортежа')

# 4
mutable_list = [1, 2, 3]
mutable_list.append(44)
del mutable_list[0]
print(mutable_list)
