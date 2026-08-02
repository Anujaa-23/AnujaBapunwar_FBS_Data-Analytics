for i in range(1,6):
    for j in range(1,6-i):
        print('',end=' ')

    for j in range(1,i+1):
        print(j,end=' ')
        A=i+1

    for j in range (1,i):
        print(A,end=' ')
        A+=1
    print()
