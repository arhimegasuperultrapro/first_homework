first = ['Strings', 'Student', 'Computers']

second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x[0])-len(x[1])) for x in zip(first, second) if len(x[0]) != len(x[1]))
second_result = (len(first[x])==len(second[x]) for x in range(0, 3))
print(list(first_result))

print(list(second_result))