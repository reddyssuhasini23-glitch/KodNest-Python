
class Developer:
    def work(self):
         print("Developer is working")

    def attendmeeting(self):
        print("Developer is attending meeting")

class JavaDeveloper(Developer):
    def work(self):
        print("Java Developer is working on java")

    def doJavaProject(self):
        print("Java Developer is building java project")

class PythonDeveloper(Developer):
    def work(self):
        print("Python Developer is working on python")
    def doPythonProject(self):
        print("Python Developer is building python project")

dev = Developer()
dev.work()
dev.attendmeeting()

javadev = JavaDeveloper()
javadev.work()
javadev.attendmeeting()
javadev.doJavaProject()

pydeveloper = PythonDeveloper()
pydeveloper.work()
pydeveloper.attendmeeting()
pydeveloper.doPythonProject()
    
    


