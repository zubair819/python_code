#the next prime number
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num=int(input())
k=num+1
while True:
    if isprime(k):
        print(k)
        break
    k=k+1

"""class main:
    def prime(self,b):
        flag=False
        for i in range(2,b):
            if (b%i)==0:
                flag=True
                break
        if flag:
            print("not a prime")
            return b
        else:
            print("prime")
            return 0
    def calculating(self):
        a=int(input())
        a=a+1
        c=s.prime(a)
        d=c
        if c>0:
            print(c)
            c=c+1
            s.prime(c)
        else:
            print(a)
s=main()
s.calculating()"""
