class A:
    classvar1 = "I am in class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "I am special in class A"

class B(A):
    classvar1 = "I am in class variable in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B constructor"
        # self.classvar1 = "Instance var in class B"

a = A()
b = B()
print(b.special,b.var1)    