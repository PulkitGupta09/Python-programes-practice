class Programmer:
    company = "Microsoft"
    
    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getinfo(self):
        print(f'The Name of the company is {self.company} and the Name of the programmer is {self.name} and the Product is {self.product}')

harry = Programmer('Harry','Skype')
rahul = Programmer('Rahul','Google')
harry.getinfo()
rahul.getinfo()        