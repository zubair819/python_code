#to find the maimum number of travers in the list till the negative value occurs [1 2 6 -5] then the ans should be 9
l=list(map(int,input().split()))
l1=[]
sum=0
for i in range(len(l)):
    if l[i]>0:
        sum=sum+l[i]
    else:
        l1.append(sum)
        sum=0
    if i==len(l)-1:
        l1.append(sum)
print(max(l1))

'or'

a=list(map(int,input().split()))
max=-1
s=0
for i in a:
    s=s+i
    if s>max:
        max=s
print(max)