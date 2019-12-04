import string
print(string.ascii_letters)

contactos= {
}
def nuevocontacto(usuario,telefono):
    contactos[usuario]=telefono
    return "Contacto {} añadido".format(usuario)

if __name__ == "__main__":
    while True:
        entrada=input("Introduce el telefono o usuario:\t")
        if entrada in contactos.keys():
            print (contactos[entrada])
        elif entrada in contactos.values():
            for telefono in contactos.items():
                if telefono[1] == entrada:
                    print (telefono[0])
        elif entrada[0] in string.ascii_letters:
            print(nuevocontacto(entrada,input("Introduce el numero de telefono:\t ")))
        elif '+' in entrada[0] and len(entrada) == 15:
            print(nuevocontacto(input("Introduce el usuario:\t"),str(entrada[0:])))
        elif entrada == 'salir':
            break

