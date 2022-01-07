#Choose any four functions except number 4

# Link: https://github.com/csfeeser/Python/blob/master/challenges/FUNCTIONS%20grab%20bag.md

#returns the maximum of 3 integers
def findMaxOfThreeInts(num1: int, num2:int, num3:int)-> int:
    max = 0
    if (num1 > num2):
        if (num1 > num3):
            max = num1
        elif (num3> num1):
            max = num3
    elif (num2 > num3):
        max = num2
    else:
        max = num3
    return max


#gets sum of all numbers in  a list
def sumAllNumbersInList(list1: list) -> int:
    return sum(list1)

def multiplyAllNumbersInList(list1:list) -> int:
    product = 1 #multiply by 1 to start off
    for num in list1:
        product *= num
    return product
def findEvenNumbersInList(list1:list) -> list:
    evenList=[]
    for num in list1:
        if (num %2 == 0):
            evenList.append(num)
    return(evenList)


print(findMaxOfThreeInts(-5,-4,3))
print(sumAllNumbersInList([1,2,3,4,5]))
print(multiplyAllNumbersInList([-2,-3, 5, -6]))
print(findEvenNumbersInList([1,2,3,4,5,6,7,8,9,10]))