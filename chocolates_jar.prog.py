# dividing chocolate jar problem give the number of chocolate in the list and there are 3 members who collect the chocolate

l=list(map(int,input().split()))
n=int(input())
x=0
res=0
print(1//3)
for i in range(len(l)):
    if l[i]%3==0:
        x=int(l[i]/3)
        res=res+x
    else:
        x=int((l[i]//3)+1)
        res=res+x
print(res)