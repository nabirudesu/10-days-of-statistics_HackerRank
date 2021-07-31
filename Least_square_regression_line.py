# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
from statistics import mean

def SumProd(x,y):
    xy=0
    for i,j in zip(x,y):
        xy=xy+i*j
    return xy
def ProdSums(x,y):
    sx=0
    sy=0
    for i,j in zip(x,y):
        sx=sx+i
        sy=sy+j
    return sx*sy
def SumSquares(x):
    sxx=0
    for i in x:
        sxx=sxx+i**2
    return sxx
def SquareSum(x):
    sx=0
    for i in x:
        sx=sx+i
    return sx**2
def findB(x,y):
    n=len(x)
    return (n*SumProd(x,y)-ProdSums(x,y))/(n*SumSquares(x)-SquareSum(x))
def findA(x,y,b):
    return mean(y)-b*mean(x)
def f(x,a,b):
    return b*x+a
x=[]
y=[]
for i in stdin:
    k=0
    ls=i.split()
    while k<2:
        if k%2==0:
            x.append(int(ls[k]))
        else:
            y.append(int(ls[k]))
        k+=1
b=findB(x,y)
a=findA(x,y,b)
X=80
print(f(X,a,b))

