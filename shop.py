from stock import Stock

print ("   M A I N - M E N U")
print ("1. Create Customer")
print ("2. View Customers")
print ("3. Action 3")
print ("4. Action 4")
print ("5. Action 5")

while True:
    # Get user input:
    choice = input('Enter a choice from the menu [1-5] : ')

    # Convert input (number) to int type:
    choice = int(choice)

    if choice == 1:
        print("Create Customer...")
    elif choice == 2:
        print ("Action 2...")
        #processing #2 is done here
    elif choice == 3:
        print ("Action 3...")
        #processing #3 is done here
    elif choice == 4:
        print ("Create Stock")
        Stock.create_Stock()  
    elif choice == 5:
        print ("Action 5...")
        #processing #5 is done here
    else:
        print ("Invalid entry. You should choose 1-5 only. Program exiting.....please restart it and try again.")
        # Add sys.exit() (will have to add 'import sys' to top

