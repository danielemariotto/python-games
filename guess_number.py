# ITA
# Costruire un gioco di indovinelli numerici, in cui l'utente seleziona un intervallo.
# Supponiamo che l'utente abbia selezionato un intervallo, ad esempio da A a B, dove A e B appartengono agli interi.
# Il sistema selezionerà un numero intero casuale e l'utente dovrà indovinare quel numero intero nel minor numero di tentativi.

# ENG
# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses


import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("Please select a range for the game.")
    while True:
        try:
            A = int(input("Enter the lower limit of the range: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        break
    while True:
        try:
            B = int(input("Enter the upper limit of the range: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        break
    number = random.randint(A, B)
    guess = None
    count = 0
    while guess != number:
        while True:
            try:
                guess = int(input(f"Guess the number between {A} and {B}: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
            break
        count += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    print(f"Congratulations! You guessed the number in {count} attempts.")


guess_number()