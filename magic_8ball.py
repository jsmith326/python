"""
ASSIGNMENT 7B: THE MAGIC 8 BALL
[ x ] 1. Header Docstring included.
[ x ] 2. RESPONSES is a tuple containing at least 8 string options.
[ x ] 3. Program uses a 'while True' loop to keep the game running.
[ x ] 4. random.choice() selects the answer from the tuple.
[ x ] 5. Logic checks if "quit" is in the user input to break the loop.
"""

# Jack Smith

import random

# My 8 ball answers (I put 10 like the lesson said at least 8)
RESPONSES = (
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "It is certain",
    "Without a doubt",
    "Very doubtful",
    "Cannot predict now",
    "Signs point to yes",
    "Don't count on it"
)

print("Welcome to the Digital Oracle!")

while True:
    user_input = input("\nWhat is your question? (type quit to stop): ")
    
    # Clean it up like the sanitization lesson
    cleaned = user_input.strip().lower()
    
    # Stop if they type quit (works for QUIT too)
    if "quit" in cleaned:
        print("Goodbye!")
        break
    
    # Pick random answer
    answer = random.choice(RESPONSES)
    print(answer)