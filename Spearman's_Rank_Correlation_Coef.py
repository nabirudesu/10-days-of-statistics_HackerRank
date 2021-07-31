# Enter your code here. Read input from STDIN. Print output to STDOUT
def spears_corr(rx,ry):
    i=0
    n=len(rx)
    summ=0
    while i < n:
        summ=summ+(rx[i]-ry[i])**2
        i+=1
    return 1-(6*summ)/(n*((n**2)-1))
import sys
ls=[]
for i in sys.stdin:
    ls.append(i.split())
n=ls[0][0]
x=[]
y=[]
for i in ls[1]:
    x.append(float(i))
for i in ls[2]:
    y.append(float(i))
rx=[]
ry=[]
for i in x:
    rx.append(sorted(x).index(i)+1)
for i in y:
    ry.append(sorted(y).index(i)+1)
p=spears_corr(rx,ry)
print(round(p,3))
