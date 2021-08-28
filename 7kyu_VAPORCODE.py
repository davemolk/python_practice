'''
https://www.codewars.com/kata/5966eeb31b229e44eb00007a/train/python

Write a function that converts any sentence into a V A P O R W A V E sentence. 
a V A P O R W A V E sentence converts all the letters into uppercase, and adds 
2 spaces between each letter (or special character) to create this V A P O R W A V E 
effect.
'''
def vaporcode(s: str):
    return '  '.join(s.replace(' ', '').upper())
    