# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
class SchoolMember:
    name = ''
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        string = 'Name: ' + self.name + ', Age: ' + str(self.age)
        return string

class Teacher(SchoolMember):
    salary = 0
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        string = 'Name: ' + self.name + ', Age: ' + str(self.age) + ', Salary: ' + str(self.salary)
        return string

class Student(SchoolMember):
    grades = 0
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    def show(self):
        string = 'Name: ' + self.name + ', Age: ' + str(self.age) + ', Grades: ' + str(self.grades)
        return string



