print("Welcome to the Biochemistry Quiz!")

player_answer = input("Would You like to play this Game? ")

if player_answer.lower() != "yes":
    quit()
else:
    print("Okay, let's play!")
    score = 0

answer = input("Biochemistry is under which Faculty? ")
if answer.lower() == "life sciences":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is an effective lifestyle that helps people predisposed to Diabetes? ")
if answer.lower() == "intermittent fasting":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What hormone is produced by the adrenal gland? ")
if answer.lower() == "adrenaline":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What carries Blood from the Heart to the Brain? ")
if answer.lower() == "carotid artery":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Deficiency of Vitamin C causes what? ")
if answer.lower() == "scurvy":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You scored " + str(score) + " out of 5")
print("You have " + str((score / 5) * 100) + "%")