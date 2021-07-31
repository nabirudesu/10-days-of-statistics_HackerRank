#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(x, w):
    # Write your code here
    i=0
    prod_sum=0
    sumw=0
    while (i < len(x)):
        prod_sum=prod_sum+x[i]*w[i]
        sumw=sumw+w[i]        
        i+=1
    return round(prod_sum/sumw,1)
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))
    print(weightedMean(vals, weights))
    

