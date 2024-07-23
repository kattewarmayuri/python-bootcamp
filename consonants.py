#consonents finding
'''check=['a','e','i','o','u']
count=0
count_c=0
inp="helloworld"
for i in inp:
    if(i in check):
       count+=1
    else:
        count_c+=1
print(count)
print(count_c)'''


#print all the  vowels followed ny consonants
str=input()
inp=str.lower()
vowel="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
for i in inp:
    if(i in vowel):
        print(i,end="")
for i in inp:
    if(i in consonants):
        print(i,end="")


