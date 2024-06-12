a=int(input("enter the number"))
n1=a
org=a
ans=0
count=0
while a>0:
    count=count+1
    a=a//10
while n1>0:
    digit=n1%10
    p=digit**count
    count=count-1
    ans=ans+p
    n1=n1//10
if ans==org:
    print("ams")
else:
    print("not ams")