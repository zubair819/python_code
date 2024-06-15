#find the equilibrium number and print the number from where you are getting equilibrium number if not found print the middle index value
x=int(input())
l=list(map(int,input().split()))
sum=0
sum1=0
j=0
for i in range(len(l)):
    j=i+1
    sum=sum+l[i]
    while True:
        if j<x:
            sum1=sum1+l[j]
            j=j+1
        else:
            break
    if sum!=sum1:
        sum1=0
    else:
        print(l[i])
        break
    if i==x-1:
        print(x//2)
