

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


def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""

# Main routine goes here
played_before = yes_no("Have you played the game before")


if played_before == "no":
    instructions()
elif played_before == "yes":
    print("Program Continues")
