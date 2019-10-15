letra=input("Introduzca una letra: ")
if letra == "ñ" or letra>= "a" and letra <="z":
    print("La letra es MINUSCULAS")
elif letra == "Ñ" or letra>="A" and letra <="Z":
    print("La letra es MAYUSCULAS")
else:
    print("Error al introducir la letra")