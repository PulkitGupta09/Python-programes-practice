class Calculator:
    def __init__(self,num):
        self.number = num
    def square(self):
        print(f"The value of {self.number} square is {(self.number)**2}")
    def cube(self):
        print(f"The value of {self.number} cube is {(self.number)**3}")
    def squareroot(self):
        print(f"The value of {self.number} squareroot is {(self.number)**(1/2)}")

number1 = Calculator(3)
number1.square()
number1.cube()
number1.squareroot()


                 