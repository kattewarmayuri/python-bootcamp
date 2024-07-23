#how many vowels are in gvn str

'''s="mayuri"
print(most_frequent_vowel(s))'''
'''s=input()
d={
    'a':0,"e":0,"i":0,"0":0,"u":0,
}
for i in s:
    if i in "aeiou":
        d[i]+=1
ans,maxvalue='',0
for key,value in list(d.items()):
    print(key,"-----",value)
    if value>maxvalue:
       ans=key
       maxvalue=value
print(ans) '''
#or
#print how many vowels are in a string

'''inp = input('Enter the string :')
count = 0
inp= inp.lower()
for i in inp:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count+=1
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))'''
          
           #or
  
'''check=['a','e','i','o','u']
count=0
inp="helloworld"
for i in inp:
    if(i in check):
       count+=1
print(count)'''