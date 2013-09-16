#!/usr/bin/python2

"""Problem 56: Powerful digit sum"""

def main():
    res = 0

    for a in xrange(90, 100):
        for b in xrange(90, 100):
            dsum = sum(map(int, str(a**b)))
            if dsum > res:
                res = dsum
    return res


if __name__ == "__main__":
    print main()
