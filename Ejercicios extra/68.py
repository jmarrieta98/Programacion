dinero = int(input("Introduzca el dinero que tiene: "))
if dinero/500>1 :
    print(dinero // 500," billetes de 500€")
    dinero=dinero % 500
if dinero/200>1:
    print(dinero // 200," billetes de 200€")
    dinero=dinero % 200
if dinero/100>1:
    print("1 billete de 100€")
    dinero=dinero % 100
if dinero/50>1:
    print("1 billete de 50€")
    dinero=dinero % 50
if dinero/20>1:
    print(dinero // 20," billetes de 20€")
    dinero=dinero % 20
if dinero/10>1:
    print("1 billete de 10€")
    dinero=dinero % 10
if dinero/5>1:
    print("1 billete de 5€")
    dinero=dinero % 5
if dinero/2>1:
    print(dinero // 2," monedas de 2€")
    dinero=dinero % 2
if dinero/1>1:
    print("1 moneda de 1€")