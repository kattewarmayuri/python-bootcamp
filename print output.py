# rev the string
check="0123456789"
i="hello 1234world"
ans=0
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)
print(ans)