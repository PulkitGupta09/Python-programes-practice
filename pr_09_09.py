with open('first.txt', 'r') as f1:
    x1 = f1.read()
with open('second.txt','r') as f2:
    x2 = f2.read()

if(x1 == x2):
    print("both files have same content")
else:
    print("no dont have not same content")    