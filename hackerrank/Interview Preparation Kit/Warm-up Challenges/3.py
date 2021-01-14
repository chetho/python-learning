#!/bin/python3

# Jumping on the Clouds
import math
import os
import random
import re
import sys
import pdb

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    counter = 0
    i,j = 0,1
    while (j < n):
        if (j == n - 1) and c[j] != 1:
            counter += 1
            return counter
        if c[j] == 0 and c[j+1] == 0:
            i = j + 1
            j = i + 1
            counter += 1
        elif c[j] == 0 and c[j+1] == 1:
            i += 1
            j = i + 1
            counter += 1
        elif c[j] == 1 and c[j+1] == 0:
            i = j + 1
            j = i + 1
            counter += 1
        #elif c[j] == 1 and c[k] == 1:
        #    i = k + 1
        #    j = i + 1
        #    k = j + 1
        else:
            counter += 1
        #pdb.set_trace()
    return counter
if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)

