# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def mean(nums):
    i=0
    m=0
    while(i<len(nums)):
        m=m+nums[i]/n
        i=i+1
    return m
def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mn=0
    minus_sum=0
    mn=mean(arr)
    for item in arr:
        minus_sum=minus_sum+(item-mn)*(item-mn)
    stdev=math.sqrt(minus_sum/len(arr))
    return stdev

import sys
ls=[]
for i in sys.stdin:
    ls.append(i.split())
x=[]
y=[]
for i in ls[1]:
    x.append(float(i))
for i in ls[2]:
    y.append(float(i
    ))
n=int(ls[0][0])
mux=mean(x)
segmax=stdDev(x)
muy=mean(y)
segmay=stdDev(y)
i=0
p=0
while i<10:
    p=p+(x[i]-mux)*(y[i]-muy)
    i+=1
pear=p/(n*segmax*segmay)

print(round(pear,3))
