#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # we need to check if n is less than zero or if if it is zero
    # use recursion until n is zero and add results up to give us the answer
    #
    # if n < 0:
    #     return 0
    # elif n == 0:
    #     return 1
    # else:
    #     print(
    #         f'1step: {eating_cookies(n - 1)},\n2step: {eating_cookies(n - 2)},\n3step: {eating_cookies(n - 3)}\n')
    #     return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

    # pass
    eat = {1, 2, 3}
    cache = [0 for num in range(n+1)]
    cache[0] = 1
    for i in range(n+1):
        cache[i] += sum(cache[i - x] for x in eat if i - x > 0)
        # print(f'cache at i({i}): {cache[i]}')
        cache[i] += 1 if i in eat else 0
    # print(f'{cache}')
    # print(f'last item: {cache[-1]}')
    return cache[-1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
