import sys
data= sys.stdin.read()
input=data.splitlines()
n=int(input[0])
nums=input[1].split(" ")
i=0
while(i<n): 
    nums[i]=int(nums[i])
    i+=1

def mean(n,nums):
    i=0
    m=0
    while(i<n):
        m=m+nums[i]/n
        i=i+1
    return m

print(mean(n,nums))
    
def median(n,nums):
    nums.sort()
    m=(nums[int(n/2)-1]+nums[int(n/2)])/2
    return m

print(median(n,nums))
    
def mode(n,nums):
    m=0
    for i in nums:
        k=nums.count(i)
        if m<k:
            m=k
            mod=i
    return mod
print(mode(n,nums))

