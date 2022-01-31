
# if(num == 1):
#     print("number is prime number")
# else:
#     i = 2
#     while(num > i):
#         if(num % i == 0):
#             print("num is not prime number")
#             i = i+1
#         else:
#             print("Number is prime number")    
#             i = i+1



# num = int(input("Enter the number"))
# if(num == 1):
#      print("number is prime number")
# else:
#      i=2
#      while(num>i):
#          if(num % i != 0):
#             i = i+1
#      print("Num is prime") 





# num = int(input("Enter the number"))
# if(num == 1):
#      print("number is prime number")
# else:
#     i=2
#     while(num>i):
#         if(num % i == 0):
#             print("num is not prime")
#             break
#             i = i+1
#         else:
#             i = i+1
#             pass   
            

# num = int(input("Enter the number"))
# for i in range(2,num):
#     print(i)


num = int(input("Enter the number"))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime  = False
        break
if prime:
    print("The number is prime")
else:
    print("This number is not prime")    