# Functions

# Calculate ticket price based on user age
def calc_ticket_price(var_age):

    # ticket price for users under 16
    if var_age < 16:
        price = 7.5

    # Ticket price for users between 16 and 64
    elif var_age <65:
        price = 10.5

    # Ticket price for users between 65 and 120
    else:
        price = 6.5

    return price

# Testing loop
while True:

    age = int(input("Age: "))   # Get age


    # Calculate ticket price 
    ticket_price = calc_ticket_price(age)
    print("Age {}, Ticket Price: ${:.2f}".format(age, ticket_price))