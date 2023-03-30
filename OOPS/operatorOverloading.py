class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __add__(self, point):
        if not isinstance(point, Point2d):
            raise ValueError('The other must be an instance of the Point2D')
        
        return Point2d(self.x + point.x, self.y + point.y)
    
a = Point2d(15, 1)
b = Point2d(21, 20)
c = a + b

print(c)
