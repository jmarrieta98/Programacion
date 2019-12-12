import random 

def numero_aleatorio():
    numeros = "0123456789"
    resultado = ""
    for i in range(5):
        while True:
            digito = random.choice(numeros)
            if digito in resultado:
                continue
            resultado += digito
            break
    return resultado

def comprueba(numero, secreto):
    m = 0
    h = 0
    for i in range(len(numero)):
        if numero[i] == secreto[i]:
            m+=1
        elif numero[i] in secreto:
            h+=1
    return m,h

if __name__ == "__main__":
    s = numero_aleatorio()
    print(s)
    intentos = 1
    while True:
        n = input("Introduce un número de 5 cifras: ")
        if len(n)!=5 or not n.isdigit():
            print("Ese número no tiene cinco cifras")
            continue
        m,h = comprueba(n,s)
        if m == 5:
            print(f"Enhorabuena, lo has conseguido en {intentos} intentos.")
            break
        print(f"{m} muertos y {h} heridos")
        print(f"{intentos} intentos")
        intentos+=1