numero = int(input("introduce un numero: "))
for i in range(1,numero+1):
    if i%2 == 0:
        print(i*-1,end=' ')
    else:
        print(i,end=' ')