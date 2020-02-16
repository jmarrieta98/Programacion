def division(a,b,x=0):
    if a >= b:
        return division(a-b,b,x+1)
    else:
        return x

if __name__ == "__main__":
    print(division(100,5))