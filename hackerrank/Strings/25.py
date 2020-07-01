# Capitalize!

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.lower()
    l = []
    c_l = []
    iname = ''
    l = s.split(" ")
    print(l)
    for row in l:
        if len(row) == 0:
            iname = ''
            c_l.append(iname)
        elif (97 <= ord(row[0]) <= 122) and len(row) != 0:
            t_l = list(row)
            t_l[0] = str(t_l[0].upper())
            iname = ''.join(t_l)
            c_l.append(iname)
        else:
            iname = row
            c_l.append(iname)
        #c_l.append(iname)
    return ' '.join(c_l)
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
