#Objective
#In this challenge, we learn about Poisson distributions. Check out the Tutorial tab for learning materials!

#Task
#A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.

#Input Format

#The first line contains X's mean. The second line contains the value we want the probability for:

#2.5
#5
#If you do not wish to read this information from stdin, you can hard-code it into your program.

#Output Format
#Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e., 1.234 format).

#Solution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from math import factorial,exp
def poisdis(k,lamda):
    return ((lamda**k)/factorial(k))*exp(-lamda)
ls=[]
for i in sys.stdin:
    for j in i.split():
        ls.append(float(j))
k=int(ls[1])
lamda=ls[0]
poisson=poisdis(k,lamda)
print(format(poisson,".3f"))

