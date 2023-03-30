# class Person:
#     def __init__(self):
#         self.count = 0
    
#     def increment(self):
#         self.count += 1
    
#     def reset(self):
#         self.count = 0
    
#     def value(self):
#         return self.count
    
# person = Person()
# person.increment()
# print(person.value())

# using private attribute

class Person:
    def __init__(self):
        self.__count = 0
    
    def increment(self):
        self.__count += 1
    
    def reset(self):
        self.__count = 0
    
    def value(self):
        return self.__count
    
person = Person()
print(person._Person__count)
