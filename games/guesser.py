import random

# region Colors
RED = "\x1b[1;31m"
WHITE = "\x1b[0m"
GREEN = "\x1b[1;32m"
BLUE = " \x1b[1;34m"
NEW_LINE = "\n"


# endregion

# region Logo + name
def print_logo():
    logo = RED + r"""         ___           ___           ___           ___           ___           ___           ___     
        /\__\         /\  \         /\__\         /\__\         /\__\         /\__\         /\  \    
       /:/ _/_        \:\  \       /:/ _/_       /:/ _/_       /:/ _/_       /:/ _/_       /::\  \   
      /:/ /\  \        \:\  \     /:/ /\__\     /:/ /\  \     /:/ /\  \     /:/ /\__\     /:/\:\__\  
     /:/ /::\  \   ___  \:\  \   /:/ /:/ _/_   /:/ /::\  \   /:/ /::\  \   /:/ /:/ _/_   /:/ /:/  /  
    /:/__\/\:\__\ /\  \  \:\__\ /:/_/:/ /\__\ /:/_/:/\:\__\ /:/_/:/\:\__\ /:/_/:/ /\__\ /:/_/:/__/___
    \:\  \ /:/  / \:\  \ /:/  / \:\/:/ /:/  / \:\/:/ /:/  / \:\/:/ /:/  / \:\/:/ /:/  / \:\/:::::/  /
     \:\  /:/  /   \:\  /:/  /   \::/_/:/  /   \::/ /:/  /   \::/ /:/  /   \::/_/:/  /   \::/~~/~~~~ 
      \:\/:/  /     \:\/:/  /     \:\/:/  /     \/_/:/  /     \/_/:/  /     \:\/:/  /     \:\~~\     
       \::/  /       \::/  /       \::/  /        /:/  /        /:/  /       \::/  /       \:\__\    
        \/__/         \/__/         \/__/         \/__/         \/__/         \/__/         \/__/    """ + WHITE + NEW_LINE
    print(logo)


def print_name(user_name):
    print_logo()
    print("Welcome: " + user_name + NEW_LINE)


# endregion

def check_valid_input(user_input):
    if not user_input.strip():
        print("No valid input")
        return False
    else:
        if user_input.isdigit():
            return True
        print("Enter a valid number")
        return False


def generate_number_to_guess(difficulty):
    minimum_number = 1

    easy_mode_max_guess_number = 10
    normal_mode_max_guess_number = 50
    hard_mode_max_guess_number = 100

    if difficulty == 1:
        return random.randint(minimum_number, easy_mode_max_guess_number)

    elif difficulty == 2:
        return random.randint(minimum_number, normal_mode_max_guess_number)

    elif difficulty == 3:
        return random.randint(minimum_number, hard_mode_max_guess_number)
    return random.randint(minimum_number, easy_mode_max_guess_number)


def user_max_tries(difficulty):
    easy_mode_max_tries = 5
    normal_mode_max_tries = 7
    hard_mode_max_tries = 10

    if difficulty == 1:
        return easy_mode_max_tries

    elif difficulty == 2:
        return normal_mode_max_tries

    elif difficulty == 3:
        return hard_mode_max_tries
    return easy_mode_max_tries


def mode_handler():
    print("Pick your difficulty \n" + GREEN + " 1. Easy (1-10)" + BLUE + "\n 2. Normal (1-50)\n" + RED + " 3. Hard (1-100)\n " + WHITE)
    user_pick = input("Select which difficulty: ", )

    if not check_valid_input(user_pick):
        return mode_handler()

    user_pick = int(user_pick)

    easy_mode_max_guess = 10
    normal_mode_max_guess = 50
    hard_mode_max_guess = 100

    easy_mode_max_tries = 5
    normal_mode_max_tries = 7
    hard_mode_max_tries = 10

    if user_pick == 1:
        print(GREEN + "Easy mode is chosen\n" + WHITE)
        return easy_mode_max_guess, easy_mode_max_tries, 1

    if user_pick == 2:
        print(BLUE + "Normal mode is chosen\n" + WHITE)
        return normal_mode_max_guess, normal_mode_max_tries, 2

    if user_pick == 3:
        print(RED + "Hard mode is chosen \n" + WHITE)
        return hard_mode_max_guess, hard_mode_max_tries, 3
    else:
        print("Chose a difficulty (numbers only).")
        return mode_handler()


def calculate_difficulty(user_score):
    low_score = 5
    normal_score = 12

    if user_score < low_score:
        return print("Try a lower difficulty")
    elif low_score <= user_score <= normal_score:
        return print("Keep this difficulty")
    else:
        return print("Advies: je kunt een hogere moeilijkheidsgraad aan!")


def calculate_score(difficulty_level, user_tries):
    score = (user_max_tries(difficulty_level) - user_tries) * difficulty_level
    return score


def start_guess_game():
    has_won = False
    user_tries = 0
    add_one = 1

    max_guess_number, max_tries, difficulty_level = mode_handler()

    number_to_guess = generate_number_to_guess(difficulty_level)
    print("number to guess: " + str(number_to_guess))

    while user_tries < max_tries:
        user_guess = input("number guess: ")

        if check_valid_input(user_guess):
            user_guess = int(user_guess)
            user_tries += add_one
            remaining = max_tries - user_tries

            print("Tries left: " + RED + str(remaining) + WHITE + ", User tries: " + BLUE + str(user_tries) + WHITE)

            if user_guess == number_to_guess:
                has_won = True
                break
            else:
                difference = abs(user_guess - number_to_guess)
                if difference <= 2:
                    print("Your close!")

            if user_guess < number_to_guess:
                print("Higher")
            else:
                print("Lower")

    if has_won:
        score = calculate_score(difficulty_level, user_tries)
        print(f"Number guessed! Your score is:{BLUE}{score}{WHITE}")
        calculate_difficulty(score)

    else:
        print("You ran out of " + RED + "tries" + WHITE + ", the number was " + RED + str(number_to_guess) + WHITE)
        score = 0
        print("Your score is: " + RED + str(score) + WHITE)
        calculate_difficulty(score)

    start_game_again()


def start_game_again():
    play_again = input(f"\nWould you like to play again? ({GREEN}y{WHITE}/{RED}n{WHITE}): ")

    if play_again == "y":
        start_guess_game()
    else:
        print("Till next time")
