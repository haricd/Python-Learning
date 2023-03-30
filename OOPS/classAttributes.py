class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.15

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius
    
circle = Circle(10)
print(circle.radius, circle.pi)
print(circle.area())
print(Circle.pi)
print(circle.pi)