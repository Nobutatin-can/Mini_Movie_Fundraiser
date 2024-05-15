from datetime import date

today = date.today()        # Get todays date

# Get day, month and year as individual strings

day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "The current date is {}/{}/{}".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# Heading
print(heading)
print("The filename will be {}.txt".format(filename))