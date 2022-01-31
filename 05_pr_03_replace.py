letter = ''' Dear <|NAME|>,
You are Selected!
DATE: <|DATE|>
'''
name = input("Enter your name")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)

