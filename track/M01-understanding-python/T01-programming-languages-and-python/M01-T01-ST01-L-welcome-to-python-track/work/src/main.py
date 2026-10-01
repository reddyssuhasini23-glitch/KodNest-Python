import student_result as s

name = input("enter your name: ")
roll_no = int(input("enter your roll no: "))
m1 = int(input("enter your marks in first subject: "))
m2 = int(input("enter your marks in second subject: "))
m3 = int(input("enter your marks in third subject: "))

print(s.student_details(name, roll_no))

total = s.calculate_total(m1, m2, m3)
average = s.calculate_average(total)
result = s.get_result(average)
grade = s.show_grade(average)

print("name: ", name)
print("roll no: ", roll_no)
print("total marks: ", total)
print("average marks: ", average)
print("result: ", result)
print("grade: ", grade)

