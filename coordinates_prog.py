"""a=input()
list=[]
b=list.append(a[0])
c=list.append(a[1])
if b=='a' or 'c' or 'e' or 'g' and c==1 or 3 or '5' or '7':
    print("false")
elif b=='b' or 'd' or 'f' or 'h' and c==2 or '4' or '6' '8':
    print("true")
else:
    print("invalid")
    """

s=input()
e="2468"
g="aceg"
if s[0] in e:
    if s[1] in g:
        print("black")
    else:
        print("white")
else:
    
