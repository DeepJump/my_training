grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades={sorted(students)[0]:sum(grades[0])/len(grades[0])} #{sorted students: average grades}
number_ = 0
while number_< len(students):
  average_grades.update({sorted(students)[number_]:round(sum(grades[number_])/len(grades[number_]),2)})
  number_ += 1
print(average_grades)