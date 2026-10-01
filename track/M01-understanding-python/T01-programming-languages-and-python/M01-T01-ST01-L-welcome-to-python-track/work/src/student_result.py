def student_details(name, roll_no):
    print(name)
    print(roll_no)

def calculate_total(m1, m2, m3):
    return m1 + m2 + m3

def calculate_average(total, count=3):
    return total / count

def get_result(average):
    if average >= 35:
        return "Pass"
    else:
        return "Fail"

def show_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 35:
        return "D"
    else:
        return "F"
