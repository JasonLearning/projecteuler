#!/usr/bin/python2

"""Problem 57: Square root convergents"""

from math import log10

def main():
    num, den, cnt = 3, 2, 0

    for _ in xrange(1, 1001):
        if int(log10(num)) > int(log10(den)):
            cnt += 1
        # http://en.wikipedia.org/wiki/Square_root_of_2#Continued_fraction_representation
        num, den = num+2*den, num+den

    return cnt

if __name__ == "__main__":
    print main()
