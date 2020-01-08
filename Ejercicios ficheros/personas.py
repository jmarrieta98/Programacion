from io import open

fichero = open('personas.txt','r', encoding="utf8")
lineas = fichero.readlines()
fichero.close()

persona = {}
for linea in lineas:
    # Borramos los saltos de línea y separamos
    campos = linea.replace("\n", "").split(";")  
    persona[campos[0]]=[campos[1],campos[2],campos[3]]
for iden, per in persona.items():
    print(f"{iden} -> {per[0]} {per[1]} {per[2]}")