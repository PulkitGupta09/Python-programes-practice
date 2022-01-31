# Health Management System

clients = ["bilal", "salman", "tariq"]

def getdate():
    import datetime
    return datetime.datetime.now()

date = getdate()

ab = int(input("What you want to do, enter 1 for record entry & 2 for see details of client: "))

while clients:
    if ab == 1:
        client = input("Enter client's name to enter his history: ")
        if client == "bilal":
            choice = int(input("Enter 1 for diet and 2 for exercise: "))
            if choice == 1:
                with open("bilal_diet.txt", "a") as f:
                    f.write(str([str(date)])+": " + input("Enter your diet here: ")+"\n")
            else:
                with open("bilal_ex.txt", "a") as f:
                    f.write(str([str(date)])+": " + input("Enter your exercise here: ")+"\n")

            break

        elif client == "salman":
            choice = int(input("Enter 1 for diet and 2 for exercise: "))
            if choice == 1:
                with open("salman_diet.txt", "a") as f:
                    f.write(str([str(date)])+": " + input("Enter your diet here: ")+"\n")
            else:
                with open("salman_ex.txt", "a") as f:
                    f.write(str([str(date)])+": " + input("Enter your exercise here: ")+"\n")

            break

        elif client == "tariq":
            choice = int(input("Enter 1 for diet and 2 for exercise: "))
            if choice == 1:
                with open("tariq_diet.txt", "a") as f:
                    f.write(str([str(date)])+": " + input("Enter your diet here: ")+"\n")
            else:
                with open("tariq_ex.txt", "a") as f:
                    f.write(str([str(date)])+": " + input("Enter your exercise here: ")+"\n")

            break

        else:
            if client not in clients:
                print("Client doesn't exists. Enter another choice.")
                continue

    else:
        client = input("Enter client's name to see his history: ")
        if client not in clients:
            print("Client doesn't exists. Enter another choice.")
            continue
        else:
            de = input("What you want to see diet/ex? ")
            with open(f"{client}_{de}.txt") as f:
                show = f.read()
                print(show)
                break