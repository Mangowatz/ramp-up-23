import sys

def rev(s:str):
    newStr = s[::-1]
    return newStr
def vowel(s:str):
    vow = {'a','e','i','o','u'}
    count = 0
    for i in s:
        if(i in vow):
            count+=1
    return count

string = sys.argv[1]
print("Reversed: ",rev(string))
print("Vowels: ",vowel(string))
        