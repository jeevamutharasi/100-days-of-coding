
import math
import os
import random
import re
import sys
from datetime import datetime 

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_data = "%a %d %b %Y %H:%M:%S %z"
    a = datetime.strptime(t1,format_data)
    b = datetime.strptime(t2,format_data)
    out = int(abs(a-b).total_seconds())
    return str(out)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
