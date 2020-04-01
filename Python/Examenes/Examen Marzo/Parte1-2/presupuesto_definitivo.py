import agencia, datetime
e1 = agencia.Evento("Concierto de Sphinx",datetime.date.today(),agencia.Ciudad("Sevilla",200,60.35),1,34)
e2 = agencia.Evento("La vida de Brian",datetime.date.today(),agencia.Ciudad("Cádiz",0,52.12),1,7)
listaEventos = []
listaEventos.append(e1)
listaEventos.append(e2)

if __name__ == "__main__":
    while True:
        for evento in listaEventos:
            print(f"{evento.denominacion}")
        opcion=input("Introduce el evento o fin para terminar: \t")
        for evento in listaEventos:
            if evento.denominacion.lower() == opcion.lower():
                try:
                    personas = int(input("Introduce el numero de personas:\t"))
                except:
                    print("Error al introcudir el numero de personas")
                else:
                    print(f"Precio total {personas*evento.precio_persona()}€")
                    break
        else: 
            if opcion.lower()== 'fin':
                break
            else:print("Error, no has escrito bien el evento")