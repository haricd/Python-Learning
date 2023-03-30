class Boss:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return self.name

class Employee(Boss):
    def __init__(self, name, members):
        self.name = name
        self.members = members

class Dummy(Employee):
    def __init__(self, name):
        self.name = name

employee = Employee('Jio', 76)
dummy = Dummy('Kio')
print(employee.greet())
print(dummy.greet())