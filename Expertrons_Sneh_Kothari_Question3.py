students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] 

grade = {}
for student in students:
	if(student[1] in grade):
		grade[student[1]].append(student[0])
	else:
		grade [student[1]] = [student[0]]

print(grade)
lis = list(sorted(grade.items()))[-2]

for student in sorted(lis[1]):
	print(student)