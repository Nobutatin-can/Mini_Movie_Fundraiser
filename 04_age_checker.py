# Functions

# Checks that user enters an integer
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer. ")



# Main routine
tickets_sold = 0

while True:

    name = input("Enter your name / 'xxx' to quit: ")   # Ask the user for their name

    if name == "xxx":
        break

    age = num_check("Age: ")    # Ask the user for their age

    if 12 <= age <= 120:    # Users between 12 and 120 can see the movie
        pass

    elif age < 12:      # Users under the age of 12 are too young to see the movie
        print("Sorry you are too young for this movie ")    
        continue

    else:       # Users over the age of 120 are a typo
        print("?? That looks like a typo, please try again. ")
        continue

    tickets_sold += 1

print("You have sold {} ticket/s ".format(tickets_sold))