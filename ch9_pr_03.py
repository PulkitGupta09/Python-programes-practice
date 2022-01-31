# def table(num):
#     for j in range(2,21):
#         with open(f'table_of_{j}','w') as f1:
#             for i in range(1,11):
#                 f1.write(f"{num} X {i} = {num*(i)}")

# for num in range(2,21):
#     table(num)    



def table():
    for j in range(2,21):
        with open(f'tables/table_of_{j}.txt','w') as f1:
            for i in range(1,11):
                f1.write(f"{j} X {i} = {j*(i)}\n")

table()




# def table():
#     for j in range(2,21):
#         for i in range(1,11):
#             with open(f'tables/table_of_{j}','w') as f1:
#                 f1.write(f"{j} X {i} = {j*(i)}")

# table()