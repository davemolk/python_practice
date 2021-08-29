'''
https://www.codewars.com/kata/5828713ed04efde70e000346/train/python

You will be given an array of objects (associative arrays in PHP) representing 
data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return an object (associative array in PHP) which includes the count of each 
coding language represented at the meetup.

'''
# from collections import Counter
# def count_languages(lst): 
#     return Counter(dev["language"] for dev in lst)
    
def count_languages(lst):
    # count = {}
    # for dev in lst:
    #     l = dev["language"]
    #     if l in count: 
    #         count[l] += 1
    #     else:
    #         count[l] = 1
    # return count

    language = [dev["language"] for dev in lst]
    return {i: language.count(i) for i in language}


list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
    { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
]

print(count_languages(list1))