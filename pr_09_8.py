with open('this.txt','r') as f1:
    readtocopy = f1.read()
with open('this_copy.txt','w') as f2:
    f2.write(readtocopy)    