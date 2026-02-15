"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

#1

#beginning of code block
no = True #boolean

#start of loop sequence
while no:
    print("\nAre we there yet?")
    
    answer = input("\n(yes/no): ")
    if answer == "yes":
        print("\nFINALLY!\n\nNow the party starts!\n")
        no = False #boolean

#end "while" of loop

#2

#beginning of code block
for i in range(99, 0, -1):
    print(f"{i} Bottles of Orc grog on the wall!\n")

#end of "for" loop

