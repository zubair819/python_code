#finding missing and repeting values
a1=int(input("enter the number of rows"))
b=int(input("enter the number for column"))
a=[]
count=1
ans=[]
d={}
#taking input fron the keyboard
for i in range(a1):
    sub=[]
    for j in range(b):
        ele=int(input())
        sub.append(ele)
    a.append(sub)
#looping to count the number of repeted values
for i in range(a1):
    for j in range(b):
        c=a[i][j]
        if a[i][j] in d:
            count=count+1
            d[c]={count}
            if count==2:
                ans.append(a[i][j])
        else:
            d[c]={1}
#to find the missing value in the dictionary
for i in range(1,a1**2+1):
    if i not in d:
        ans.append(i)
print(ans)
