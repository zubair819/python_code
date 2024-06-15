#pizza party there will be two inputs 1.number of pizza 2. number of people in party, to find the number of people that has to be increased so that every one gets an equal number of pizza after that add that number and print it as a result
x,y=map(int,input().split())
x1=True
ans=y
while x1==True:
    if x%y==0:
         ans=y
         x1=False
    elif x%y!=0:
        y=y+1
s=0
while ans>0:
    digit=ans%10
    s=s+digit
    ans=ans//10
print(s)