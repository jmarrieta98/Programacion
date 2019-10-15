altura = 1
alturas=[]
while altura != 0:
    altura = float(input("Introduce la altura: "))
    alturas.append(altura)
alturas.remove(0)
mas17 = mas16 = mas15 = menos15 = 0
for i in alturas:
    if i> 1.70:
        mas17+=1
    elif i>1.60:
        mas16+=1
    elif i>1.50:
        mas15+=1
    else:
        menos15+=1
print("Alumnos más altos de 1,70m ",mas17,'\nAlumnos entre 1,60m y 1,70m inclusive ',mas16,"\nAlumnos entre 1,50m y 1,60m inclusive ",mas15,"\nAlumnos más bajos de 1,50m, incluyendo 1,50m ",menos15)
