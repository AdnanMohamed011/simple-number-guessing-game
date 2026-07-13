import random

random_num = random.randint(1 , 9)

attempts = 0
while attempts < 3:
    user_num = int(input("Choose a number between 1 & 9: "))
    if user_num == random_num:
        print("You guessed the number!")
        break
    