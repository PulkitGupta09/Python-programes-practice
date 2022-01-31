f = open('poems.txt','r')
x = f.read()
print(x)

wordfinder = x.find("Twinkle")
print(wordfinder)
f.close()