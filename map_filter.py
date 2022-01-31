# numbers = ["3","56","78"]
# numbers = list(map(int,numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])


# print(numbers)    

list1 = [1,2,3,4,5,6,7,8,9]
def is_greater_4(num):
    return num>4

greater_than_4 = list(filter(is_greater_4,list1))
print(greater_than_4)