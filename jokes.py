import pyjokes
from random import randint

# print(pyjokes.get_joke())

# length = len(pyjokes.get_jokes())

for joke in pyjokes.get_jokes(): # can call function (returns list) within for

    # randint(length)

    print(joke)
    response = input("Have another? (n to exit) ") # instructors want us to use \n at end

    if response == "n":
        exit()

    # no else needed because it'll just keep looping
