def yes_no(question):

    while True:

        response = input(question).lower()

        # If the user says yes, return yes
        if response == "yes" or response == "y":
            return "yes"

        # If the user says no, return no
        elif response == "no" or response == "n":
            return "no"

        # If the user inputs anything else, show an error
        else:
            print("Please answer yes / no")

# yes / no checker
show_instructions = ""

want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    print("instructions go here ")  # ********* Change this to a function with instructions later *********
