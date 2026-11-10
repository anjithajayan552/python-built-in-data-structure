s1 = int(input("enter the mark of student 1:"))
s2 = int(input("enter the mark of student 2:"))
s3 = int(input("enter the mark of student 3:"))
s4 = int(input("enter the mark of student 4:"))
s5 = int(input("enter the mark of student 5:"))

marks = [s1, s2, s3, s4, s5]
print(marks)

print(marks[0], marks[-1])
marks.append(65)
print(marks)
marks.pop(3)
print(marks)
print(len(marks))
marks.sort()
print(marks)
