class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 56
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 56
rohan.role = "student"

print(harry.__dict__)
harry.no_of_leaves = 4
print(harry.__dict__)

print(Employee.__dict__)
Employee.no_of_leaves = 10
print(Employee.__dict__)



