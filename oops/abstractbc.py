from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def printarea(self):
#         return 0

# class Rectangle(Shape):
#     type = "Rectangle"
#     sides = 4
#     def __init__(self):
#         self.length = 45
#         self.breadth = 10

#     # def printarea(self):
#     #     return self.length * self.breadth

# rect1 = Rectangle()
# print(rect1.printarea())


class Shape (ABC):
    def _init_(self):
        print("I am in init")
    @abstractmethod
    def draw_shape(self):
        pass
    @abstractmethod
    def set_color(self):
        pass


class Circle(Shape):
    def draw_shape(self):
        print("Draw Circle")
