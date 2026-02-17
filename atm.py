# ATM Program by Jack Smith

#variable
balance = 1000.00

#match loop
while True:
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    match choice:
        case "1":
            print(f"Balance: ${balance:.2f}")
        
        case "2":
            amt = input("Amount: ")
            if amt.isdigit():
                amount = float(amt)
                if amount > 0:
                    balance += amount
                    print(f"New balance: ${balance:.2f}")
                else:
                    print("Too small")
            else:
                print("Bad")
        
        case "3":
            amt = input("Amount: ")
            if amt.isdigit():
                amount = float(amt)
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"New balance: ${balance:.2f}")
                    else:
                        print("Not enough")
                else:
                    print("Too small")
            else:
                print("Bad")
        
        case "4":
            amt = input("Amount: ")
            if amt.isdigit():
                amount = float(amt)
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"New balance: ${balance:.2f}")
                    else:
                        print("Not enough")
                else:
                    print("Too small")
            else:
                print("Bad")
        
        case "5":
            print("Goodbye")
            break
        
        case _:
            print("Bad choice")

#program should satisfy all conditions - j smith