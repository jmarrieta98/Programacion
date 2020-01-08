diccionario = {
    1:['h','o','l','a'],
    2:['c','a','s','a'],
    3:['l','o','s','a'],
    4:['p','e','p','e']
}

def escribir(diccionario,archivo)
    claves = list(diccionario.keys())
    archivo=open('archivo','w')
    archivo.writelines(str(x)+' ' for x in claves)
    archivo.write('\n')
    listdic=list(diccionario.values())
    for i in range(len(listdic)):
        for j in range(len(listdic[i])):
            archivo.write(listdic[j][i]+' ')
        archivo.write('\n')

if __name__ == "__main__":
    escribir(diccionario,'archivo.csv')