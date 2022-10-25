from multiple_function import with_friend as MP
from pc_functions import with_pc as PC

print("---!Guess The Number!---")
while True:
    print("\nPress 1 for play with PC.")
    print("\nPress 2 for play with your friend.")

    choose = str(input("MAKE YOUR CHOOSE: "))
    if choose == "q":
        break
    while True:
        if choose == "1":
            PC()
            break
        elif choose == "2":
            MP()
            break
        else:
            choose = str(input("MAKE YOUR CHOSE AGAIN: "))