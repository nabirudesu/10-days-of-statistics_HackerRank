#Objective
#In this challenge, we learn about geometric distributions. Check out the Tutorial tab for learning materials!

#Task
#The probability that a machine produces a defective product is 1/3 . What is the probability that the First defect occurs the  5th item produced?

#Input Format
#The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of #being the first defect for:
#1 3
#5
#If you do not wish to read this information from stdin, you can hard-code it into your program.

#Output Format
#Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e., 1.234 format).

#Solution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


def geodis(x,p):
    return ((1-p)**(x-1))*p

def getP(inputs):
    return  inputs[0]/inputs[1]

inputs=[]
for line in sys.stdin:
    l=line.split()
    for i in l:
        inputs.append(int(i))

geo=geodis(inputs[2],getP(inputs))
print(format(geo,".3f"))





#part2
#Objective
#In this challenge, we go further with geometric distributions. We recommend reviewing the Geometric Distribution tutorial before attempting this challenge.

#Task
#The probability that a machine produces a defective product is 1/3 . What is the probability that the  defect is found during the first 5 inspections?

#Input Format
#The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of the first defect being discovered by:
#1 3
#5
#If you do not wish to read this information from stdin, you can hard-code it into your program.

#Output Format
#Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e., 1.234 format).
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def geodis(x,p):
    return ((1-p)**(x-1))*p

def getP(inputs):
    return  inputs[0]/inputs[1]


inputs=[]
for i in sys.stdin:
    for j in i.split():
        inputs.append(int(j))
n=inputs[2]
p=getP(inputs)
i=1
geo=0
#the probability that defect occurs at ith trial 
while i<=n:
    geo = geo +geodis(i,p)
    i+=1
print(format(geo,".3f"))

