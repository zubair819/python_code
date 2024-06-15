#magic string
x=input()
d={}
res=0
for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
    if res<d[i]:
        res=d[i]
y=len(x)
r=y-res
print(r)