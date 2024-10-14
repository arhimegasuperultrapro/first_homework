students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
for num, lst in enumerate(grades):
    grades[num] = sum(lst) / len(lst)

stud_grad = {}
for i in range(len(students)):
    stud_grad[students[i]] = grades[i]

print(stud_grad)