"""
ASSIGNMENT 6A: TICKET SALES
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
"""

#Jack Smith

# make the list of seats like the hint said

seats = list(range(1, 21))

# keep asking until done

while True:
    # show what seats are left
    print("Available seats:", seats)
    
    # if nothing left, stop
    if len(seats) == 0:
        print("All seats are sold out!")
        break
    
    # ask for a seat
    choice = int(input("Enter seat number (0 to quit): "))
    
    # if they type 0, stop
    if choice == 0:
        print("Thanks for coming!")
        break
    
    # if the seat is still there, sell it
    if choice in seats:
        seats.remove(choice)
        print("Seat", choice, "sold successfully!")
    else:
        print("Sorry Mr., Mrs., They, that seat is gone or doesn't exist.")