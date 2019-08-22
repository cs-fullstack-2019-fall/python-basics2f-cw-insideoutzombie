import random

### Problem 1:
# Write some Python code that has three variables called ```greeting```, ```my_name```, and ```my_age```.
# Intialize each of the 3 variables with an appropriate value,
# then rint out the example below using the 3 variables and two different approaches for formatting Strings.
#
# 1) Using concatenation and the ```+``` and 2) Using an ```f-string```. Sample output:
#
# ```
# YOUR_GREETING_VARIABLE YOUR_NAME_VARIABLE!!! I hear that you are YOUR_MY_AGE_VARIABLE today!
# ```

greeting = 'Hello'
my_name = 'david'
my_age = 26

# welcome_text = 'Hello '+fname+ ' ' + lname + ' from ' + city + '!!!'
welcome_text = f'{greeting} I hear that you are {my_age} today '



print(welcome_text)

### Problem 2:
# Write some Python code that asks the user for a secret password.
# Create a loop that quits with the user's quit word.
#  If the user doesn't enter that word, ask them to guess again.
# randomWord = input("Enter a secret word ")
# userGuess = ''
# while (userGuess != randomWord):
#     userGuess = input("Enter the password ")
#     if(userGuess == randomWord):
#         print("success")
#     else:
#         userGuess = input("Sorry incorrect! Try again ")

### Problem 3:
# Write some Python code using ```f-strings``` that prints 0 to 50 three times in a row (vertically).
# ```
# 1 1 1
# 2 2 2
# 3 3 3
# 4 4 4
# 5 5 5
# .
# .
# .
# ```
for idx in range(0, 51, 1):
    print(idx, idx, idx)

### Problem 4:
# Write some Python code that create a random number and stores it in a variable.
# Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
randomNumber = random.randint(1, 10)
userGuess = ''
while (userGuess != randomNumber):
    userGuess = int(input("Enter a number "))
    if(userGuess == randomNumber):
        print("success")
    else:
        userGuess = int(input("sorry incorrect "))
