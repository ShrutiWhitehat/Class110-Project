import random

response="y"
while response=="y":
    number=random.randint(1,6)

    if (number==1):
        print("O")

    if (number==2):
        print("OO")

    if (number==3):
        print("OOO")   

    if (number==4):
        print("OO")
        print("OO")

    if (number==5):
        print("OO")
        print("O")
        print("OO")

    if (number==6):
        print("OOO")
        print("OOO")
    response=input("Press y To Roll A Dice And n To Exit")

    print("\n")
