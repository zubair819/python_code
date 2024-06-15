#minimum number of key press
x=input()
count=0
i=0
while i<len(x)-1:
    if x[i]=="0" and x[i+1]=="0":
        i=i+2
        count=count+1
    else:
        count=count+1
        i=i+1
if i<len(x):
    count=count+1
print(count)