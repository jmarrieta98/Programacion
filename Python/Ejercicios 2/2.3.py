control=0
while control != 1:
    try:
        nota = float(input("Introduzca puntuación: "))
    except ValueError:
        print("Error al introducir la información")
    else:
        if nota >= 0.0 and nota <= 1.0:
            control=1
            if nota < 0.6:
                print("Insuficiente")
            elif nota<0.7:
                print("Suficiente")
            elif nota<0.8:
                print("Bien")
            elif nota<0.9:
                print("Notable")
            else:
                print("Sobresaliente")
        else:
            print("Error al introducir la información")