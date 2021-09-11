'''
return True if array has two consecutive 2s, otherwise return false
'''

import re

def has22(nums):
    pattern = r"[2]{2}"
    regex = re.compile(pattern)
    match = regex.findall(("".join(str(el) for el in nums)))
    return True if match else False

print(has22([1, 2, 2]))