# T = int(input())
# num = int(input())
# def firstdigit_calc(num):
#     num = num%10
#     return num

# def lastdigit_calc(num):
#     dig = num
#     while(num>0):
#         dig = num % 10
#         num = int(num/10)
#     return dig
        
# def sum():
#     x = firstdigit_calc(num) + lastdigit_calc(num)
#     return x
# print(sum())    






# def firstdigit_calc(num):
#     num = num%10
#     return num

# def lastdigit_calc(num):
#     dig = num
#     while(num>0):
#         dig = num % 10
#         num = int(num/10)
#     return dig
        
# def sum():
#     x = firstdigit_calc(num) + lastdigit_calc(num)
#     return x
    
# T = int(input())
# for i in range(0,T):
#     num = int(input())
#     print(sum())    




# a=input()
# def sum(a):
#     l=len(a)
#     X=int(a[0])+int(a[l-1])
#     return X

# print(sum(a))




def firstdigit_calc(num):
    num = num%10
    return num

def lastdigit_calc(num):
    dig = num
    while(num>0):
        dig = num % 10
        num = int(num/10)
    return dig
        
def sum(num):
    x = firstdigit_calc(num) + lastdigit_calc(num)
    return x

T = int(input())
n = []
for i in range(0,T):
    p = int(input())
    n.append(p)  

for i in range(0,T):
    print(sum(n[i])) 