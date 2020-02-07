#dibuja un arbol de navidad y según el número que introduzcas será mas grande o mas chico 
# y si no es un numero dibuja un arbol de 3
try:
    n=int(input("numero "))
except:
    n=3
a=1
for i in range(n,0,-1):
    print(" "*i+"*"*a)
    a+=2
print(" "*(n-1)+"*"*3)