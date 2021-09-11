def count_evens(nums):
    # return len(list(filter(lambda x: x%2 == 0, nums)))
    count = 0
    for n in nums:
        if n%2 == 0:
            count += 1
    return count

print(count_evens([2, 1, 6, 3, 4]))