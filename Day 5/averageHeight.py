studentsHeight = input("Enter the list of student height to be averaged: ").split()

for n in range(0, len(studentsHeight)):
    studentsHeight[n] = int(studentsHeight[n])

print(studentsHeight)

totalHeight = 0

for eachHeight in studentsHeight:
    totalHeight += eachHeight

numberOfStudents = 0

for students in studentsHeight:
    numberOfStudents += 1

# print(totalHeight)
# print(numberOfStudents)

averageHeight  = totalHeight // numberOfStudents
print(averageHeight)
