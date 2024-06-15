#target sum 
l=list(map(int,input().split()))
x=int(input())
l.sort()
l1=[]
def find(a,b):
    return a+b
i=0
j=len(l)-1
while i<j:
    y=find(l[i],l[j])
    if y>x:
        j=j-1
    else:
        i=i+1
    if y==x:
        l1.append(i)
        l1.append(j)
        i=i+1
        j=j-1
print(l1)

"""for i in range(len(l)):
    j=i+1
    if j<len(l):
        y=find(l[i],l[j])
    if y==x:
        l1.append(i)
        l1.append(j)"""