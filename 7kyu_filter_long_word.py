'''
https://www.codewars.com/kata/5697fb83f41965761f000052

Write a function filter_long_words that takes a string sentence and an integer n.

Return a list of all words that are longer than n.

'''

def filter_long_words(sentence, n):
    # result = []
    # for word in sentence.split():
    #     print(word)
    #     if len(word) > n:
    #         result.append(word)

    # return result
    
    return list(filter(lambda x: len(x) > n, sentence.split()))

    



print(filter_long_words("The quick brown fox jumps over the lazy dog", 4))