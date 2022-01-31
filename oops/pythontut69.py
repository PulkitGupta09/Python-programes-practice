class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@codewithpulkit.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    def printemail(self):
        return f"This employee email id is {self.email}"        

Hindustani = Employee("Hindustani","Supporter")
Princeraj = Employee("Prince","Raj")
# print(Princeraj.explain())
# print(Princeraj.printemail())
print(Princeraj.email)
