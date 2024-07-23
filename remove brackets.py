#removeall the brckts from the given alg exp
'''inp=input()
for i in inp:
    if(ord(i)==41 or ord(i)==40 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="")'''

#ip=ABC skip value=4 
#OP=EFG 
'''inp=input()
for i in inp:
    print(chr(ord(i)+4),end="")'''

#IP=hello------wor---ld
#op=---------helloworld

inp="hello----wor--ld"
newstr=inp.replace('-','')
str=inp.count('-')
result='-'*str+newstr

print(result)        