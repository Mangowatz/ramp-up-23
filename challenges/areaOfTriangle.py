#return area of triangle
import sys

def area(int1:int, int2:int):
    output = .5*int1*int2
    return output

num1 = sys.argv[1]
num2 = sys.argv[2]
num1 = int(num1)
num2 = int(num2)
print(area(num1,num2))