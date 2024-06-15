#finding the unique product of tripletes which match to my result 
x=int(input())
l=list(map(int,input().split()))
m=int(input())
count=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if l[i]*l[j]*l[k]==m:
                #print(l[i],l[j],l[k])
                count=count+1
print(count)