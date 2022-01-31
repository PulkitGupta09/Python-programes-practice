T = int(input())
n = []
for i in range(0,T):
    p = int(input())
    n.append(p)        

def sum_of_digit(num):
    tot = 0
    while(num>0):
        dig = num%10
        tot = tot + dig
        num = int(num/10)
    return tot


for i in range(0,T):
    print(sum_of_digit(n[i])) 