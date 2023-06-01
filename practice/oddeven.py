import sys

def ooe(num:int):
    num = int(sys.argv[1])
    result:float = num%2
    #print(result)
    if(result==0):
        return True
    return False
if(ooe(int(sys.argv[1]))):
    print("This number is even")
else:
    print("This number is odd")