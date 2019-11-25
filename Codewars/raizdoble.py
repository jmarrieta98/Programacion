def raiz (x):
    r=x
    t=0
    while (t != r):
        t=r
        r = 0.5 * ( (x/r)+r)
    return r
def cuadrado(x):
    return x**2

if __name__ == '__main__':
    print(raiz(int(input("Introduce un numero:\t"))))
