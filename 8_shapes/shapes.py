# Circle, Rectangle, Triangle, sum_area_of_shapes
import math


class Shape:

    def __init__(self):
        pass

    def get_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * (self.__radius**2)


class Triangle(Shape):

    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def get_area(self):
        return 0.5 * self.__base * self.__height


def sum_area_of_shapes(shapes):
    sum = 0
    for shape in shapes:
        sum += shape.get_area()

    return sum