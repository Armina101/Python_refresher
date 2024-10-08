import random

top_range = input("Type a number: ")
if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a valid number next time.")
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a valid number next time.")
        continue
    if user_guess == random_number:
        print("You guessed correctly!")
        break
    elif user_guess > random_number:
            print("You were above the number!")
    else:
            print("You guessed below the number")

print("You got it in", guesses, "guesses")