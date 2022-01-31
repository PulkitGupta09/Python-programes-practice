maths = int(input("Enter the marks of student in maths : "))
physics = int(input("Enter the marks of student in physics : "))
chemistry = int(input("Enter the marks of student in chemistry : "))
total = ((maths + physics + chemistry)/300)*100

if(maths>33 and physics>33 and chemistry>33 and total>40 ):
    print("student is pass")
    print("percentage is :" + str(total))
else:
    print("student is fail")
    print("percentage is :" + str(total))


