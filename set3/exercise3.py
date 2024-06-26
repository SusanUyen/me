"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

from click import prompt
from matplotlib.rcsetup import validate_int


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    """Play a guessing game with adjustable bounds and robust input validation."""
    print("\nWelcome to the advanced guessing game!")
    
    # Get valid lower bound
    while True:
        try:
            lower_bound = int(input("Enter a lower bound: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Get valid upper bound
    while True:
        try:
            upper_bound = int(input(f"Enter an upper bound greater than {lower_bound}: "))
            if upper_bound > lower_bound:
                break
            else:
                print(f"The upper bound must be greater than {lower_bound}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    print(f"OK then, a number between {lower_bound} and {upper_bound}.")

    # Generate a random number within the given range
    actual_number = random.randint(lower_bound, upper_bound)
    guessed = False

    # Start the guessing loop
    while not guessed:
        try:
            guessed_number = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            if guessed_number < lower_bound or guessed_number > upper_bound:
                print(f"Your guess is out of bounds! It should be between {lower_bound} and {upper_bound}.")
            else:
                print(f"You guessed {guessed_number},")
                if guessed_number == actual_number:
                    print(f"You got it!! It was {actual_number}")
                    guessed = True
                elif guessed_number < actual_number:
                    print("Too small, try again :'(")
                else:
                    print("Too big, try again :'(")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return "You got it!"

if __name__ == "__main__":
    print(advancedGuessingGame())
