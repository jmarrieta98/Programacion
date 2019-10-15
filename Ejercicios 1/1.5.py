importe = float(input("Introduzca el importe del producto sin IVA: ")) 
IVA = int(input("Introduzca el IVA: "))
print("El precio del producto es: ",importe+importe*(IVA/100))