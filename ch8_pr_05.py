# def pattern(n):
#     for i in reversed(range(1,n)):
#         print(" * " * (i+1))

# pattern()



def pattern(n):
    for i in range(0,n):
        print(" * " * (n-i))

pattern(4)