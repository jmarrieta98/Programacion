def ordena_saltadores(saltadores):
    lista = []
    for saltador, saltos in saltadores.items():
        media = 0.0
        if len(saltos)>0:
            media = sum(saltos)/len(saltos)
        lista.append((saltador,media))
    lista.sort(reverse=True, key=lambda r: r[1])
    return lista


saltadores = { "Louganis": [], "Xiao": [], "Perez": [], "Gordon": [], "Chan": []}

while True:
    opcion = input("¿Que desea hacer?: ")
    if opcion.lower() == "salir":
        break
    if opcion.lower() == "clasificacion":
        orden = 1
        for saltador, media in ordena_saltadores(saltadores):
            print(f"{orden}.- {saltador} {media:.2f}")
            orden+=1
        continue
    if opcion.lower() == "saltos":
        for saltador, saltos in saltadores.items():
            print(saltador, end=" ")
            for salto in saltos:
                print(f"{salto:.2f}", end=" ")
            print()
        continue

    lopciones = opcion.split()
    if lopciones[0] not in saltadores or len(lopciones)!=6:
        print("Introducción no válida")
        continue
    try:
        valoraciones = [ int(v) for v in lopciones[1:]]
    except ValueError:
        print("Introducción no válida")
        continue
    
    valoraciones.sort()
    del valoraciones[0]
    del valoraciones[-1]

    puntuacion = sum(valoraciones)/len(valoraciones)

    saltadores[lopciones[0]].append(puntuacion)