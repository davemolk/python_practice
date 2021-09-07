'''
Write a function mindPsAndQs(str) that accepts a string of uppercase
letters. The function should return the length of the longest consecutive
streak of the letters 'P' and 'Q'.
Hint: Use two variables. One to track the length of the current streak
and another to track the length of the longest streak so far. This can also be solved using a
single loop!
Nested loops not needed!
Examples:
mindPsAndQs('ENGINEERING'); // => 0
mindPsAndQs('APCDQQPPC'); // => 4
mindPsAndQs('PQPQ'); // => 4
mindPsAndQs('PPPXQPPPQ'); // => 5
'''
def p_and_q(string):
    # current, longest = [0, 0]
    # my_list = list(string)
    # for i in my_list:
    #     if i == 'P' or i == 'Q':
    #         current += 1
    #         if current > longest:
    #             longest = current
    #     else:
    #         current = 0
            
    # return longest
    current, longest = [0, 0]
    my_list = list(string)
    for i in my_list:
        if i == 'P' or i == 'Q':
            current += 1
            longest = max(current, longest)
        else:
            current = 0
            
    return longest


print(p_and_q('PPPXQPPPQ'))
print(p_and_q('ENGINEERING'))
