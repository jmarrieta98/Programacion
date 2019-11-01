def digitos(x):
    return len(list(str(bin(x))))-2

if __name__=="__main__":
    print("Necesitas",digitos(int(input("Introduce un numero: "))),"digitos para convertir en binario")