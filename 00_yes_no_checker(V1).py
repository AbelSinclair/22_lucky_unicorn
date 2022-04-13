# Ask the user if they have played before
show_instructions = input("Have you played this game before").lower()

# if yes , output ' program continues '
if show_instructions == "yes":
    print("program continues")

elif show_instructions == "y":
    print("program continues")

# if no , output ' display instructions '
elif show_instructions == "no":
    print("display instructions")

elif show_instructions == "n":
    print("display instructions")

else:
    print("Please answer yes/no")
