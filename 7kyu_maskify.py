'''
https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

Your task is to write a function maskify, which changes all but the last four characters into '#'.

'''
# def maskify(cc):
#     if len(cc) <= 4:
#         return cc
#     else:
#         to_mask = len(cc[:-4])
#         return to_mask * '#' + cc[-4:]
    
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

