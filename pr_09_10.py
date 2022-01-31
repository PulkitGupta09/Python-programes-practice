with open('re.txt','r') as f1:
    x = f1.read()
with open('re.txt','w') as f2:
    f2.write(x.replace(x,''))    