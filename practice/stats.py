import sys

def stat(myList):
    highestNum=myList[0]
    sum = 0
    minimum = myList[0]
    average = 0
    for i in myList:
        if(i>highestNum):
            highestNum=i
        if(i<minimum):
            minimum=i
        sum+=i
    average = sum/len(myList)
    print("High ",highestNum)
    print("Min ",minimum)
    print("Sum ",sum)
    print("Avg. ",average)

myList = [1,45,23,6]
stat(myList)
