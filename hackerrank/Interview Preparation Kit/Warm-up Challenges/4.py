#!/bin/python3

# Repeated String
import math
import os
import random
import re
import sys
import pdb

# Complete the repeatedString function below.
def repeatedString(s, n):
    i,j = n // len(s), n % len(s)
    if len(s) == 1:
        return s.count("a") * n
    else:
        return s.count("a") * i + s[:j].count("a")
if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(str(result) + '\n')
