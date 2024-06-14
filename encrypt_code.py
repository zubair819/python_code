#encrypt code:- in this we take a list of arrays like [321,462,984] and in each values we find the largest number and convert the whole thing into the same value like in 321 3 is largest so we convert it as 333 after doing this process we add and display the result of the whole list
a=list(map(int,input().split()))
l1=[]
r=0
def largest(a):
    x=True
    c=-1
    temp=0
    while x==True:
        if a>0:
            s=a%10
            c=c+1
            if temp<s:
                temp=s
            a=a//10
        else:
            count(c,temp)
            x=False
def count(c,temp):
    result=0
    x=True
    while x==True:
        if c>=0:
            res=(temp*(10**c))
            c=c-1
            result=result+res
        elif c==1:
            continue
        else:
            x=False
    l1.append(result)
for i in a:
    largest(i)
print(l1)
for i in l1:
    r=i+r
print(r)

"or"
"""def process(n):
    mx=-999
    c=0
    ans=0
    while n>0:
        digit=n%10
        if digit>mx:
            mx=digit
        c=c+1
        n=n//10

        while c>0:
            ans=ans*10+mx
            c=c-1"""
