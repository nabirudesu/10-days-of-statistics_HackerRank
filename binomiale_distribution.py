#part1
#Objective
#In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

#Task
#The ratio of boys to girls for babies born in Russia is . If there is  child born per birth, what proportion of Russian families with exactly  children will have at least  boys?
#Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of  decimal places (i.e.,  format).

#Input Format
#A single line containing the following values:
#1.09 1

#If you do not wish to read this information from stdin, you can hard-code it into your program.

#Output Format
#Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format). 

# here it begins the solution 

#Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

def get_p(ar):
    p=ar[0]/(ar[1]+ar[0])
    return p
def comb(n,x):
    n=factorial(n)/((factorial(x))*(factorial(n-x)))
    return n

def b(x,p,n):
    return comb(n,x)*p**x*(1-p)**(n-x)
x=3
p=get_p([1.09,1])
n=6
m=0
while x<=6:
    m=m+b(x,p,n)
    x+=1

print(format(m,".3f"))



#part2

#Objective
#In this challenge, we go further with binomial distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

#Task
#A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

#No more than 2 rejects?
#At least 2 rejects?
#Input Format

#A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons):

#12 10
#If you do not wish to read this information from stdin, you can hard-code it into your program.

#Output Format
#Print the answer to each question on its own line:
#The first line should contain the probability that a batch of 10 pistons will contain no more than 2 rejects.
#The second line should contain the probability that a batch of 10 pistons will contain at least 2 rejects.
#Round both of your answers to a scale of  decimal places (i.e.,  format).


# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

def get_p(ar):
    p=ar[0]/(ar[1]+ar[0])
    return p
def comb(n,x):
    n=factorial(n)/((factorial(x))*(factorial(n-x)))
    return n

def b(x,p,n):
    return comb(n,x)*p**x*(1-p)**(n-x)
x=0
p=0.12
n=10
m=0
while x<=2 :
    m=m+b(x,p,n)
    x+=1
print(format(m,".3f"))
x=2
m=0
while x<=9:
    m=m+b(x,p,n)
    x+=1
print(format(m,".3f"))
