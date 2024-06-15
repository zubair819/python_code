#sub array with max sum, input[2,4,6,-13,9,8,2]
# it is famously called as kadanes algorithm
x=int(input())
l=list(map(int,input().split()))
a=0
r=0
for i in range(len(l)):
    a=a+l[i]
    if a<0:
        a=0
    if r<a:
        r=a
print(r)