"""
ASSIGNMENT 5A: INPUT VALIDATION

1. Header Docstring included.
2. All 4 inputs have 'while' loop validation.
3. The Chaperone loop uses .upper() and correct Boolean logic.
4. I have pinned a variable in the WATCH window and took a screenshot.
"""

# 1. Validate First Name (Cannot be blank)
first_name = input("Enter First Name: ")
while first_name == "":
    print("X Error: First Name cannot be blank.")
    first_name = input("Enter First Name: ")

# 2. Validate Last Name (Cannot be blank)
last_name = input("Enter Last Name: ")
while last_name == "":
    print("X Error: Last Name cannot be blank.")
    last_name = input("Enter Last Name: ")

# 3. Validate Chaperone (Must be Y or N)
chaperone = input("Chaperone (Y/N): ").upper()
while chaperone != "Y" and chaperone != "N":
    print("X Error: Must only accept Y, y, N, or n.")
    chaperone = input("Chaperone (Y/N): ").upper()

# 4. Validate Phone Number (Cannot be blank)
phone_number = input("Enter Phone Number: ")
while phone_number == "":
    print("X Error: Phone Number cannot be blank.")
    phone_number = input("Enter Phone Number: ")

# 5. Validate Ticket Count (Must be a valid integer > 0, crash-proof)
ticket_count = 0
while True:
    try:
        ticket_count = int(input("Enter Ticket Count: "))
        if ticket_count > 0:
            break
        print("X Error: Must be a valid integer > 0")
    except ValueError:
        print("X Error: Please enter a number")