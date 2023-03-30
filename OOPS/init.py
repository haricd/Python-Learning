class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Hari', 21)
print(person.name, person.age)        

#######################################

class Member:
    def __init__(self, name, age=23):
        self.name = name
        self.age = age

person = Member('Hari')
print(person.name, person.age)   