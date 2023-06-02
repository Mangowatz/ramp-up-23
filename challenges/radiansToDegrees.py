import sys
from math import pi

def radToPi(rad):
    output = float(rad * 180 / pi)
    return round(output,1)

num = sys.argv[1]
num = float(num)
print(radToPi(num))