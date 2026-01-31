"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""

#variable for user's age

age = int(input("Please enter your age: "))

#determine price based on age from top to bottom

if age < 1:         #start
    print("\nYou eat for 0 dollars!")
 
elif age <= 11:     #path
    price = age * 1.00
    print(f"\nYour price is: ${price:.2f}")
    print("\nEnjoy your meal!")

elif age <= 64:     #path
    price = 16.95
    print(f"\nYour price is: ${price:.2f}")
    print("\nThis will cost you!")

else:               #end
    price = 12.95
    print(f"\nYour price is: ${price:.2f}")
    print("\nThank you for eating at the Age Buffet!")

#program should run without bugs, be on github and fulfill all asks - J. Smith