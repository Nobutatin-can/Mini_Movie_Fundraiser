# Main routine

# *********** Set the max amount of tickets here ***********
MAX_TICKETS = 3

# Loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:

    name = input("Please enter your name or 'xxx' to quit: ") # Ask user for their name

    if name == 'xxx':
        break

    tickets_sold += 1 # tickets_sold +=1 placed after exit to ensure exit is not counted as a ticket purchase
    

# Output number of tickets sold   
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")

else:
    print("You have sold {} ticket/s. There is {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))  