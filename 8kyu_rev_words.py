'''
https://www.codewars.com/kata/51c8991dee245d7ddf00000e

Complete the solution so that it reverses all of the words 
within the string passed in.

'''

def reverse_words(s):
    # return ' '.join(list(reversed(s.split())))
    return ' '.join(s.split(' ')[::-1])

print(reverse_words("The greatest victory is that which requires no battle"))