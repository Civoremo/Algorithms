#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # pass
    # buyPrice = lowest purchase price
    # sellPrice = largest price after our purchase price
    # if current int is larger than next int,
    # make int equal to next int as long as next int is not last int
    # subtract largest int from current int (sellPrice - buyPrice = max profit)
    # if lowest int is 2nd to last, subtract from last int

    buyPrice = prices[0]
    sellPrice = prices[1]
    for index, price in enumerate(prices):
        if buyPrice == prices[len(prices)-2]:
            return prices[len(prices)-1] - buyPrice

        if index <= prices[len(prices)-1]:
            if buyPrice > price:
                buyPrice = price
            if (index+1) <= (len(prices)-1) and sellPrice < prices[index+1]:
                sellPrice = prices[index+1]

    return (sellPrice - buyPrice)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
