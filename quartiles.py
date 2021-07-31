#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
#!/bin/python

def median(nums):
    n=len(nums)
    if n % 2 == 0:
        m=(nums[int(n/2)-1]+nums[int(n/2)])/2
    else:
        m=nums[int(n/2)]
    return m

def quartiles(arr):
    # Write your code here
    arr.sort()    
    q2= median(arr)
    i=len(arr)/2
    ar1=arr[:i]
    q1=median(ar1)
    if len(arr)%2==1:
        ar3=arr[i+1:]
    else:
        ar3=arr[i:]
    q3=median(ar3)
    return (q1,q2,q3)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

