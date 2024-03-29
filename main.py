from random import randint


def guessing_game():
    """Generates a random number and checks user's guess.

    Raises:
        ValueError: When user input isn't integer literal.
    """
    secret_number = randint(1, 100)
    while True:

        user_guess = input("Guess the number: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("It's not a number!")
            continue

        if user_guess == secret_number:
            print("You win")
            break
        elif user_guess > secret_number:
            print("To big!")
        else:
            print("To small!")


guessing_game()
