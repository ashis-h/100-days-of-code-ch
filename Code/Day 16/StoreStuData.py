students = []
names = []
marks = []
rollno =input("Enter the Registration Number :=")
for i in rollno:
     #rollno = input("input  of student "+ i)
     #rollnos.append(rollno)
     name = input("input name of student :=")
     names.append(name)
     mark = input("input mark % of the student :=")
     marks.append(mark)
for i in rollno:
     print(students[i] + ": ",'names[i]')
     print(students[i] + ": ",'marks[i]')
