"""
## ASSIGNMENT REQUIREMENTS
## [ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
"""
#jack_smith

# variables
hobbit = "Frodo"
hobbit2 = "Sam"
hobbit3 = "Gollum"

print(f"{hobbit3} has suggested a quicker path to Mount Doom.")
print(f"{hobbit2} is unsure of {hobbit3}'s intentions.")
print(f"{hobbit} cannot think straight due to the One Ring's influence.")

# inputs from user(s)
print(f"Help get these hobbits past the Orcs to Mount Doom... or not...")
num1 = int(input("First number (any number): "))
num2 = int(input("Second number (any number): "))

# The 6 Logic Checks (separate if/else statements)

# 1. Are both numbers greater than 0?
if num1 > 0 and num2 > 0:
    print(f"\n{hobbit}: Yes, both numbers are greater than 0! The journey continues.")
else:
    print(f"\n{hobbit}: No, not both greater than 0. The path is blocked.")

# 2. Are both numbers greater than 100?
if num1 > 100 and num2 > 100:
    print(f"\n{hobbit2}: Yes, both greater than 100! Mighty as the mountains.")
else:
    print(f"\n{hobbit2}: No, not both greater than 100.")

# 3. Is at least one of them even?
if (num1 // 2) * 2 == num1 or (num2 // 2) * 2 == num2:
    print(f"\n{hobbit3}: Yes, at least one is even, my precious!")
else:
    print(f"\n{hobbit3}: No, neither is even. Tricksy odds.")

# 4. Is either number less than 100?
if num1 < 100 or num2 < 100:
    print(f"\n{hobbit}: Yes, at least one is less than 100, small like hobbits.")
else:
    print(f"\n{hobbit}: No, neither is less than 100.")

# 5. Are they not equal to each other?
if not (num1 == num2):
    print(f"\n{hobbit2}: Yes, they are not equal, different as day and night.")
else:
    print(f"\n{hobbit2}: No, they are equal.")

# 6. Is it true that neither of them is zero?
if not (num1 == 0) and not (num2 == 0):
    print(f"\n{hobbit3}: Yes, neither is zero, good, no emptiness in the void.")
else:
    print(f"\n{hobbit3}: No, at least one is zero, bad for the precious.")

# The Categorizer: Use an if/elif/else chain to check only num1 (Positive, Negative, or Zero)
if num1 > 0:
    print(f"\n{hobbit}: {num1} is Positive, full of hope like the Shire.")
elif num1 < 0:
    print(f"\n{hobbit2}: {num1} is Negative, dark like Mordor.")
else:
    print(f"\n{hobbit3}: {num1} is Zero, balanced like the ring's temptation.")