from extras.colors import *
from games import guesser, galgje
from api import api_animal, weather_api
import account_management
from extras import logos, rekenmenen


# region LOGO
def print_logo():
    logos.print_main_logo()


# endregion


def get_credentials():
    """
    Instead of repeated usages of the same snippet of code this function enables the user to enter there details without being present in both functions.
    :return: The user input of their username and password.
    """
    user_name = input("Enter username: ").strip()
    user_password = input("Enter password: ").strip()
    return user_name, user_password


def check_valid_input(user_input):
    """
    Checks if the given useer_input is a valid response and if it is a digit.
    :param user_input: The input given by the player.
    :return: If the input isn't valid we return None but if the input is a digit we return the int value.
    """
    if not user_input.strip():
        print("No valid input")
        return None

    if user_input.isdigit():
        return int(user_input)
    return None


def space_in_text(given_text):
    """
    Adds a new line before and after the given_text.
    :param given_text: The given text we want to be centered.
    :return: Nothing.
    """
    text = f"\n{given_text}\n"
    print(text)


def handle_account_action(action_text):
    """"
    :parameter action_text:
    """
    space_in_text(action_text)
    username, password = get_credentials()
    account_management.user_account_handler(username, password)
    return username


def ask_account():
    """
    Ask user if he wants to log in or create an account.
    :return:Nothing.
    """
    while True:
        print(f"{BLUE}1.{WHITE} to {BLUE}login{WHITE} into your account\n{GREEN}2.{WHITE} to {GREEN}create{WHITE} a account\n")
        choose_detail = check_valid_input(input(""))

        match choose_detail:
            case 1:
                return handle_account_action(f"{BLUE}Log in{WHITE}")
            case 2:
                return handle_account_action("Create a account")
            case _:
                print(f"{RED}Invalid{WHITE} selection. Try again.\n")


def choose_game(logged_in, user_name):
    """
       Main function that lets the user pick the game they want to play and gives the username.
       :parameter logged_in: If the user is logged then we show the game selection.
       :parameter user_name: The username we are going to display.
       :return: Nothing.
    """
    if not logged_in:
        return

    while logged_in:
        print(f"\nPick a game to play:\n"
              f"{BRIGHT_GREEN} 1. Guesser\n"
              f"{BRIGHT_BLUE} 2. Galgje\n"
              f"{MAGENTA} 3. Animal facts API\n"
              f"{BRIGHT_CYAN} 4. Weather guesser api\n"
              f"{BRIGHT_RED} 5. Rekenmenen\n"
              f"{WHITE}"
              )

        enter_game_text = f"Enter {BRIGHT_BLUE}game{WHITE} choice: "

        user_pick = input(enter_game_text)

        match user_pick:
            case "1"| "Guesser":
                guesser.start_guess_game(user_name)

            case "2"|"Galgje":
                galgje.start_galgje_game(user_name)

            case "3"|"Animal facts API":
                api_animal.start_api_animal(user_name)

            case "4"| "Weather":
                weather_api.get_city()

            case "5" | "Reken":
                rekenmenen.choices()
            case _:
                print(f"{RED}Invalid{WHITE} selection. Try again\n")


def main():
    """
    The main function organizing the loop of the game.
    """
    print_logo()
    # ask_account()
    choose_game(True, "k")


if __name__ == '__main__':
    main()
