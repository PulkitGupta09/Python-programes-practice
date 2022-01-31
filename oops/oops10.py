# Public -
# Protected -
# Private -


class Employee:
    no_of_leaves = 8
    _protectedvariable = 78
    __privatevariable = 99

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


emp1 = Employee("Pulkit",20000000000,"Ceo")
print(emp1._Employee__privatevariable) 
