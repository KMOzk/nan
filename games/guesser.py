import random

red = "\x1b[1;31m"
white = "\x1b[0m"
green = "\x1b[1;32m"
blue = " \x1b[1;34m"
new_line = "\n"

max_tries = 5

def print_logo():
    logo = red + r"""        ___           ___           ___           ___           ___           ___           ___     
        /\__\         /\  \         /\__\         /\__\         /\__\         /\__\         /\  \    
       /:/ _/_        \:\  \       /:/ _/_       /:/ _/_       /:/ _/_       /:/ _/_       /::\  \   
      /:/ /\  \        \:\  \     /:/ /\__\     /:/ /\  \     /:/ /\  \     /:/ /\__\     /:/\:\__\  
     /:/ /::\  \   ___  \:\  \   /:/ /:/ _/_   /:/ /::\  \   /:/ /::\  \   /:/ /:/ _/_   /:/ /:/  /  
    /:/__\/\:\__\ /\  \  \:\__\ /:/_/:/ /\__\ /:/_/:/\:\__\ /:/_/:/\:\__\ /:/_/:/ /\__\ /:/_/:/__/___
    \:\  \ /:/  / \:\  \ /:/  / \:\/:/ /:/  / \:\/:/ /:/  / \:\/:/ /:/  / \:\/:/ /:/  / \:\/:::::/  /
     \:\  /:/  /   \:\  /:/  /   \::/_/:/  /   \::/ /:/  /   \::/ /:/  /   \::/_/:/  /   \::/~~/~~~~ 
      \:\/:/  /     \:\/:/  /     \:\/:/  /     \/_/:/  /     \/_/:/  /     \:\/:/  /     \:\~~\     
       \::/  /       \::/  /       \::/  /        /:/  /        /:/  /       \::/  /       \:\__\    
        \/__/         \/__/         \/__/         \/__/         \/__/         \/__/         \/__/    """ + white + new_line
    print(logo)

def print_name(user_name):
    print_logo()
    print("Welcome: " + user_name + new_line)

def generate_number_to_guess(difficulty):
    print("")


def mode_handler():
    print("")


def user_max_tries(difficulty):
    max_tries = difficulty
    return max_tries

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
    print("Your score is: " + str(score))


def start_guess_game():

    has_won = False
    print("Pick your difficulty \n" + green + " 1. easy" + blue + "\n 2. normal\n" + red + " 3. hard\n " + white)
    user_pick = int(input("Which difficulty: ", ))

    easy_mode_max_guess = 10
    normal_mode_max_guess = 50
    hard_mode_max_guess = 100

    max_guess_number = 0

    easy_mode_max_tries = 5
    normal_mode_max_tries = 7
    hard_mode_max_tries = 10
    difficulty_level = 0
    user_tries = 0
    max_tries = 5

    add_one = 1

    if user_pick == 1:
        max_guess_number = easy_mode_max_guess
        max_tries = easy_mode_max_tries
        difficulty_level = 1
        print(green + "Easy mode is chosen\n" + white)

    if user_pick == 2:
        max_guess_number = normal_mode_max_guess
        max_tries = normal_mode_max_tries
        difficulty_level = 2
        print(blue + "Normal mode is chosen\n" + white)

    if user_pick == 3:
        max_guess_number = hard_mode_max_guess
        max_tries = hard_mode_max_tries
        difficulty_level = 3
        print(red + "Hard mode is chosen \n" + white)

    number_to_guess = random.randint(1, max_guess_number)
    print("number to guess: " + str(number_to_guess))

    while user_tries < max_tries:

        user_guess = int(input("number guess: "))
        user_tries += add_one

        remaining = max_tries - user_tries
        print("User tries: " + blue + str(user_tries) + white)
        print("Tries left: " + red + str(remaining) + white)

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
        score = (max_tries - user_tries) * difficulty_level
        print("Your score is: " + blue + str(score) + white)
        calculate_difficulty(score)
    else:
        print("You ran out of " + red + "tries" + white + ", the number was " + red + str(number_to_guess) + white)
        score = 0
        print("Your score is: " + red + str(score) + white)
    calculate_difficulty(user_tries)

    start_again = int(input("Want to play again? Press 1: "))
    if start_again == 1:
        start_guess_game()
    else:
        print("Till next time")