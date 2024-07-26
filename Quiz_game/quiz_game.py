print("Welcome to Amina's Quiz!")

playing = input("Would you like to play my Quiz? ")
if playing.lower() != "yes":
    quit()
print("Okay, Let's play!")
score = 0

answer = input("What is Amina's favourite colour? ")
if answer.lower() == "brown":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("Who is Amina's crush? ")
if answer.lower() == "abubakar nur khalil":
    print("Correct!")
    score += 1
else:
    print("No, She has a crush on Abubakar Nur Khalil")

answer = input("Is Amina a Doctor? ")
if answer.lower() == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect, Amina is a Software Engineer")

print("Your final score is " + str(score) + " out of 3")
print("You got " + str((score / 3) * 100) + "%")