import random
print("adivine el número del 1 al 20.")
adv = random.randint(1,20)
num = -1
while num != adv:
    num = int(input("--> "))
    if adv < num:
        print("el número a adivinar es menor.")
    elif adv > num:
        print("el número a adivinar es mayor.")
    elif adv == num:
        print("adivinó :)")
