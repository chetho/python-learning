#!/bin/python3

# Counting Valleys
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    steps = 0
    valley = 0
    for foot in s:
        if foot == 'U':
            steps += 1
            if steps == 0:
                valley += 1
        else:
            steps -= 1
    return valley
if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(result)