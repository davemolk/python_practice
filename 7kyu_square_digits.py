'''
https://www.codewars.com/kata/546e2562b03326a88e000020

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''
def square(num):
    # result = []
    # for i in list(str(num)):
    #     result.append(str(int(i)**2))
    # return int(''.join(result))

    return int(''.join(str(int(i)**2) for i in list(str(num))))



print(square(9119))