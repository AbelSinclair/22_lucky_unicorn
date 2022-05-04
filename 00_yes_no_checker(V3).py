# functions go here...
def yes_no(question):
    valid = False
    while not valid:
        # Ask the user if they have played before
        response = input(question).lower()

        # if yes , output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # if no , output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes/no")

# Main routine goes here
show_instructions = yes_no("Have you played the game before")
print("You chose {}".format(show_instructions))
