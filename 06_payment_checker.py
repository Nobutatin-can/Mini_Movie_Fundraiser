# Functions

def cash_credit(question):

    while True:

        response = input(question).lower()

        # If the user input is cash
        if response == "cash" or response == "ca":
            return "cash"

        # If the user input is credit
        elif response == "credit" or response == "cr":
            return "credit"

        # If the user inputs anything else, show an error
        else:
            print("Please choose a valid payment method ")
            print()

# Main routine
            
while True:
    payment_method = cash_credit("Choose a payment method ( Cash or Credit ): ")

    print("You chose", payment_method)
    print()