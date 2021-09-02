'''
Write a function oddWordsOut(sentence) that takes in a sentence string
and returns the sentence where words with an odd number of characters
are removed.
Examples:
oddWordsOut('go to the store and buy milk'); // => 'go to milk'
oddWordsOut('what is the answer'); // => 'what is answer'

'''
def odd(sentence):
    words = sentence.split()
    return ' '.join(list(filter(lambda word: len(word) % 2 == 0, words)))

print(odd('go to the store and buy milk'))