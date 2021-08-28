'''
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

'''

def find_short(s):
    # result = []
    # for i in s.split():
    #     result.append(len(i))
    # return min(result)

    # arr = s.split()
    # word = min(arr, key=len)
    # return len(word)

    return min(len(x) for x in s.split(' '))

print(find_short("bitcoin take over the world maybe who knows perhaps"))