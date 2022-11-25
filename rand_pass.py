
import os
import random as r
sim = list("@#$_&/*qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890")
while True:
    try:
        xint = int(input("кол-во символов: "))
    except ValueError:
        print("число!")
        continue
    os.system("clear")
    for i in range(xint):
        print(r.choice(sim), end="")
    print()
    input()

