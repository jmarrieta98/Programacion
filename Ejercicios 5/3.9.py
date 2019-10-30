def digitos(x):
    x=len(list(str(bin(x))))-2
    return x

if __name__=="__main__":
    print("Necesitas",digitos(int(input("Introduce un numero: "))),"digitos para convertir en binario")