#Objective
#In this challenge, we learn about normal distributions. Check out the Tutorial tab for learning materials!

#Task
#In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the #probability that a car can be assembled at this plant in:

#Less than 19.5 hours?
#Between 20 and 22 hours?


# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from math import exp,factorial,sqrt,pi,erf

#def normdist(x,segma,mu):
 #   return (1/(segma*sqrt(2*pi)))*exp(-(x-2)**2/(2*segma**2))

def cumulNormDist(x,segma,mu):
    z=(x-mu)/(segma*sqrt(2))
    return 0.5+0.5*(erf(z))

ls=[]
for line in sys.stdin:
    for j in line.rstrip().split():
        ls.append(float(j))
segma=ls[1]
mu=ls[0]
x1=ls[2]
x2=ls[3]
y2=ls[4]
p1=cumulNormDist(x1,segma,mu)
p2=cumulNormDist(y2,segma,mu)-cumulNormDist(x2,segma,mu)
print(format(p1,".3f"))
print(format(p2,".3f"))

#Seconde challenge
import sys
from math import exp,factorial,sqrt,pi,erf

#def normdist(x,segma,mu):
 #   return (1/(segma*sqrt(2*pi)))*exp(-(x-2)**2/(2*segma**2))

def cumulNormDist(x,segma,mu):
    z=(x-mu)/(segma*sqrt(2))
    return 0.5+0.5*(erf(z))

ls=[]
for line in sys.stdin:
    for j in line.rstrip().split():
        ls.append(float(j))
segma=ls[1]
mu=ls[0]
x1=ls[2]
x2=ls[3]

p1=1-cumulNormDist(x1,segma,mu)
p2=1-cumulNormDist(x2,segma,mu)
p3=1-p2
print(format(p1*100,".2f"))
print(format(p2*100,".2f"))
print(format(p3*100,".2f"))

