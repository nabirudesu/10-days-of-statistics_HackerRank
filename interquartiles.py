#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(nums):
    n=len(nums)
    if n % 2 == 0:
        m=float((nums[int(n/2)-1]+nums[int(n/2)])/2)
    else:
        m=float(nums[int(n/2)])
    return m

def quartiles(arr):
    # Write your code here
    arr.sort()    
    i=int(len(arr)/2)
    ar1=arr[:i]
    q1=median(ar1)
    if len(arr)%2==1:
        ar3=arr[i+1:]
    else:
        ar3=arr[i:]
    q3=median(ar3)
    return (q3-q1)

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    s=[]
    i=0
    j=0
    while (i<len(values)):
        while j<freqs[i]:
            s.append(values[i])
            j+=1
        j=0
        i+=1    
    s.sort()
    iqr=quartiles(s) 
    print(iqr)
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)

