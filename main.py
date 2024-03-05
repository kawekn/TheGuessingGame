from random import randint


secret_number = randint(1, 100)
success = False

while not success:

    user_guess = input("Guess the number: ")

    try:
        user_guess = int(user_guess)
    except ValueError:
        print("It's not a number!")
        continue

    if user_guess == secret_number:
        print("You win")
        success = True
    elif user_guess > secret_number:
        print("To big!")
    else:
        print("To small!")
