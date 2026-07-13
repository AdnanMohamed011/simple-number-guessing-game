import random

random_num = random.randint(1 , 9)

attempts = 0
score = 0
while attempts < 3:
    attempts += 1

    user_num = int(input("Choose a number between 1 & 9: "))
    if user_num == random_num:
        score += 10
        print(f"You guessed the number! You got '{score}' points!")
        choice = input("Would you like to keep playing? (Y/N) ").capitalize()

        if choice == "Y":
            attempts = 0
            random_num = random.randint(1 , 9)
            user_num = int(input("Choose a number between 1 & 9: "))

        else:
            break

    if user_num in range(random_num - 2, random_num + 2):
        print("Hot! You are so close!")
    else:
        print("Cold, not close.")
    
    if attempts == 3 and user_num != random_num:
        print(f"You are out of attempts. Game over. You got '{score}' Points")