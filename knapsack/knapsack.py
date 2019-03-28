#!/usr/bin/python

import sys
from collections import namedtuple
from functools import lru_cache

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    pass
    # keep grabbing items and place in bag if capacity allows
    # recursively fill bag with each combination of items
    # check which has the most value when filled
    @lru_cache(maxsize=None)
    def bestvalue(i, j):
        if j < 0:
            return float('-inf')
        if i == 0:
            return 0
        index, size, value = items[i - 1]
        return max(bestvalue(i - 1, j), bestvalue(i - 1, j - size) + value)

    j = capacity
    result = []
    for i in reversed(range(len(items))):
        if bestvalue(i + 1, j) != bestvalue(i, j):
            result.append(items[i])
            j -= items[i][1]
    result.reverse()

    totalValue = 0
    chosen = []
    for item in result:
        totalValue += item[2]
        chosen.append(item[0])

    finalResult = {'Value': totalValue, 'Chosen': chosen}
    bestvalue(len(items), capacity), result

    return finalResult


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
