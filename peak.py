#peak element *****
'''n=list(map(int,input().split( )))
for i in range(len(n)):
    if(n[i-1]<n[i] and n[i]>n[i+1]):
        print({n[i]})'''
#peek element
'''n=list(map(int,input().split( )))
count=0
for i in range(1,len(n)-1):
    if n[i]>n[i-1] and n[i]>n[i+1]:
        count=i
if(n[-1]>n[-2] and n[-1]>count):
    count=len(n)-1
print(n[count])2'''


#find the no of prime numbers in given range

