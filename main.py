from games import guesser, galgje
import json

red = "\x1b[1;31m"
green = "\x1b[1;32m"
blue = "\x1b[1;34m"
reset = "\x1b[0m"


def print_logo():
    logo = red + r""" 
         <-. (`-')_ (`-')  _ <-. (`-')_            <-. (`-')_  _     <-. (`-')_                (`-').->  _     <-. (`-')   _  (`-')          (`-')  _               (`-')  _ <-. (`-')   (`-')  _ (`-').-> 
       \( OO) )(OO ).-/    \( OO) )     .->      \( OO) )(_)       \( OO) )    .->        ( OO)_   (_)       \(OO )_  \-.(OO )   <-.    ( OO).-/        .->    (OO ).-/    \(OO )_  ( OO).-/ ( OO)_   
    ,--./ ,--/ / ,---.  ,--./ ,--/ (`-')----. ,--./ ,--/ ,-(`-'),--./ ,--/  ,---(`-')    (_)--\_)  ,-(`-'),--./  ,-.) _.'    \ ,--. )  (,------.     ,---(`-') / ,---.  ,--./  ,-.)(,------.(_)--\_)  
    |   \ |  | | \ /`.\ |   \ |  | ( OO).-.  '|   \ |  | | ( OO)|   \ |  | '  .-(OO )    /    _ /  | ( OO)|   `.'   |(_...--'' |  (`-') |  .---'    '  .-(OO ) | \ /`.\ |   `.'   | |  .---'/    _ /  
    |  . '|  |)'-'|_.' ||  . '|  |)( _) | |  ||  . '|  |)|  |  )|  . '|  |)|  | .-, \    \_..`--.  |  |  )|  |'.'|  ||  |_.' | |  |OO )(|  '--.     |  | .-, \ '-'|_.' ||  |'.'|  |(|  '--. \_..`--.  
    |  |\    |(|  .-.  ||  |\    |  \|  |)|  ||  |\    |(|  |_/ |  |\    | |  | '.(_/    .-._)   \(|  |_/ |  |   |  ||  .___.'(|  '__ | |  .--'     |  | '.(_/(|  .-.  ||  |   |  | |  .--' .-._)   \ 
    |  | \   | |  | |  ||  | \   |   '  '-'  '|  | \   | |  |'->|  | \   | |  '-'  |     \       / |  |'->|  |   |  ||  |      |     |' |  `---.    |  '-'  |  |  | |  ||  |   |  | |  `---.\       / 
    `--'  `--' `--' `--'`--'  `--'    `-----' `--'  `--' `--'   `--'  `--'  `-----'       `-----'  `--'   `--'   `--'`--'      `-----'  `------'     `-----'   `--' `--'`--'   `--' `------' `-----'  """ + reset
    print(logo)


def credentials():
    """
    Instead of repeated usages of the same snippet of code this function enables the user to enter there details without being present in both functions.
    :return: The user input of their username and password.
    """
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")
    return user_name, user_password


def user_login_create_json(user_name, user_password):
    """
    This function is responsible for the check and creation of user accounts.
    It checks if the user already exist and logs the user in, if not then the account gets created.
    :param user_name: The users name.
    :param user_password: The users password
    :return:
    """
    file_path = 'account.json'

    with open(file_path, 'r+') as json_file:
        data = json.load(json_file)
        accounts = data["accountDetails"]

        for account in accounts:
            if account["username"] == user_name and account["password"] == user_password:
                print("User found logging in")
                choose_game(True, user_name)
                return

        print("User not found creating account")

        new_entry = {
            "username": user_name,
            "password": user_password
        }

        accounts.append(new_entry)

        json_file.seek(0)
        json.dump(data, json_file, indent=2)
        json_file.truncate()
        choose_game(True, user_name)


def log_in():
    print("\nLog in\n")
    user_details = credentials()
    user_login_create_json(user_details[0], user_details[1])


def create_account():
    print("\nCreate a account\n")
    user_details = credentials()
    user_login_create_json(user_details[0], user_details[1])


def account():
    print("\n1. to login into your account\n2. to create a account\n")
    choose_detail = int(input(""))

    if choose_detail == 1:
        log_in()
    else:
        create_account()


def choose_game(logged_in, user_name):
    """
       Main function that lets the user pick the game they want to play and gives the username.
       :return:
    """
    if logged_in:
        print("\nPick a game to play:\n" + green + "1. Guesser\n" + reset + blue + "2. Galgje" + reset)

        user_pick = int(input("Enter game choice: "))
        if user_pick == 1:
            guesser.print_name(user_name)
            guesser.start_guess_game()


        elif user_pick == 2:
            galgje.start_galgje_game()
            galgje.print_name(user_name)
        else:
            print("Invalid selection.")


def main():
    print_logo()
    # account()
    choose_game(True,"k")


if __name__ == '__main__':
    main()

# een script wat de functies heeft dus dan hoef je alleen een string door te geven waardoor je de functions.py import en dan een variable meegeeft en dat het returned
