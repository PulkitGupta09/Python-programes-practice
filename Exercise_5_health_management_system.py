import time
start = time.time()
def getdate():
    import datetime
    return datetime.datetime.now()

def Food_Details_maker(clients_name,detailed):
    with open(f"{clients_name}.txt","a") as f:
        # f.write(str(getdate()) + "  :  " + detailed  + "\n")
        f.write(f"{str(getdate())} : {detailed} \n")
        

def Exercise_Details_maker(clients_name,detailed):
    with open(f"{clients_name}.txt","w") as f:
        f.write(str(getdate()) + "  :  " + detailed  + "\n")


def Food_Details_retriever(clients_name):
    with open(f"{clients_name}.txt","rt") as f:
        x = f.read()
        print(x)


def Exercise_Details_retriever(clients_name):
    with open(f"{clients_name}.txt","r") as f:
        # f.read(f"{clients_name}.txt") <--- Wrong method
        x = f.read()
        print(x)


print("Press 1:: to log the data or Press 2:: to retreive the data")
datachecker = int(input())
print("Enter the number for the clients below::")
print("1->Rohan\t 2->Harry\t 3->Ritwik\t")
clients_name = input()
print("Enter digit for the options as 1. Food\t 2. Exercise\t")
option_name = int(input())

if(datachecker == 1 and option_name==1):
    detailed = input("Enter the list of food you have eat")
    Food_Details_maker(clients_name,detailed)
elif(datachecker == 1 and option_name==2):
    detailed = input("Enter the list of Exercise you have done")
    Food_Details_maker(clients_name,detailed)
elif(datachecker == 2 and option_name==1):
    print("The detailed analysis of food is")
    Food_Details_retriever(clients_name)
elif(datachecker == 2 and option_name==2):
    print("The detailed analysis of your exercise is:")
    Food_Details_retriever(clients_name)

end = time.time()

print(f"time for the program is {end-start}")

