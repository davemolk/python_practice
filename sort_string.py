'''
Create a function that takes a string and returns the string with the letters 
in alphabetical order (ie. hello becomes ehllo), Assume numbers and punctuation 
symbols will not be included in the string.


Give me a string to alphabetize
supercalifragilisticexpialidocious
Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux

'''
def alpha():
    # my_string = input('Give me a string to alphabetize ')
    # result = (list(my_string))
    # result.sort()
    # print(''.join(result))

    my_string = input('Give me a string to alphabetize: ')
    result = (list(my_string))
    print(''.join(sorted(result)))


alpha()