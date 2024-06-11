class main:
    def __init__(self) -> None:
        pass
    def a(self):
        print("this is parent class")
class child1(main):
    def __init__(self) -> None:
        pass
    def b(self):
        print("this is child1 class1 inherits parent main")
s=child1()
s.a()
s.b()

class child2(main):
    def __init__(self) -> None:
        pass
    def c(self):
        print("this is child1 class2 inherits parent main")
s1=child2()
s1.a()
s1.c()

class child3(child2):
    def __init__(self) -> None:
        pass
    def d(self):
        print("this is child1 class2 inherits child2")
s2=child3()
s2.c()
s2.d()



























"""class main:
    def __init__(self,a,b) -> None:
        self.a1=a
        self.b1=b
    def add(self):
        res=self.a1+self.b1
        print(res)
class child(main):
    def __init__(self) -> None:
        pass
    def subs(self):
        res=self.a1-self.b1
        print(res)
a=int(input())
b=int(input())
s=main(a,b)
m=child()
m.add()"""