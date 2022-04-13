

# functions go here...
def yes_no(question):
    valid = False
    while not valid:
        responce = input("Have you played this game before").lower()

        if responce == "yes" or responce == "y":
            responce = "yes"
            return responce


        elif responce == "no" or  responce == "n":
            responce = "no"
            return responce

        else:
            print("Please answer yes/no")

# Main routine goes here...
show_instructions = yes_no("Have you played the game before")

