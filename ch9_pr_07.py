with open('log.txt','r') as f1:
    count = 0
    for i in range(1,100):
        lne = f1.readline()
        count = count + 1 
        if 'python' in lne:
            print(f'python is present in the line {count}')    