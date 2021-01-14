#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    i,j,k = 0,0,1
    result = []
    for i in range(len(arr)):
        for j in range(k,len(arr)):
            result.append(abs(arr[i] - arr[j]))
        k += 1
    return min(result)
    #return min(abs(arr[i+1]-arr[i]) for i in range(len(arr)-1))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)