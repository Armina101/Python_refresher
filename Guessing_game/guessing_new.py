import random
import time

print("Welcome to the Guessing Game!")
time.sleep(1)
playing = input("Would you like to play this game? ")
if playing.lower() != "yes":
    quit()
number = random.randrange(2, 10)
print(number)