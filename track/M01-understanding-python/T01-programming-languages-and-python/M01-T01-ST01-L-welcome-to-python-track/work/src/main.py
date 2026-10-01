import show_student_details as s
import calculate_total as t
import get_result as r

name = input("enter your name: ")
roll_no = int(input("enter your roll no: "))
m1 = int(input("enter your marks in first subject: "))
m2 = int(input("enter your marks in second subject: "))
m3 = int(input("enter your marks in third subject: "))

print(s.student_details(name, roll_no))

total = t.calculate_total(m1, m2, m3)
average = t.calculate_average(total)
result = r.get_result(average)
grade = r.show_grade(average)

print("name: ", name)
print("roll no: ", roll_no)
print("total marks: ", total)
print("average marks: ", average)
print("result: ", result)
print("grade: ", grade)

