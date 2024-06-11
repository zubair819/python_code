n=int(input())
def f(n):
    #base
    if n==1:
        return 0
    if n==2:
        return 1
    return f(n-1)+f(n-2)
for i in range(1,n):
    print(f(i))