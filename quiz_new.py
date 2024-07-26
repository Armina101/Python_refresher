import time

print("Welcome to the Day Quiz!")
time.sleep(2)
playing = input("Would you like to Play with Me? ")
if playing.lower() == "yes":
    print("Lets Play!") 
    time.sleep(2)    
elif playing.lower() == "no":
    print("Okay, Bye!")
    quit()    
else:
    print("Please enter a valid input next time (Either yes or no)")
    quit()   

print("You earn 1 point everytime you answer the question correctly!")
time.sleep(1)
score = 0

first_answer = input("What is the Capital of Nigeria? ")
if first_answer.lower() == "abuja": 
    print("That is the correct answer!")
    time.sleep(1)
    score += 1
else:
    print("No, that's incorrect!")    

second_answer = input("How many continents are in the World? ")
if second_answer == "6": 
    print("That is the correct answer!")
    score += 1
else:
    print("No, that's incorrect!") 

third_answer = input("What is the first letter of the Greek Alphabet? ")
if third_answer.lower() == "alpha": 
    print("That is the correct answer!")
    time.sleep(1)
    score += 1
else:
    print("No, that's incorrect!")

print("You scored " + str(score) + " out of 3")
time.sleep(1)
print("You have " + str((score / 3) * 100) + "%")                   