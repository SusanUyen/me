"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think it will declare the variables called some_words
# And I'll put a list of strings into it
some_words = ["what", "does", "this", "line", "do", "?"]
# I think this will print every single variable at a time 
# word = ['what', 'does', 'this', 'line', 'do', '?']
for word in some_words:
    print(word)
# I think this will also print every single variable at a time
# x = ['what', 'does', 'this', 'line', 'do', '?']
for x in some_words:
    print(x)
# I think this will print variable called some_words
print(some_words)
# I think this will test the condition of the variable called len
# And if it is true, this will print "some_words contains more than 3 words"
if len(some_words) > 3:
    print("some_words contains more than 3 words")
# I think it will print a named tuple of the current laptop/computer 
# containing six attributes: system, node, release, version, machine, and processor.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
