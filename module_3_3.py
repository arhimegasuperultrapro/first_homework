# 1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()

print_params(1, 2)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2
values_list = [True, 12, 'dd']
values_dict = {'a': 'hi', 'b': True, 'c': 20}
print_params(*values_list)
print_params(**values_dict)



# 3
values_list2 = [1, True]
print_params(*values_list2, 42)


