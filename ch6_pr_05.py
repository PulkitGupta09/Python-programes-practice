import time
start = time.time()
name = input("Enter your name : ")
list = ["pulkit","manoj","rahul","raghvendra"]
if(name in list) :
    print("Name is in list")
else:
    print("Name is not in the list")

end = time.time()
print(end-start)    