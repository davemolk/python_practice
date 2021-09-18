'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
'''

from collections import Counter

def find_it(seq: list):
    # count = Counter(i for i in seq)
    # for key in count:
    #     if count[key] % 2 != 0:
    #         return key

    # return [k for k, v in Counter(seq).items() if v % 2 != 0][0]
    # for i in seq:
    #     if seq.count(i) % 2 != 0:
    #         return i
    
    counts = {}
    for i in seq:
        if i not in counts:
            counts[i] = 0
        
        counts[i] += 1
        
    for i, i_count in counts.items():
        if i_count % 2 != 0:
            return i

print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
