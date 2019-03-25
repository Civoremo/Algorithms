#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # pass
    # if n == 1 or n == 0:
    #     return 1
    # elif (n == 2):
    #     return 2
    # else:
    #     return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n - 1)
    eat = {1, 2, 3}
    cache = [0 for num in range(n+1)]
    cache[0] = 1
    for i in range(n+1):
        cache[i] += sum(cache[i - x] for x in eat if i - x > 0)
        cache[i] += 1 if i in eat else 0
    return cache[-1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
