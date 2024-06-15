"""there will be 3 inputs 1. size of the list 2. list elements 3. number to calculate 
lets assume 1. length of list 6 
2. a=[11,12,13,14,15]
3. 6
try to find the factor of the 6 we get [2,3] then we have to add these number with the index value of the given list i.e (2+a[2])+(3+a[3])"""
a=int(input())
b=list(map(int,input().split()))
x=int(input())
l=[]
i=2
while x>1:
    if x%i==0:
        l.append(i)
        x=x//i
    else:
        i=i+1
s=0
print(l)
for i in l:
    s=s+b[i]
print(s)