a = input("Enter your string\n")
numlist = []
for x in a:
    if(x.isdigit()):
        numlist.append(int(x))        
# numlist.sort()
# print(numlist)
hel = list(set(numlist))
hel.sort()
# hel.reverse()
# print(hel)
small = 0
for xt in hel:
    if(xt%2==0):
        small = xt
        hel.remove(small)
        break
# print(small)
# print(hel)
hel.reverse()
# print(hel)
if(small != 0):
    str1 = ""
    for x in hel:
        str1 = str1 + str(x)
    print(str1 + str(small))
else:
    print("-1")    