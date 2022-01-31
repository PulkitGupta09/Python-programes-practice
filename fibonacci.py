def febonac(n):
    x = 2
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return febonac(n-1) + febonac(n-2)

print(febonac(8))