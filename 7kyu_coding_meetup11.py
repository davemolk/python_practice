'''
https://www.codewars.com/kata/582ba36cc1901399a70005fc/train/python

Given the following input array:

list1 = [
  { 'firstName': 'Maria', 'lastName': 'Y.', 'country': 'Cyprus', 'continent': 'Europe', 'age': 30, 'language': 'Java' },
  { 'firstName': 'Victoria', 'lastName': 'T.', 'country': 'Puerto Rico', 'continent': 'Americas', 'age': 70, 'language': 'Python' },
]

write a function that returns the average age of developers (rounded to the nearest integer). 
In the example above your function should return 50 (number).

'''

def get_average(lst): 
    return round(sum(dev['age'] for dev in lst) / len(lst))



list1 = [
    { 'firstName': 'Maria', 'lastName': 'Y.', 'country': 'Cyprus', 'continent': 'Europe', 'age': 30, 'language': 'Java' },
    { 'firstName': 'Victoria', 'lastName': 'T.', 'country': 'Puerto Rico', 'continent': 'Americas', 'age': 70, 'language': 'Python' },
]

print(get_average(list1))