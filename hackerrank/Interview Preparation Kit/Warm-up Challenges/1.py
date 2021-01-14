#!/bin/python3

# Sock Merchant

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    freq_sock = {}
    for item in ar:
        if item in freq_sock:
            freq_sock[item] += 1
        else:
            freq_sock[item] = 1
    for i in freq_sock:
            socks = int(freq_sock[i] / 2)
            pairs += socks
    return pairs
if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
