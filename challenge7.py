'''
In these exercises we will be practicing decomposition by building
multiple functions. Be sure to test each function thoroughly as you go
before moving on to the next problem. Each function will require the
previous to solve.
***********************************************************************/


/***********************************************************************
Write a function `isPrime(number)` that returns a boolean indicating if
`number` is prime or not. Assume `number` is a positive integer.
Examples:
isPrime(2); // => true
isPrime(1693); // => true
isPrime(15); // => false
isPrime(303212); // => false

'''

def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

print(is_prime(7))