'''
https://www.codewars.com/kata/58287977ef8d4451f90001a0/train/python

You will be given an array of objects (associative arrays in PHP) representing 
data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return either:

true if all developers in the list code in the same language; or
false otherwise.

'''
# from collections import Counter
# def is_same_language(lst): 
#     count = Counter(dev["language"] for dev in lst)
#     return len(count.keys()) == 1

def is_same_language(lst):
    return len(set(dev["language"] for dev in lst)) == 1




list1 = [
    { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'JavaScript' },
    { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'JavaScript' },
    { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 65, 'language': 'JavaScript' },
]

print(is_same_language(list1))