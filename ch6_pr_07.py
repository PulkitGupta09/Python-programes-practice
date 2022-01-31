name = input("Enter the name : \n")
sentence = "i am Pulkit Gupta and hello world"
sentence = sentence.lower()
if(name in sentence):
    print(name + " is present in the string")
else:
    print("Not present in the string")