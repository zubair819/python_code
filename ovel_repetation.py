#count the most repeated vowel letter
s=input()
v="aeiou"
mx=-999
ans=0
d={}
for i in s:
    if i in v:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
        if d[i]>mx:
            mx=d[i]
            ans=i
print(ans)
