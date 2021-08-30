'''
https://www.codewars.com/kata/58291fea7ff3f640980000f9/train/python

You will be given a sequence of objects (associative arrays in PHP) representing data about developers 
who have signed up to attend the next coding meetup that you are organising.

Your task is to return:

true if all of the following continents / geographic zones will be represented by at least one developer: 
'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'.
false otherwise.

'''
# from collections import Counter
# def all_continents(lst): 
#     count = Counter(dev["continent"] for dev in lst)
#     return True if len(count) == 5 else False

def all_continents(lst): 
    return len(set(dev["continent"] for dev in lst)) == 5

list1 =  [
    { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
    { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
    { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
    { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
    { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
]

print(all_continents(list1))