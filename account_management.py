import json
import main
from extras.colors import *


def set_main(logged_in, user_name):
    main.choose_game(logged_in, user_name)


def user_account_handler(user_name, user_password):
    """
    This function is responsible for the check and creation of user accounts.
    It checks if the user already exist and logs the user in, if not then the account gets created.
    :param user_name: The users name.
    :param user_password: The users password.
    :return:
    """
    file_path = "account.json"
    data_section = "accountDetails"
    json_username = "username"
    json_password = "password"

    with open(file_path, 'r+') as json_file:
        data = json.load(json_file)
        accounts = data[data_section]

        for user_account in accounts:
            if user_account[json_username] == user_name and user_account[json_password] == user_password:
                print(f"{GREEN}User found logging in{WHITE}, Welcome {MAGENTA}{user_name}{WHITE}")
                set_main(True, user_name)

        print(f"{BLUE}User not found creating account{WHITE}")

        new_entry = {
            "username": user_name,
            "password": user_password
        }

        accounts.append(new_entry)

        json_file.seek(0)
        json.dump(data, json_file, indent=2)
        json_file.truncate()
        json_file.close()
        set_main(True, user_name)


def get_user_score(user_name, game_key):
    file_path = "account.json"
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            for entry in data.get("AccountScore", []):
                if entry.get("username") == user_name:
                    return entry.get(game_key, 0)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return 0


def update_user_score(user_name, new_score, game_key):
    file_path = "account.json"

    with open(file_path, 'r+') as f:
        data = json.load(f)
        if "AccountScore" not in data:
            data["AccountScore"] = []

        scores = data["AccountScore"]
        user_found = False

        for entry in scores:
            if entry.get("username") == user_name:
                current_high = entry.get(game_key, 0)
                if new_score > current_high:
                    entry[game_key] = new_score
                user_found = True
                break

        if not user_found:
            scores.append({"username": user_name, game_key: new_score})

        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()