import random

secret_number = random.randint(1,100)
attempts = 0

while True:
    guess_num = int(input("Enter your guessing number: "))
    attempts += attempts
    
    if guess_num == secret_number:
        print(f"You Won! Total attempts: {attempts}")
        break
    elif guess_num > secret_number:
        print("Too High!")
    elif guess_num < secret_number:
        print("Too Low!")
    else:
        print("Invalid input please Enter number between 1 - 100 or q/Q to quit.")