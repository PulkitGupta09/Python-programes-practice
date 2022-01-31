# x = int(input("Enter the number"))

# for star in range(1,x+1):
#     print(star * "*")

    
# x = int(input("Enter the number"))
# for star in range(x):
#     print("*")

# for star in range(x,0,-1):
#     print(star * "*")


z = int(input("Enter 1 for forward printing & Enter 0 for backward printing"))
x = int(input("Enter the number"))
if(z==1):
    for star in range(1,x+1):
        print(star * "*")
else:
    for star in range(x,0,-1):
        print(star * "*")       
