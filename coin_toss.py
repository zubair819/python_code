#tossing a coin input:-HHHT if 3 consecutive heads comes then it should break vise versa if not then return the tota count for head increase 2 for tale it is -1
str=input()
count=0
c1=0
c=0
for i in str:
    if i=="H":
        count=count+2
        c1=c1+1
        c=0
        if c1==3:
            print("end")
            exit(0)
    elif i=="T":
        count=count-1
        c=c+1
        c1=0
        if c==3:
            print("game end")
            exit(0)
print(count)