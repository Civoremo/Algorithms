#!/usr/bin/python

import sys


def rock_paper_scissors(n):
  # declare our variables that will hold our outcome and our list
    outcome = []
    actions = ['rock', 'paper', 'scissors']

  # recursively
  # for each action in actions; run recursion to add action of those actions until n == 0
  # when n == 0; append the result to our outcomes
  # first action is 'rock'
  # run recursion: passing n-1, add current action to result
  # if n-1 != 0; run recursion again by passing n-1, adding current action to result
  # if n-1 == 0; append result to our outcome and break recursion
  #
  #                               n = 2
  #                             for each action
  #                               1. rock
  #                                  |
  #                          recursion(n=1, [rock])
  #                                   |
  #          -------------------for each action--------------
  #          |                       |                      |
  #         rock                   paper                scissors
  #          |                       |                      |
  #   recursion(n=0,           recursion(n=0,           recursion(n=0,
  #             [rock, rock])            [rock,paper])            [rock,scissors])
  #          |                       |                      |
  #     outcome.append          outcome.append          outcome.append
  #
    def find_combinations(rounds, result=[]):
        if rounds == 0:
            outcome.append(result)
            return
        for action in actions:
            find_combinations(rounds - 1, result + [action])

    find_combinations(n, [])
    return outcome


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
