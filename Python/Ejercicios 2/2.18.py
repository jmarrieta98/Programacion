n = int(input("Introduce un numero mayor que 2: "))
for i in range(2,n):
    if n%i == 0:
        print(i,"*",n//i,end=', ')