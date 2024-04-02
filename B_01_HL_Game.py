# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and amke sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an itme in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()
        # checks for an integer more than 0 (allows <enter>)


# Shows user instructions
def instruction():
    print('''

    **** Instructions ****

To begin, choose the number of rounds  and either customise
the game parameters or go with the default game ( where the 
secret number will between 1 and 100).


Then choose how many rounds you'd like to play <enter> 
for infinite mode.

Your  goal is to try to guess the secret number without
running out of guesses.

Press <xxx> to end game at anytime 

Good Luck!
    ''')


def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer "

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more then / equal to {low}")

    # if the number needs to between low and high
    else:
        error = (f"Please enter an integer that is "
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # Check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            return response

        except ValueError:
            print(error)


# checks for integer with optional upper /
# lower limits and optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer "

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more then / equal to {low}")

    # if the number needs to between low and high
    else:
        error = (f"Please enter an integer that is "
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # Check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            return response

        except ValueError:
            print(error)

    error = "Please enter an integer that is 1 or more."

    to_check = input(question)

    # Check for infinite mode
    if to_check == "":
        return "infinite"

    try:
        response = int(to_check)

        # checks that the number is more than / equal to 1

        if response < 1:
            print(error)
        else:
            return response

    except ValueError:
        print(error)


# Main Routine Starts here

# Intialise game variables
mode = "regular"
rounds_played = 0

print(" Higher Or Lower Game")
print()

want_instructions = string_checker("Do you want to read the instruction?")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for numbers of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts  here
while rounds_played < num_rounds:

    # Rounds heading (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n  Round {rounds_played + 1} (Infinite Mode) "
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)
    print()

    # get user choice
    user_choice = input("Choose: ")

    # If user choice os the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game History / Statistics area
