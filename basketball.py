inp1=int(input())
arr=list(map(int,input().split()))
inp2=int(input())
mx=-1
for i in range(0,len(arr)-inp2+1):
    temp=arr[i:i+inp2]
    k,s=1,0
    for j in temp:
        s+=(j*k)
        k+=1
    if s>mx:
        mx=s
print(mx)
