class Employee:
    no_of_leaves = 8

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def  printdetails(self):
        return f"Name of the employee is {self.name} and Salary is {self.salary} and role in company is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls,string):
        params = string.split("-")
        return cls(params[0],params[1],params[2])    

harry = Employee("Harry",5600,"Fianane manager")
karan = Employee.from_str("Karan-340-student")
print(karan.printdetails())
# rohan = Employee()

# harry.name = "Harry"
# harry.salary = 56
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 56
# rohan.role = "student"

# print(harry.printdetails())
# print(harry.salary)

# harry.change_leaves(68)
# print(harry.no_of_leaves)
# print(Employee.no_of_leaves)



