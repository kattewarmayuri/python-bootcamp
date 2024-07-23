
#prime or not
'''n=4 
for i in range(2,n):
    if(n%i==0):
        print("not a prime")
        break
    else:
        print("prime")'''
#prime numbers b/w two number
a=int(input())
b=int(input())
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
