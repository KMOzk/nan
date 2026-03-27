import random
from extras import logos
import account_management
from extras.colors import *


# region Logo
def print_logo():
    logos.print_guesser_logo()


# endregion

GAME_KEY = "score_guesser"


def check_valid_input(user_input):
    if not user_input.strip():
        print("No valid input")
        return False
    else:
        if user_input.lstrip('-').isdigit():
            return True
        print(f"{RED}Enter a valid number{WHITE}")
        return False


def generate_number_to_guess(difficulty, lowest=1, highest=10):
    minimum_number = 1

    easy_mode_max_guess_number = 10
    normal_mode_max_guess_number = 50
    hard_mode_max_guess_number = 100

    match difficulty:
        case 1:
            return random.randint(minimum_number, easy_mode_max_guess_number)

        case 2:
            return random.randint(minimum_number, normal_mode_max_guess_number)

        case 3:
            return random.randint(minimum_number, hard_mode_max_guess_number)
        case 4:
            return random.randint(lowest, highest)
        case _:
            return random.randint(minimum_number, easy_mode_max_guess_number)


def user_max_tries(difficulty, custom_tries=5):
    easy_mode_max_tries = 5
    normal_mode_max_tries = 7
    hard_mode_max_tries = 10

    match difficulty:
        case 1:
            return easy_mode_max_tries
        case 2:
            return normal_mode_max_tries
        case 3:
            return hard_mode_max_tries
        case 4:
            return custom_tries
        case _:
            return easy_mode_max_tries


def custom_mode():
    while True:
        user_input_tries = input("How many tries?: ")
        user_input_lowest_number = input("Lowest number: ")
        user_input_highest_number = input("Highest number: ")

        if check_valid_input(user_input_tries) and check_valid_input(user_input_lowest_number) and check_valid_input(user_input_highest_number):
            tries = int(user_input_tries)
            lowest = int(user_input_lowest_number)
            highest = int(user_input_highest_number)

            if lowest >= highest:
                print(f"{RED}Lowest{WHITE} number must be {BRIGHT_RED}smaller{WHITE} than the {BLUE}highest{WHITE} number.")
                continue
            if tries <= 0:
                print(f"{RED}Tries{WHITE} must be greater than {BRIGHT_RED}0{WHITE}.")
                continue

            print(f"{GREEN}Custom{WHITE} mode is chosen\n")
            return lowest, highest, tries, 4


def mode_handler():
    print(f"Pick your difficulty \n"
          f"{GREEN} 1. Easy (1-10)"
          f"{BLUE}\n 2. Normal (1-50)\n"
          f"{RED} 3. Hard (1-100)\n "
          f"{MAGENTA}4. Custom"
          f"{WHITE}")
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

    match user_pick:
        case 1:
            print(f"{GREEN}Easy mode is chosen\n{WHITE}")
            return 1, easy_mode_max_guess, easy_mode_max_tries, 1
        case 2:
            print(f"{BLUE}Normal mode is chosen\n{WHITE}")
            return 1, normal_mode_max_guess, normal_mode_max_tries, 2
        case 3:
            print(f"{RED}Hard mode is chosen \n{WHITE}")
            return 1, hard_mode_max_guess, hard_mode_max_tries, 3
        case 4:
            return custom_mode()
        case _:
            print(f"Chose a difficulty ({RED}numbers{WHITE} only).")
            return mode_handler()


def calculate_difficulty(user_score):
    low_score = 5
    normal_score = 12

    if user_score < low_score:
        return print(f"Try a {RED}lower{WHITE} difficulty")
    elif low_score <= user_score <= normal_score:
        return print(f"{GREEN}Keep this difficulty{WHITE}")
    else:
        return print(f"Try a {RED}harder{WHITE} difficulty!")


def calculate_score(difficulty_level, user_tries):
    score = (user_max_tries(difficulty_level) - user_tries) * difficulty_level
    return score


def start_guess_game(user_name):
    print_logo()
    old_score = account_management.get_user_score(user_name, GAME_KEY)
    print(f"Welcome back {BRIGHT_CYAN}{user_name}{WHITE}! Your {RED}previous{WHITE} highscore was: {BRIGHT_CYAN}{old_score}{WHITE}\n")

    has_won = False
    user_tries = 0
    add_one = 1

    lowest_number, max_guess_number, max_tries, difficulty_level = mode_handler()

    number_to_guess = generate_number_to_guess(difficulty_level, lowest_number, max_guess_number)

    while user_tries < max_tries:
        user_guess = input("Number guess (or press enter to stop): ").strip()

        if not user_guess:
            print(f"{BRIGHT_RED}Session stopped.{WHITE}")
            return

        try:
            user_guess = int(user_guess)
        except ValueError:
            print(f"{BRIGHT_RED}Please enter a valid number.{WHITE}")
            continue

        user_tries += add_one
        remaining = max_tries - user_tries

        if user_guess == number_to_guess:
            has_won = True
            break
        else:
            difference = abs(user_guess - number_to_guess)
            if difference <= 2:
                print(f"You're {GREEN}close!{WHITE}")

            if user_guess < number_to_guess:
                print(f"{BRIGHT_CYAN}Higher{WHITE}")
            else:
                print(f"{RED}Lower{WHITE}")

            current_score = calculate_score(difficulty_level, user_tries)
            print(f"Tries left: {RED}{remaining}{WHITE}, Current score: {BLUE}{current_score}{WHITE}\n")

    if has_won:
        score = calculate_score(difficulty_level, user_tries)
        print(f"Number guessed! Your score is: {BLUE}{score}{WHITE}")
    else:
        score = 0
        print(f"You ran out of {RED}tries{WHITE}, the number was {RED}{number_to_guess}{WHITE}")
        print(f"Your score is: {RED}{score}{WHITE}")

    calculate_difficulty(score)
    account_management.update_user_score(user_name, score, GAME_KEY)
    start_game_again(user_name)


def start_game_again(username):
    play_again = input(f"\nWould you like to play again? ({GREEN}y{WHITE}/{RED}n{WHITE}): ")

    match play_again:
        case "y":
            start_guess_game(username)
        case _:
            print("Till next time")
