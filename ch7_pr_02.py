l1 = ["Harry","Sohan","sachin","Rahul"]
for item in l1:
    item = item.lower()
    if(item.find("s") == 0):
        print("hello " + item)