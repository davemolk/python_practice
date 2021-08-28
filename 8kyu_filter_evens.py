'''
https://www.codewars.com/kata/566dc566f6ea9a14b500007b/train/python

fix given code
'''

def kata_13_december(lst): 
    # return list(filter(lambda x: x%2 != 0, lst))
    return [i for i in lst if i%2 != 0]