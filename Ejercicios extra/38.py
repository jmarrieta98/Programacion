from math import sin,pi
lado1=float(input("Introduce el primer lado: "))
lado2=float(input("Introduce el segundo lado: "))
angulo=pi/180*float(input("Introduce el angulo entre los lados dados: "))
area=1/2*lado1*lado2*sin(angulo)
print("El area es ",round(area,2))
