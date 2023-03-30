from pprint import pprint

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age

    age = property(fget=get_age, fset=set_age)


print(Person.age)

john = Person('John', 18)
print(john)

john.age = 19
print(john.age, john.name)

###############################################


class Member:
    def __init__(self,person,age):
        self.person = person
        self.age = age

    @property
    def age_(self):
        return self.person
    
    @age_.setter
    def age_(self, person):
        self.person = person


    
member = Member('Duraisingam', 39)
member.person = 'Hari'
print(member.age_)
