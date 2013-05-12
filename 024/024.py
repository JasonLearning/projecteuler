#!/usr/bin/python2

from math import factorial

def nthPerm(s, n):
    if len(s) < 2:
        return s
    quot, n = divmod(n, factorial(len(s)-1))
    return s[quot] + nthPerm(s[:quot] + s[quot+1:], n)

print nthPerm('0123456789', 999999)