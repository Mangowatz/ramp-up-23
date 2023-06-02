#return final price after discount
import sys

def discount(msrp, discount):
    discount/=100
    output = msrp*(1-discount)
    return output

num1 = sys.argv[1]
num2 = sys.argv[2]
num1 = int(num1)
num2 = int(num2)
print(discount(num1,num2))