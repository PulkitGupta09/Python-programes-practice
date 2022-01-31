# f = open('game.py','r')
# high = f.read()
# f2 = open('hiscore.txt','r')
# hiscore = f2.read()
# f3 = open('hiscore.txt','w')
# if(hiscore<high):
#     hiscoreupdater = f3.write(high)
# f.close()
# f2.close()
# f3.close()


import random
def game():
    p = random.randint(1,100)
    return p

x = game()
print(x)
# def game():
#     return 600    

# x = game()
# print(x)
with open('hiscore.txt') as f1:
    highscore = int(f1.read())
if(x>highscore):
    with open('hiscore.txt','w') as f2:
        f2.write(str(x))
# else:
#     f2.write(str(highscore))    
  