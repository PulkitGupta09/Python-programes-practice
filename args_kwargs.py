def funargs(normal, *argspul, **kwargros):
    print(normal)
    for x in argspul:
        print(x)
    for key,value in kwargros.items():
        print(f"{key} is {value}")




y = 42
har = ["Harry", "Rohan", "Rahul","Corona","Mariz"]
kwargos = {"Rohan":"Monitor","Harry":"Good Teacher","Pulkit":"Top Coder","Manoj":"good runner"}
# kwargos = [['rohan','monitor'],['pulkit','top-coder']]
x = funargs(y,*har,**kwargos)