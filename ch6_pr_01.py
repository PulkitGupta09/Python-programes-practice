num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))
num4 = int(input("Enter the fourth number : "))

if(num1>num2 and num1>num3 and num1>num4):
    print("num1 is greatest")
elif(num2>num1 and num2>num3 and num2>num4):
    print("num2 is greatest")
elif(num3>num2 and num3>num1 and num3>num4):
    print("num3 is greatest")
else:
    print("num4 is greatest")