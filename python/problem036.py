#!/usr/bin/env python

"""Problem 36: Double-base palindromes"""

from utils import is_palindrome


# generate a palindrome in base 2
def mk_palindrome(n, oddlength):
    r = n
    if oddlength: n >>= 1
    while n:
        r = (r << 1) + (n & 1)
        n >>= 1
    return r

def palindromes(oddlength, lim=1000000):
    i = 1
    p = mk_palindrome(i, oddlength)
    while p < lim:
        if is_palindrome(p, 10):
            yield p
        i += 1
        p = mk_palindrome(i, oddlength)

def main():
    # sum of the palindromes of the form xyz+yx and xyz+zyx
    return sum(p for p in palindromes(True)) + sum(p for p in palindromes(False))

if __name__ == "__main__":
    print(main())
