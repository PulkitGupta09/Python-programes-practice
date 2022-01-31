with open('donkey_m.txt','r') as f1:
    read = f1.read()

with open('donkey_m.txt','w') as f2:
    read = read.replace('donkey','******')
    f2.write(read)
