#print  *
rows = 15
columns = 15
for i in range(rows):
    for j in range(columns):
        print('*', end='  ')
    print() 



for i in range(10):
    for j in range(10):
        if(i==j):
            print(' ', end=' ')
        else:
            print("*", end=' ')
    print() 
