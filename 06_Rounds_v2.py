import random

# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print("*** Round #{} ***".format(rounds_played))
    chosen_num = random.randint(1, 100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "Horse"
        else:
            chosen = "Zebra"
        balance -= 0.5


    if balance < 1:
        play_again ="xxx"
        print("Sorry you have ran out of money")
    else:
        play_again = input("Press Enter to play again" " or 'xxx' to quit")

print()
print("Final Balance", balance)
