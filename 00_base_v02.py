import pandas
import random
from datetime import date

# Functions

# Checks that user's response is not blank.
def not_blank(question):

    while True:

        response = input(question)

        if response == "":  # If the response is blank, show an error.
            print("sorry this can't be blank. Please try again")

        else:   # If response is not blank, return the response.
            return response


# Checks that user enters an integer.
def num_check(question):

    while True:

        try:    # Try to turn the user's response (string) into an integer.
            response = int(input(question))
            return response

        except ValueError:  # Show an error if the response is not an integer.
            print("Please enter an integer. ")


# Calculate ticket price based on user's age.
def calc_ticket_price(var_age):

    # Ticket price for users under 16.
    if var_age < 16:
        price = 7.5

    # Ticket price for users between 16 and 64.
    elif var_age <65:
        price = 10.5

    # Ticket price for users between 65 and 120.
    else:
        price = 6.5

    return price


# Checks yes/no and cash/credit.
def string_checker(question, num_letters, valid_responses, error):

    while True:

        response = input(question).lower()  # Make the response lowercase.

        for item in valid_responses:    # Check if the user response is a valid item or first letter/s of a valid item.
            if response == item[:num_letters] or response == item:
                return item
            
        print(error)


# Currency formatting
def currency(x):
    return "${:.2f}".format(x)  


# Instructions
def show_instructions():
    print('''\n
***** Instructions *****
          
For each ticket, enter ...
- The person's name (can't be blank)
- Age (between 12 and 120)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program will then display the ticket details
including the cost of each ticket, the total cost
and the total profit.

This information will be automaticaly written to a text file.

**********************************''')

# Main routine

MAX_TICKETS = 5    # Set the maximum amount of tickets here
tickets_sold = 0

# Valid response lists.
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Lists to hold ticket details.
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create data frame.
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# Ask the user if they want to see the instructions.
want_instructions = string_checker("Do you want to see the instructions? (y/n): ",1 ,yes_no_list, "Please enter 'yes' or 'no'. ")

if want_instructions == "yes":
    show_instructions()

print()


# Loop to sell tickets.

while tickets_sold < MAX_TICKETS:

    name = not_blank("Please enter your name or 'xxx' to quit: ")       # Ask the user for their name.

    if name == 'xxx' and len(all_names) > 0:    # Let user close the program if they have sold at least one ticket.
        break

    elif name == 'xxx': # If no tickets have been sold, tell the user to sell a ticket, then continue the program.
        print("You must sell at least ONE ticket before quitting")
        continue


    # Ask the user for their age and check if it is a number.
    age = num_check("Age: ")        

    if 12 <= age <= 120:        # The user can be between age 12 and 120.
        pass

    elif age < 12:
        print("Sorry you are too young for this movie ")    # Users under 12 are too young.
        continue

    else:
        print("?? That looks like a typo, please try again. ")  # Users over 120 are a typo.
        continue


    # Calculate the base price of the ticket (no surcharge yet) based on the users age.
    ticket_price = calc_ticket_price(age)

    # Ask the user for their payment method.
    payment_method = string_checker("Do you want to pay cash or credit? ",2 ,payment_list, "please enter a valid payment type")

    if payment_method == "cash":
        surcharge = 0   # Users paying with cash do not pay a surcharge.

    else:   # Calculate 5% surcharge if users are paying by credit card.
        surcharge = ticket_price * 0.05


    tickets_sold += 1 
    
    # Add ticket name, cost and surcharge to the lists.
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharge.append(surcharge)

    # Create data frame from dictionary to orginise information.
    mini_movie_frame = pandas.DataFrame(mini_movie_dict)

    # Calculate the total ticket cost (ticket + surcharge).
    mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

    # Calculate profit for each ticket.
    mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

    # Calculate ticket and profit totals.
    total = mini_movie_frame['Total'].sum()
    profit = mini_movie_frame['Profit'].sum()

    # Currency formatting using currency function.
    add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
    for var_item in add_dollars:
        mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

    # Choose winner and look up total won.
    winner_name = random.choice(all_names)
    win_index = all_names.index(winner_name)
    total_won = mini_movie_frame.at[win_index, 'Total']

# Set index at end before printing
    mini_movie_frame = mini_movie_frame.set_index('Name')


# Write to file

today = date.today()        # Get todays date.

# Get the day, month and year as individual strings.

day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "\n---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# Change frame to a string so we can export to a file.
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Create strings for printing.
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
total_profit = "Total Profit After Raffle: ${:.2f}".format(profit - all_ticket_costs[win_index] - all_surcharge[win_index])

if tickets_sold == MAX_TICKETS:
    sales_status = "\n *** All the tickets have been sold ***"
else:
    sales_status = "\n*** You have sold {} out of {} tickets ***".format(tickets_sold, MAX_TICKETS)

winner_heading = "\n----- Raffle Winner -----"
winner_text = "The winner of the raffle is {}. They have won {}. ie: Their ticket is free!".format(winner_name, total_won)

# List holding content to print to the file.
to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales, total_profit, sales_status, winner_heading, winner_text]

# Print the output.
for item in to_write:
    print(item)

# Write the output to a file.
write_to = "{}.txt".format(filename)    # Create file to hold data (add .txt extention)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# Close the text file.
text_file.close()