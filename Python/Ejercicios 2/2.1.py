horas = int(input("Horas de trabajo: "))
coste = float(input("Coste por hora: "))
if horas > 40:
    print("Importe total: ",40*coste+((horas-40)*coste*1.5))
else:
    print("Importe total: ",horas*coste)
