# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int 

# print(funcret(1))

# def executor(func):
#     func("this")

# executor(print)    

def dec1(func1):
    def onemore():
        print("before execting")
        func1()
        print("executed")
    return onemore

@dec1
def func():
    print("This is to be printed using decorators")

# func = dec1(func)
func()

