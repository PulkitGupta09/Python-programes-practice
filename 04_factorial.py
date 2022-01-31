def factorial(n):
    factorial_1 = 1
    for i in range(n):
        factorial_1 = factorial_1 * (i+1)
    return factorial_1

x = factorial(4)
print(x)