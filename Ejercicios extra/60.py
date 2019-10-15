edad1 = int(input("Introduce la edad de la primera persona: "))
edad2 = int(input("Introduce la edad de la segunda persona: "))
if edad1 == edad2:
    print("Las dos personas tienen la misma edad")
elif edad1 > edad2:
    print("La primera persona es mayor")
else:
    print("La segunda persona es mayor")