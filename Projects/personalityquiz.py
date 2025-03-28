# Beginning: create variables
Football_points = 0
Basketball_points = 0
Baseball_points = 0 

# Middle: Ask questions
answer = input ("Would you rather A) Score the game winning touchdown, B) Make a buzzer beater for the win, or C) Hit a game winning home run?")
if answer == "A":
    Football_points += 1
elif answer == "B":
    Basketball_points += 1
elif answer == "C":
    Baseball_points += 1


answer = input ("Would you rather A) Play sports on a Field, B) Play sports on a Court, or C) Play sports on a baseball diamond?")
if answer == "A":
    Football_points += 1
elif answer == "B":
    Basketball_points += 1
elif answer == "C":
    Baseball_points += 1


answer = input ("Would you rather A) Catch a ball, B) Shoot a ball, or C) Hit a ball?")
if answer == "A":
    Football_points += 1
if answer == "B":
    Basketball_points += 1
if answer == "C":
    Baseball_points += 1


answer = input ("Would you rather A) Wear a Lot of gear, B) Wear a tiny bit of gear, or C) wear a medium amount of gear?")
if answer == "A":
    Football_points += 1
if answer == "B":
    Basketball_points += 1
if answer == "C":
    Baseball_points += 1


answer = input ("Which one do you like the most A) Madden, B) Nba2k, or C) MLB the show?")
if answer == "a":
    Football_points += 1 
if answer == "b":
    Basketball_points += 1
if answer == "c":
    Baseball_points += 1

# End: determine results
if Football_points > Basketball_points and Football_points > Baseball_points:
    print("you are a football person")
elif Basketball_points > Football_points and Basketball_points > Baseball_points:
    print("you are a basketball person")
elif Baseball_points > Football_points and Baseball_points > Basketball_points:
    print("you are a baseball person")