import random

random_num = random.randint(1 , 9)

attempts = 0
while attempts < 3:
    attempts += 1
    user_num = int(input("Choose a number between 1 & 9: "))
    if user_num == random_num:
        print("You guessed the number!")
        break

    if user_num in range(random_num - 2, random_num + 2):
        print("Hot! You are so close!")
    else:
        print("Cold, not close.")