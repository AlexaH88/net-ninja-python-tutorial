grades = ['A', 'B', 'F', 'C', 'F', 'A']


def remove_fails(grade):
    return grade != 'F'


# filter method --> filter(testing_function, data)
# same as on map method, list() is needed to convert object to list
print(list(filter(remove_fails, grades)))


# for loop method
filtered_grades = []
for grade in grades:
    if grade != 'F':
        filtered_grades.append(grade)
print(filtered_grades)


# comprehension method
print([grade for grade in grades if grade != 'F'])
