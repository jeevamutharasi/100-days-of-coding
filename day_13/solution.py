#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    result=[1,1,1,1]
    
    for i in password:
        i=str(i)
        if i in numbers:
            result[0]=0
        elif i in lower_case:
            result[1]=0
        elif i in upper_case:
            result[2]=0
        elif i in special_characters:
            result[3]=0
    minn =result[0]+result[1]+result[2]+result[3]
    return minn if minn+n >6 else 6-(n+minn)+minn
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
