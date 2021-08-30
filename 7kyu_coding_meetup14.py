'''
https://www.codewars.com/kata/583952fbc23341c7180002fd/train/python

Your task is to return an object which includes the count of food options selected by the developers on the meetup sign-up form..

given: 
list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
    { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
]

your function should return the following object (the order of properties does not matter):

{ 'vegetarian': 2, 'standard': 1, 'vegan': 1 }
'''
# from collections import Counter
# def order_food(lst): 
#     return Counter(dev['meal'] for dev in lst)

# def order_food(lst):
#     orders = {}
#     for dev in lst:
#         o = dev['meal']
#         if o in orders:
#             orders[o] += 1
#         else:
#             orders[o] = 1

#     return orders

def order_food(lst):
    orders = [dev['meal'] for dev in lst]
    return {o: orders.count(o) for o in orders}



list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
    { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
]

print(order_food(list1))