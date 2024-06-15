#peak element finder :- to find the peak element in the list which is greater than previous element and the next element
x=int(input())
greatest=0
great=0
l=list(map(int,input().split()))
for i in range(1,len(l)-1):
    if l[i]>l[i-1] and l[i]>l[i+1]:
        great=l[i]
    if greatest<great:
        greatest=great
        res=i
print(res)