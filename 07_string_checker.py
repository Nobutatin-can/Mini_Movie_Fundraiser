# Functions

def string_checker(question, num_letters, valid_responses, error):

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item
            
        print(error)

# Main routine
            
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0,5):

    want_instructions = string_checker("Do you want to see the instructions? (y/n): " ,1 ,yes_no_list, "Please enter yes or no")
    print("You chose", want_instructions)

for case in range(0,5):
    payment_method = string_checker("Do you want to pay cash or credit? ",2 ,payment_list, "please enter a valid payment type")
    print("You chose",payment_method)