#Operadores de comparación
#== object.__eq__(self, other)
#!= object.__ne__(self, other)

import math
class Fraccion:
    def __init__(self, numerador, denominador=1):
        self.numerador = numerador
        self.denominador = denominador
    def __str__(self):
        return (f"{self.numerador}/{self.denominador}")
    def __add__(self, otro):
        if type(otro) == type(0):
            otro = Fraccion(otro)
        return Fraccion(self.numerador*otro.denominador + self.denominador*otro.numerador,self.denominador*otro.denominador)
    def __sub__(self, otro):
        if type(otro) == type(0):
            otro= Fraccion(otro)
        return Fraccion(self.numerador*otro.denominador - self.denominador*otro.numerador,self.denominador*otro.denominador)
    def __mul__(self, otro):
        if type(otro) == type(0):
            otro = Fraccion(otro)
        return Fraccion(self.numerador*otro.numerador, self.denominador*otro.denominador)
    def __floordiv__(self,otro):
        if type(otro) == type(0):
            otro = Fraccion(otro)
        return Fraccion(self.numerador*otro.denominador,self.denominador*otro.numerador)
    def __truediv__(self,otro):
        if type(otro) == type(0):
            otro = Fraccion(otro)
        return Fraccion(self.numerador*otro.denominador,self.denominador*otro.numerador)
    def __mod__(self,otro):
        if type(otro) == type(0):
            otro=Fraccion(otro)
        return((self.numerador/self.denominador)%(otro.numerador/otro.denominador)) 
    def __pow__(self,otro):
        if type(otro) == type(0):
            otro=Fraccion(otro)
        if otro.numerador == 0:
            return 1
        elif otro.numerador > 0:
            return Fraccion(self.numerador**(otro.numerador/otro.denominador),self.denominador**(otro.numerador/otro.denominador))
        elif otro.numerador < 0:
            return Fraccion(self.denominador**(otro.numerador/otro.denominador),self.numerador**(otro.numerador/otro.denominador))
    __radd__=__add__
    __rsub__=__sub__
    __rmul__ = __mul__
    __rfloordiv__=__floordiv__
    __rtruediv__=__truediv__
    __rmod__=__mod__
    __rpow__=__pow__

    __iadd__=__add__
    __isub__=__sub__
    __imul__=__mul__
    __ifloordiv__=__floordiv__
    __itruediv__=__truediv__
    __imod__=__mod__
    __ipow__=__pow__
    def __lt__(self,otro):
        a=self.numerador/self.denominador
        b=otro.numerador/otro.denominador
        if a < b:
            return True
        else:
            return False
    def __gt__(self,otro):
        a=self.numerador/self.denominador
        b=otro.numerador/otro.denominador
        if a > b:
            return True
        else:
            return False
    def __le__(self,otro):
        a=self.numerador/self.denominador
        b=otro.numerador/otro.denominador
        if a <= b:
            return True
        else:
            return False
    def __ge__(self,otro):
        a=self.numerador/self.denominador
        b=otro.numerador/otro.denominador
        if a >= b:
            return True
        else:
            return False
    def __eq__(self,otro):
        a=self.numerador/self.denominador
        b=otro.numerador/otro.denominador
        if a == b:
            return True
        else:
            return False
    def __neg__(self,otro):
        a=self.numerador/self.denominador
        b=otro.numerador/otro.denominador
        if a != b:
            return True
        else:
            return False
if __name__ == "__main__":
    x=Fraccion(3,4)
    y=Fraccion(1,3)
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x//y)
    print(x%y)
    print(x**y)
    x+=y
    print(x)
    x=Fraccion(3,4)
    x-=y
    print(x)
    x=Fraccion(3,4)
    x*=y
    print(x)
    x=Fraccion(3,4)
    x/=y
    print(x)
    x=Fraccion(3,4)
    x//=y
    print(x)
    x=Fraccion(3,4)
    x%=y
    print(x)
    x=Fraccion(3,4)
    x**=y
    print(x)
    print(x>y)
    print(x>=y)
    print(x<y)
    print(x<=y)
    print(x==y)
    print(x!=y)