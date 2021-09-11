'''
Return the "centered" average of an array of ints, 
which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array.
'''

def centered_ave(nums):
    my_sorted_list = sorted(nums)[1:-1]
    return sum(my_sorted_list)//len(my_sorted_list)


# print(centered_ave([1, 2, 3, 4, 100]))
# print(centered_ave([1, 1, 5, 5, 10, 8, 7]))