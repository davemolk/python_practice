'''
https://www.codewars.com/kata/582746fa14b3892727000c4f/train/python

You will be given an array of objects (hashes in ruby) representing data about developers who have signed up to attend the coding meetup that you are organising for the first time.

Your task is to return the number of JavaScript developers coming from Europe.

'''
def count_developers(lst):
    # result = []
    # for dev in lst:
    #     if dev["continent"] == "Europe":
    #         result.append(dev)
    # return len(result)

    # return len(list(filter(lambda dev: dev["continent"] == "Europe" and dev["language"] == "JavaScript", lst)))

    return sum(dev["continent"] == "Europe" and dev["language"] == "JavaScript" for dev in lst)


list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
    { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
    { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Europe', 'age': 35, 'language': 'JavaScript' },
    { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
]

        
print(count_developers(list1))