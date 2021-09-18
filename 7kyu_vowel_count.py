def get_count(sentence):
    # count = 0
    # for i in list(sentence):
    #     if i in ['a', 'e', 'i', 'o', 'u']:
    #         count += 1
    
    # return count

    # return len(list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], list(sentence))))

    return sum(1 for i in sentence if i in "aeiou")

print(get_count('abracadabra'))