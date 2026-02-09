"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

#Jack_Smith

#variables

hobbit = "Frodo"
hobbit2 = "Sam"
hobbit3 = "Gollum"

#constants

ACTION_RUN = 1
ACTION_STAY = 2
ACTION_FIGHT = 3
ACTION_SNEAK_UP = 4
ACTION_MANIPULATE = 5
ACTION_SUBMIT_TO_THE_RING = 6

print(f"{hobbit3} has suggested a quicker path to Mount Doom.")
print(f"{hobbit2} is unsure of {hobbit3}'s intentions.")
print(f"{hobbit} cannot think straight due to the One Rings influence.")

# inputs from user(s)

print(f"Help get these hobbits past the Orcs to Mount Doom... or not...")
choice_1 = int(input("First action (Pick 1-6): "))
choice_2 = int(input("Second action (Pick 1-6): "))

# The Gate

# 1. Using OR

if choice_1 == ACTION_RUN or choice_1 == ACTION_STAY:
    print(f"\n{hobbit3} is scared of the Orcs and runs... He wants to come back later for the ring...")
    print(f"\n{hobbit2} yells: 'I told you he was not for us Mr. Frodo!'")

# 2. Using AND

elif choice_1 == ACTION_FIGHT and choice_2 == ACTION_SNEAK_UP:
    print(f"\n{hobbit} decides to attack the orcs... but without their knowledge of his presence...")
    print(f"\n{hobbit3} says: 'Master Baggins is a sneaky one! These Orcs is stupid swine!'")

# 3. Using ELIF

elif choice_1 == ACTION_MANIPULATE:
    print(f"\n{hobbit} decides it is best if he acts and sounds like an Orc to convince them to let him and his 'prisoners' ({hobbit2} and {hobbit3}) pass")
elif choice_1 == ACTION_SUBMIT_TO_THE_RING:
    print(f"\n{hobbit} has felt a draw to the power of the One Ring...")
    print(f"\nBefore either {hobbit2} or {hobbit3} can realize... {hobbit} is gone like a wraith...")
    print(f"\nThe sounds of orcs approaching and stomping for fresh meat grows louder with each second... Mount Doom, in the distance, has become calm...")

# 4. Using NOT

elif not (choice_1 >= 1 and choice_1 <= 6):
    print(f"\n{hobbit}, {hobbit2}, and {hobbit3} cannot come to an agreeable decision... they all part to their own ways... {hobbit3}, though, will not let {hobbit} get far alone with the One Ring...")
else:
    print(f"\nThe Ring Wraiths are above {hobbit}, {hobbit2}, and {hobbit3}. A decision for our poor hobbits was not made wisely...")