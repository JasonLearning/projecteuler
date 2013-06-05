#!/usr/bin/python2

from projecteuler import is_pentagonal

def hexagonal_numbers():
    t = 1
    d = 5
    while True:
        yield t
        t += d
        d += 4

def main():
    cnt = 0

    for h in hexagonal_numbers():
        if is_pentagonal(h): # Every hexagonal number is a triangular number
            cnt += 1
            if cnt == 3:
                return h

if __name__ == "__main__":
    print main()