'''
Write a function `hasAllVowels(str)` that takes in a string and returns
true if the string contains every vowel (a, e, i, o, u) and false
otherwise.
Examples:
hasAllVowels('have you gone biking?'); // => true
hasAllVowels('get out of the way, silly'); // => true
hasAllVowels('software engineer'); // => false
hasAllVowels('hello world'); // => false
'''

def all_vowels(string):
    stripped = set(list(string))
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        if vowel not in stripped:
            return False
    return True


print(all_vowels('have you gone biking?'))

print(all_vowels('hello world'))