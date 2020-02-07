palabra = list(input("Introduce una palabra:\t"))
vocales = consonantes = mayusculas = ''
for i in palabra:
    if i == 'a' or i == 'A' or i == 'e'  or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U': 
        vocales+=i
        mayusculas+=i.upper()
    else:
        consonantes+=i
        mayusculas+=i
print(vocales,consonantes,mayusculas)