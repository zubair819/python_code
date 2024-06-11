class cse1:
    def __init__(self,a,b):
        self.a1=a
        self.a2=b
    def add(self):
        res=self.a1+self.a2
        print(res)
    def mul(self):
        res=self.a1*self.a2
        print(res)
a=int(input())
b=int(input())
s=cse1(a,b)
s.add()
s.mul()