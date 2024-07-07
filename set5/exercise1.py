# -*- coding: UTF-8 -*-

import requests

"""REFACTORING

Refactoring is the process of making your code better. You are usually looking 
to make it more readable or easier to maintain. Usually you'll do this by 
pulling out bits of code that encapsualte one idea, especially if that idea is 
used in several places.

We've talked already about 
    ↱red→green→refactor↴
    ↜←←←←←←←←←←←←←←←←←←↩

Where red means make sure the test fails if you haven't done anything, green 
means make the test pass, however you can, now this is the reafactor part.

The function below works fine, but it's long and hard to read. Identify the 
parts that are repeated, and pull them out into their own functions. I've made 
that easier for you by making the function stubs for the bits you need to do.

Modify this function, don't write a whole new one.
"""


def fetch_word(url):
    """Fetches a word from the given URL and returns it."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()  # Return the word after stripping whitespace
    else:
        print(f"Failed to fetch word from {url}. Status code: {response.status_code}")
        return None

def wordy_pyramid():
    """Make a pyramid out of real words."""
    baseURL = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}"
    pyramid_list = []

    # Build pyramid upwards
    for length in range(3, 21, 2):
        url = baseURL.format(length=length)
        word = fetch_word(url)
        if word:
            pyramid_list.append(word)

    # Build pyramid downwards
    for length in range(20, 2, -2):
        url = baseURL.format(length=length)
        word = fetch_word(url)
        if word:
            pyramid_list.append(word)

    return pyramid_list

def get_a_word_of_length_n(length):
    """Fetches a word of specified length from an API endpoint and prints it."""
    if not isinstance(length, int) or length < 3:
        print("Invalid length. Length must be an integer greater than or equal to 3.")
        return None

    url = f"https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            word = response.text.strip()  # Return the word after stripping whitespace
            print(f"Requested length: {length}, Retrieved word: {word}")
            return word
        else:
            print(f"Failed to fetch word of length {length}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def list_of_words_with_lengths(list_of_lengths):
    """Returns a list of words fetched from the API for the specified list of lengths."""
    words = []
    for length in list_of_lengths:
        word = get_a_word_of_length_n(length)
        if word:
            words.append(word)
    return words

if __name__ == "__main__":
    pyramid = wordy_pyramid()
    for word in pyramid:
        print(word)
