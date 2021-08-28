'''
https://www.codewars.com/kata/5866fc43395d9138a7000006/train/python

Given a string, write a function that returns the string with a question mark ("?") 
appends to the end, unless the original string ends with a question mark, in which case, returns the original string.

'''

def ensure_question(s):
    if len(s) == 0:
        return "?"
    else:
        return s if s[-1] == "?" else s + "?"