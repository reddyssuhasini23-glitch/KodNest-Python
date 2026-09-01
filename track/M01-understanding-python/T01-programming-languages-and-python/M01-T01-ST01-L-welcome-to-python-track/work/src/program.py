class Employee:
    companyName = "kodnest"
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def printDetails(self):
        print(self.id)
        print(self.name)
        print(Employee self.companyName)
e1 = Employee(11, "sanjeev);
print(e1.id)
print(e1.name)
print(Employee.companyName)
print()
e1.printDetails()

