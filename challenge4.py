'''
// Write a function `everyOtherWord(sentence)` that takes in a sentence and returns
// an array containing every other word in that sentence.
//
// Examples:
//
// everyOtherWord('hello how are you doing on this lovely day?'); // => [ 'hello', 'are', 'doing', 'this', 'day?' ]
// everyOtherWord('the weather is wonderful'); // => [ 'the', 'is' ]
'''

def every_other_word(sentence):
    # words = sentence.split()
    # evens = list(filter(lambda index: index%2 == 0, range(len(words))))
    # return [words[i] for i in evens]

    words = sentence.split()
    return words[::2]
    

print(every_other_word('hello how are you doing on this lovely day?'))