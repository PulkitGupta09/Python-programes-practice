def sumofnatural(n):
    if(n == 1):
        return 1
    else:    
        sum = n
        sum =  sum +sumofnatural(n-1)
        return sum
x = sumofnatural(4)
print(x)        