# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

learning_features=[]
learning_target=[]
data=[]
for i in stdin:
    data.append(i.split())
m=int(data[0][0])
n=int(data[0][1])
data.pop(0)
datan=data[0:n]
dataq=data[n:]
for i in datan:
    line=[]
    learning_target.append(float(i.pop(-1)))
    for j in i:
        line.append(float(j))
    learning_features.append(line)
test_features=[]
q=int(dataq[0][0])
dataq.pop(0)
for i in dataq:
    line=[]
    for j in i:
        line.append(float(j))
    test_features.append(line)    
#print("learning features:{} \n learning target:{} \n test features:{} ".format(learning_features,learning_target,test_features))   
from sklearn import linear_model
lm = linear_model.LinearRegression()
lm.fit(learning_features, learning_target)
a = lm.intercept_
b = lm.coef_
def calculate_y(x,a,b):
    results=[]
    for xi in x:
        result=a
        for i,j in zip(b,xi):
            result=result+i*j
        results.append(result)
    return results
final_results=calculate_y(test_features,a,b)
for i in final_results:
    print(format(i,'.2f')) 
