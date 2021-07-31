# Enter your code here. Read input from STDIN. Print output to STDOUT
#A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?
from math import sqrt,erf

def cumulNormDist(x,segma,mu):
    z=(x-mu)/(segma*sqrt(2))
    return 0.5+0.5*(erf(z))

max_weight=9800
n=49
mu=205
std_dev=15
nmu=n*mu
nstd_dev=sqrt(n)*std_dev

p1=cumulNormDist(max_weight,nstd_dev,nmu)
print(format(p1,".4f"))




#challenge 2
#The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of 2.4 and a standard deviation of 2.0.
#A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt,erf

def cumulNormDist(x,segma,mu):
    z=(x-mu)/(segma*sqrt(2))
    return 0.5+0.5*(erf(z))

max_tickets=250
n=100
mu=2.4
std_dev=2
nmu=n*mu
nstd_dev=sqrt(n)*std_dev

p1=cumulNormDist(max_tickets,nstd_dev,nmu)
print(format(p1,".4f"))
