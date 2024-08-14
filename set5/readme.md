TODO: Reflect on what you learned this week and what is still unclear.
Some notice I have learned from exercise 1 :

1. Encapsulation of Logic: The function fetch_word is already refactored to encapsulate the logic of making a request and handling the response. However, similar refactoring could be done within wordy_pyramid to further improve readability.
2. Error Handling:
   Consistent Error Handling: The fetch_word function checks for a successful HTTP response with status_code == 200. This ensures that only valid responses are processed, and errors are reported with informative messages.
   Graceful Fallbacks: If a word cannot be fetched (e.g., due to a bad request), the functions handle it by returning None and not appending anything to the list. This prevents the program from crashing and allows it to handle failures gracefully.
