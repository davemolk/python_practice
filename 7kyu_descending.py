'''
https://www.codewars.com/kata/5467e4d82edf8bbf40000155

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.

'''

def descending_order(num):
    # return int(''.join(sorted(list(str(num)))[::-1]))
    return int("".join(sorted(str(num), reverse=True)))


print(descending_order(1346034))
print(descending_order(123456789))