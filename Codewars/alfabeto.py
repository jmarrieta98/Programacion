#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
#"a" = 1, "b" = 2, etc.
def alphabet_position(text):
    text = text.lower()
    lista = []
    for i in range(len(text)):
        if text[i]>='a' and text[i] <='z':
            lista.append(str(ord(text[i])-96))

    return ' '.join(lista)
    