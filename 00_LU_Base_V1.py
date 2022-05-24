# imports

# Functions
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

def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"
    valid = False
    while not valid:
         try:
             # ask the question
             response = int(input(question))
             # if the amount is too low / too high give
             if low < response <= high:
                                   return response

             # output an error
             else:
                 print(error)


         except ValueError:

                     print(error)

# Main Routine
played_before = yes_no("Have you played before?")

# played before checker
if played_before == "no":
    instructions()

# number check
how_much = num_check("How much would you like to play with?", 0, 10)

# how much
print("You will be spending ${}".format(how_much))
