def validBraces(string):
    corchetes=0
    parentesis=0
    llaves=0
    for i in range(len(string)):
        if (string[i]==')' and parentesis<1) or (string[i]==']' and corchetes<1) or (string[i]=='}' and llaves<1):
            return False
        elif (string[i]==')' and parentesis>0) or (string[i]==']' and corchetes>0) or (string[i]=='}' and llaves>0):
            if string[i] == ')':
                parentesis-=1
            elif string[i] == ']':
                corchetes-=1
            else:
                llaves-=1
        elif string[i]=='(' or string[i] =='[' or string[i] == '{':
            if string[i] == '(':
                parentesis+=1
            elif string[i] == '[':
                corchetes+=1
            else:
                llaves+=1
    if corchetes == 0 and parentesis == 0 and llaves == 0:
        return True
    else:
        return False

print(validBraces('[]{()}[]'))