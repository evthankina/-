import math

class GeometricFigure:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle(GeometricFigure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__(x1, y1)
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def perimeter(self):
        side1 = math.sqrt((self.x2 - self.x) ** 2 + (self.y2 - self.y) ** 2)
        side2 = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        side3 = math.sqrt((self.x3 - self.x) ** 2 + (self.y3 - self.y) ** 2)
        return side1 + side2 + side3

    def area(self):
        return 0.5 * ((self.x2 - self.x) * (self.y3 - self.y) - (self.x3 - self.x) * (self.y2 - self.y)) # S=1/2⋅c⋅h

class Rectangle(GeometricFigure):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Circle(GeometricFigure):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

# Пример использования
triangle = Triangle(0, 0, 4, 0, 2, 3.46)
print("Triangle perimeter:", triangle.perimeter())
print("Triangle area:", triangle.area())

rectangle = Rectangle(0, 0, 4, 3)
print("Rectangle perimeter:", rectangle.perimeter())
print("Rectangle area:", rectangle.area())

circle = Circle(0, 0, 5)
print("Circle perimeter:", circle.perimeter())
print("Circle area:", circle.area())
