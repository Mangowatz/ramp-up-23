#return the sum of two numbers
import sys

def sum(int1:int, int2:int):
    output:int = int1+int2
    return output

num1 = sys.argv[1]
num2 = sys.argv[2]
num1 = int(num1)
num2 = int(num2)
print(sum(num1,num2))