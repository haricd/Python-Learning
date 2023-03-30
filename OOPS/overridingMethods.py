class Boss:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return self.name
    
    def change(self):
        return self.name

class Employee(Boss):
    def __init__(self, name, members, count):
        self.name = name
        self.members = members
        self.count = count

    def greet(self):
        return f'{self.name} {self.members}'
    
    def no_members(self):
        return self.members + self.count
    
employee = Employee('Hari', 20, 7)
print (employee.greet())
print (employee.no_members())
print (employee.change())

