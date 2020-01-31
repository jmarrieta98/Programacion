aux0=1
aux1=2
i=1
num=0
while num < 1000:
    num= (3*aux1) + (2*aux0)
    aux0=aux1
    aux1=num
    i+=1

print("El primer numero mayor de 1000 es",num,"y pertenece a ",i)
