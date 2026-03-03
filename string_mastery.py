"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ x ] 1. Header Docstring included with your name.
[ x ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ x ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ x ] 4. Task 3: Validation (isdigit check) completed.
[ x ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: Jack
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR 🎸 ---
instrument = "Acoustic Guitar"

print(len(instrument))                    # prints length
print(instrument[0])                      # first letter
print(instrument[-1])                     # last letter
print(min(instrument))                    # lowest ASCII
print(max(instrument))                    # highest ASCII


# --- TASK 2: THE CLEANUP CREW 🧵 ---
messy_input = "   vOLUME_knob_11   "

messy_input = messy_input.strip()         # remove spaces
messy_input = messy_input.upper()         # make uppercase
messy_input = messy_input.replace("_", " ")   # change _ to space

print(messy_input)                        # show the cleaned result


# --- TASK 3: THE VALIDATOR 🔍 ---
serial_number = "90210"

if serial_number.isdigit():
    print("Valid Serial")
else:
    print("Invalid Serial")


# --- TASK 4: THE DUCK BRIDGE 🦆🎵 ---
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("\n--- Singing the Duck Song! ---")

for char in name_string:
    current_name = " ".join(duck_letters)
    
    print("There was a teacher who had a duck and Ducky was his Name-o")
    print(f"({current_name}) \n" * 3)
    print("and Ducky was his Name-o!\n")
    
    duck_letters[count] = "🦆"
    count = count + 1

# Finale
final_name = " ".join(duck_letters)
print(f"({final_name}) \n" * 3)
print("and Ducky was his Name-o!")