#!/usr/bin/python2

"""Problem 62: Cubic permutations"""

def main(N=5):
    num, bound = 1, 10
    cubes = {}
    candidates = []

    while True:
        cube = num**3
        key = "".join(sorted(str(cube)))

        if cube > bound: # safe to return a candidate
            if candidates and [ c for c in candidates if len(cubes[c]) == N ]:
                return min(map(min, [ cubes[c] for c in candidates ]))
            bound *= 10

        if key in cubes:
            cubes[key].append(cube)

            if len(cubes[key]) == N:
                candidates.append(key)
        else:
            cubes[key] = [cube]
        num += 1


if __name__ == "__main__":
    print main()
