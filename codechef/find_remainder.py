T = int(input())
# def remainder(num1,num2):
#     num3 = num1 % num2
#     return num3
for i in range(0,T):
    x, y = int(input()), int(input())
    # x = int(input())
    # y = int(input())
    z = x % y 
    print(z)

# T = int(input())
# for items in range(0,T):
#     num = int(input())
#     sum = 0
#     while(num>0):
#         sum = sum + (num%10)
#         num = int(num/10)
#     print(sum)


T = int(input())
def remainder(num1,num2):
    num3 = num1 % num2
    return num3
for i in range(0,T):
    x, y = int(input()), int(input())
    z = remainder(x,y)
    # x = int(input())
    # y = int(input())
    # z = x % y 
    print(z)