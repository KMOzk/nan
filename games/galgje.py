import random
from extras import logos
from extras.colors import *

WORD_DICTIONARY = "wordlist/galgje_words.txt"
SCORE_TEXT = "score_galgje.txt"


def read_text(file_name):
    word_dict = {}
    try:
        with open(file_name, "r") as file:
            for word in file.read().splitlines():
                if len(word) < 6:
                    word_dict[word] = 1
                elif 7 <= len(word) <= 11:
                    word_dict[word] = 2
                else:
                    word_dict[word] = 3
    except FileNotFoundError:
        print(f"{RED}Error: Wordlist file '{file_name}' not found.{WHITE}")

        word_dict = {"apple": 1, "programming": 3, "python": 2}

    return word_dict


def saved_word(file_name, words_dict):
    with open(file_name, "w") as file:
        for word in words_dict.keys():
            file.write(word + "\n")


def add_score_to(name, word, score):
    with open(SCORE_TEXT, "a") as file:
        file.write(f"{name} {word} {score}\n")


def print_logo():
    logos.print_galgje_logo()


def print_name(user_name):
    print(f"Welcome: {BRIGHT_CYAN}{user_name}")


def show_progress(word, guessed_letters):
    display = []
    for letter in word:
        if letter in guessed_letters:
            display.append(letter.upper())
        else:
            display.append("_")
    return " ".join(display)


def calculate_score(lives_left, difficulty):
    return lives_left * difficulty


def chose_word(word_dict, difficulty_level):
    valid_words = []
    for word, difficulty in word_dict.items():
        if difficulty == difficulty_level:
            valid_words.append(word)

    if valid_words:
        return random.choice(valid_words)
    return None


def change_wordlist(galge_word_dict):
    word = input("Enter word to remove: ").strip().lower()
    if word in galge_word_dict:
        del galge_word_dict[word]
        saved_word(WORD_DICTIONARY, galge_word_dict)
        print(f"The word '{word}' has been successfully removed.")
    else:
        print("Word not found in the list.")


def add_word_to(galge_word_dict):
    new_word = input("Add new word: ").strip().lower()
    if new_word:
        if len(new_word) < 6:
            galge_word_dict[new_word] = 1
        elif 7 <= len(new_word) <= 11:
            galge_word_dict[new_word] = 2
        else:
            galge_word_dict[new_word] = 3

        saved_word(WORD_DICTIONARY, galge_word_dict)
        print(f"The word '{new_word}' has been added.")
    else:
        print("Invalid word entered.")


def try_word_guess(player_name, galge_word_dict):
    print(f"\nDifficulty:\n"
          f"{GREEN}1. Easy (Wordlength < 6 | 10 lives){WHITE}\n"
          f"{BLUE}2. Medium (Wordlength 7-11 | 8 lives){WHITE}\n"
          f"{BRIGHT_RED}3. Hard (Wordlength > 11 | 6 lives){WHITE}")

    user_input = input("Pick your difficulty: ")

    if user_input == "1":
        lives, difficulty = 10, 1
    elif user_input == "2":
        lives, difficulty = 8, 2
    elif user_input == "3":
        lives, difficulty = 6, 3
    else:
        print(f"{RED}Invalid choice. Defaulting to Easy.{WHITE}")
        lives, difficulty = 10, 1

    word_to_guess = chose_word(galge_word_dict, difficulty)

    if not word_to_guess:
        print("No words found for this difficulty.")
        return

    guessed_letters = []
    wrong_letters = []
    win = False

    while lives > 0 and not win:
        print(f"\nWord: {show_progress(word_to_guess, guessed_letters)}")
        print(f"Wrong guesses: {', '.join(wrong_letters)}")
        print(f"Lives left: {MAGENTA}{lives}{WHITE}")

        user_guess = input("Guess a letter (or press Enter to quit): ").strip().lower()

        if not user_guess:
            print("Session aborted.")
            return

        if len(user_guess) != 1:
            print(f"Enter only {RED}one{WHITE} letter.")
            continue

        if user_guess in guessed_letters or user_guess in wrong_letters:
            print(f"{BLUE}You already guessed '{user_guess}'. No lives lost.{WHITE}")
            continue

        if user_guess in word_to_guess:
            print(f"{GREEN}Nice!{WHITE}")
            guessed_letters.append(user_guess)
        else:
            print(f"{RED}Unfortunate{WHITE}")
            wrong_letters.append(user_guess)
            lives -= 1

        if "_" not in show_progress(word_to_guess, guessed_letters):
            win = True

    if win:
        print(f"\n{GREEN}Congratulations!{WHITE} You guessed the word: {BRIGHT_CYAN}{word_to_guess.upper()}{WHITE}")
    else:
        print(f"\n{RED}Game over! The word was: {word_to_guess.upper()}{WHITE}")

    score = calculate_score(lives, difficulty)
    add_score_to(player_name, word_to_guess, score)
    print(f"Score ({score}) saved!")


def choose_option(player_name, galge_word_dict):
    print(f"\n{GREEN}1. Play Hangman"
          f"{BLUE}\n2. Remove a word from the word list"
          f"{MAGENTA}\n3. Add a word to the word list\n"
          f"{BRIGHT_CYAN}4. Show number of words in the word list"
          f"{RED}\n5. Quit\n"
          f"{WHITE}")

    user_choice = input("User selection: ")

    match user_choice:
        case "1":
            try_word_guess(player_name, galge_word_dict)
        case "2":
            change_wordlist(galge_word_dict)
        case "3":
            add_word_to(galge_word_dict)
        case "4":
            print(f"{BRIGHT_BLUE}{len(galge_word_dict)}{WHITE} words in the word list.")
        case "5":
            print("\nGoodbye")
            quit()
        case _:
            print(f"\n{BRIGHT_RED}Invalid{WHITE} choice.")


def start_galgje_game(name):
    galge_word_dict = read_text(WORD_DICTIONARY)
    print_logo()
    print_name(name)
    choose_option(name, galge_word_dict)
