# Functions

# Checks that user response is not blank
def not_blank(question):

    while True:

        response = input(question)

        if response == "":  # If response is blank, show an error
            print("sorry this can't be blank. Please try again")

        else:   # If response is not blank, return the response
            return response


# Main routine
        
while True:

    name = not_blank("Enter your name (or 'xxx' to quit)")

    if name == "xxx":
        break

print("We are done")