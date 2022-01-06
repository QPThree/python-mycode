# Lab 28
foo = open("files/ourfile.txt","w")
for i in range(4):
    print(i)
for num in range(5):
    print(num, end=" ")
fruitbowl = ["apple", "pear", "grapes"]
for fruit in fruitbowl:
    print(fruit, file=foo) #this will write to the file 
foo.close()