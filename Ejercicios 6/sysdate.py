import os

fecha=os.popen('date /t').read()[:-1]
print(fecha)