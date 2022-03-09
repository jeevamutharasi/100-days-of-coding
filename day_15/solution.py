#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    last_ans = []
    arr = [[] for i in range(n)]
    a = 0
    
    for q in queries:
        t = q[0]
        x = q[1]
        y = q[-1]
        if t == 1:
            i = (x^a)%n
            arr[i].append(y)
        elif t == 2:
            i = (x^a)%n
            a = arr[i][y%len(arr[i])]
            last_ans.append(a)
    
    return(last_ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
