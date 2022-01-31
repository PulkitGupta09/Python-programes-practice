l = 10

def function1(n):
    m = 8
    global l 
    l = l + 45
    print(l,m)
    print(n,"printed")

function1(8)

print(l)