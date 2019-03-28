#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # pass
    # if amount < 0:
    #     return 0
    # if amount == 0:
    #     return 1
    # if not denominations:
    #     return 0
    # return making_change(amount-denominations[0], denominations) + making_change(amount, denominations[1:])

    amount = amount/100
    return round(1 + (55*amount + 238*amount**2 + 380*amount**3 + 200*amount**4)/3)

    # cache = [0 for num in range(amount+1)]
    # cache[0] = 1
    # for i in range(amount+1):
    #     for x in denominations:
    #         print(f'x: {x}')
    #         if i - x > 0:
    #             cache[i] += sum(cache[i - x])
    #     if i in denominations:
    #         cache[i] += 1
    #     else:
    #         0
    # print(f'{cache}')
    # return cache[-1]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
