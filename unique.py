# prnt the unique chart in str(non repting)str=input()

ans=""
vowel="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
i="heloworld"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)