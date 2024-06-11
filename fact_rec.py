n=int(input())
def fact(n):
    #base
    if n==0:
        return 1
    return n*fact(n-1)
n=fact(n)
print(n)