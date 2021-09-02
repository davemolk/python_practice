'''
Write a function missyElliot(array) that takes in an array of strings 
and returns a sentence string that flip each string element in the array 
and reverses the entire array. 

Examples:

arr = [ 'siht', 'esrever', 'dna', 'pilf', 'attog', 'uoY' ];

lyricsArr = ['ti', 'esrever', 'dna', 'ti', 'pilf', 'nwod', 'gnaht', 'ym', 'tup', 'I'];

missyElliot(arr); // You gotta flip and reverse this

missyElliot(lyricsArr); // I put my thang down flip it and reverse it
'''
def m_e(lst):
    missy = []
    lst.reverse()
    for word in lst:
        missy.append(word[::-1])
    return ' '.join(missy)


arr = [ 'siht', 'esrever', 'dna', 'pilf', 'attog', 'uoY' ]

lyricsArr = ['ti', 'esrever', 'dna', 'ti', 'pilf', 'nwod', 'gnaht', 'ym', 'tup', 'I']

m_e(arr)
