"""
ASSIGNMENT 6B: THE LOCKED CALENDAR
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
"""

#Jack Smith

# MONTHS is a tuple so it can't be changed - that's why the calendar is locked
MONTHS = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

print("Here are the months in the locked calendar:")
for month in MONTHS:
    print(month)

# try to change the first month (this should fail)
try:
    MONTHS[0] = "New January"   # trying to change a tuple
except TypeError:
    print("Oops! Can't change any month in the calendar.")
    # This failed because MONTHS is a tuple.
    # Tuples are immutable - you can't add, remove, or change anything after you make them.
    # That's why the calendar is "locked"!

print("The calendar stayed exactly the same.")