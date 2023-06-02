import sys

def factByLoop(num:int):
    output=1;
    for i in range(1,num+1):
        output=output*i
    return output
def factByRec(num, output):
    if(num==1):
        return 1
    temp = num-1
    output = num*factByRec(temp,output)

    return output
def factByRecursion(input):
    if(input==0):
        return 1
    return factByRec(input,input)

input = sys.argv[1]
input = int(input)
print(factByLoop(input))
print(factByRecursion(input))

# print("Factorial via loop: ",factByLoop(input))
# print("Factorial via recurion: ",factByLoop(input))