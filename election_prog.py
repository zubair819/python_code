"""a=int(input())
l=list(map(int,input().split()))
l.sort()
print(l)
l1={}
c=1
j=1
for i in range(0,len(l)):
    if j<len(l):
        if l[i]==l[j]:
            c=c+1
            l1[l[i]]={c}
            j=j+1
        elif l[i]!=l[j]:
            l1[l[i]]={c}
            c=0
            j=j+1
    elif j==len(l):
        c=c+1
        l1[l[i]]={c}
print(l1)"""


n=int(input())
arr=list(map(int,input().split()))
d={}
if n==1:
    print(arr[0])
    exit(0)
else:
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
ans=-1
vals=list(d.items())
print(vals)
vals.sort(reverse=True,key=lambda x:x[1])
print(vals)
if len(vals)==1:
    ans=vals[0][0]
else:
    if vals[0][1]==vals[1][1]:
        ans=-1
    else:
        ans=vals[0][0]
print(ans)