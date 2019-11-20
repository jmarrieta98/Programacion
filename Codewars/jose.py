import sys
try:
    if len(sys.argv) != 2:
        print("Error. IP argument is not correct.")
        exit()
    else:
        for octet in map(int, sys.argv[1].split(".")): #variable obligatoria por bucle for
            if octet in range(0, 256) and len(sys.argv[1].split(".")) == 4:
                isCorrect = True #variable
            else:
                isCorrect = False
                print("Error. IP {} is not correct.".format(sys.argv[1], end=""))
                break
    if isCorrect:
        print("IP {} is correct.".format(sys.argv[1], end=""))
except ValueError:
    print("Error. IP {} is not correct.".format(sys.argv[1], end=""))