n=int(input())
min=int(input())
hour=min//60
hour_left=4-hour
h=hour_left*60
c=0
a=0
y=0
for i in range(1,n+1):
    x=5*i
    y=y+x
    c=c+1
    if y==60:
        a=a+1
        print(a)
    elif y>h:
        c=c-1
        break
print(c)
"or"
#prob=int(input())
