class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def dis_name(self):
        return self.name
    
    def dis_age(self):
        return self.age
    
    @classmethod
    def dis_all(cls):
       return Person("Hari", 21)
    
person = Person.dis_all()
print(person.dis_name())
