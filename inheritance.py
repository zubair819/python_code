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
