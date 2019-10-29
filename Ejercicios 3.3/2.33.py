#
try:
    a=int(input("numero: "))
    if not a%400 or (not a%4 and a%100):
        print("si")
    else:
        print("no")
except:
    print("no es un numero")