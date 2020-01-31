sum1,sum2=1,1
n1=int(input("ingrese primer numero: "))
n2=int(input("ingrese segundo numero: "))
for i in range(2,n1):
    if n1%i==0:
        sum1+=i
for j in range(2,n2):
    if n2%i == 0:
        sum2+=i
if sum1==n2 and sum2==n1:
       print("los numeros ",n1," y ",n2," Si son numeros amigos")
else:
       print("los numeros ",n1," y ",n2," No son numeros amigos")