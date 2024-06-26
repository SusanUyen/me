"""Set 3, Exercise 2.

An example of how a guessing game might be written.
Play it through a few times, but also stress test it. What if your lower bound 
is 🍟, or your guess is "pencil", or "seven"
This will give you some intuition about how to make exercise 3 more robust.
"""


import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    # Ask for a valid upper bound
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")
    upperBound = input("Enter an upper bound: ")
    print(f"OK then, a number between 0 and {upperBound} ?")
    upperBound = int(upperBound)
    # Generate a random number within the given range
    actualNumber = random.randint(0, upperBound)

    guessed = False
    # Start the guessing loop
    while not guessed:
        guessedNumber = int(input("Guess a number: "))
        print(f"You guessed {guessedNumber},")
        if guessedNumber == actualNumber:
            print(f"You got it!! It was {actualNumber}")
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()
