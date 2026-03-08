import random
from itertools import count

WORD_DICTIONARY = "wordlist/galgje_words.txt"

# region Color + logo
RED = "\x1b[1;31m"
WHITE = "\x1b[0m"
GREEN = "\x1b[1;32m"
BLUE = " \x1b[1;34m"
MAGENTA = '\033[35m'
BRIGHT_CYAN = '\033[96m'
NEW_LINE = "\n"


def print_name(user_name):
    print(f"Welcome: {BRIGHT_CYAN}{user_name}\n")


def print_logo():
    logo = RED + r"""          o__ __o                   o                       o                
         /v     v\                 <|>                    _<|>_              
        />       <\                / \                                       
      o/                 o__ __o/  \o/    o__ __o/          o      o__  __o  
     <|       _\__o__   /v     |    |    /v     |          <|>    /v      |> 
      \\          |    />     / \  / \  />     / \         / \   />      //  
        \         /    \      \o/  \o/  \      \o/         \o/   \o    o/    
         o       o      o      |    |    o      |           |     v\  /v __o 
         <\__ __/>      <\__  / \  / \   <\__  < >         < >     <\/> __/> 
                                                |           |                
                                        o__     o   o__     o                
                                        <\__ __/>   <\__ __/>                """ + WHITE
    print(logo)


# endregion

def add_score_to(name, word, score):
    print()


def read_text(k):
    with open(WORD_DICTIONARY, "r") as file:
        words = file.read().splitlines()
        count = len(words)
        if k:
            return count

        if words:
            return random.choice(words)
        else:
            print("The word list is empty.")
            return None


def save_word(file_name, words_dict):
    new_word = input("Voer het nieuwe woord in: ").strip().lower()
    if new_word:
        with open(WORD_DICTIONARY, "a") as file:
            file.write(new_word + "\n")
        print(f"Het woord '{new_word}' is toegevoegd.")
    else:
        print("Geen geldig woord ingevoerd.")


def try_word_guess():
    word_to_guess = read_text(False)

    print("word to guess: " + word_to_guess + "\n")
    word_letters = list(word_to_guess)
    display_word = ["_"] * len(word_letters)
    user_lives = 10
    win = False

    while user_lives > 0 and not win:
        print(f"Word: {' '.join(display_word)}")
        print(f"Lives left: {MAGENTA}{user_lives}{WHITE}")

        user_guess = input("Guess a letter: ").lower()

        if len(user_guess) != 1:
            print(f"Enter only {RED}one{WHITE} letter.")
            continue

        if user_guess in word_letters:
            print(f"{GREEN}Nice!{WHITE}")
            for i in range(len(word_letters)):
                if word_letters[i] == user_guess:
                    display_word[i] = user_guess
        else:
            print(f"{RED}Unfortunate{WHITE}")
            user_lives -= 1

        if "_" not in display_word:
            win = True

    if win:
        print(f"\n{GREEN}Congratulations!{WHITE} You guessed the word: {''.join(display_word)}{WHITE}")
    else:
        print(f"\n{RED}Game over! The word was: {word_to_guess}{WHITE}")



def choose_option():
    print(f"{GREEN}1. Speel galgje{BLUE}\n2. Wijzig een woord in de woordenlijst{MAGENTA}\n3. Voeg woord toe aan de woordenlijst\n{BRIGHT_CYAN}4. Toon aantal woorden in de woordenlijst{RED}\n5. Stoppen\n{WHITE}")
    user_choice = int(input("User selection: "))

    if user_choice == 1:
        try_word_guess()

    if user_choice == 2:
        print("change wordlist")

    if user_choice == 3:
        save_word(WORD_DICTIONARY, "new wor  d2")
        print("add word to wordlist")

    if user_choice == 4:
        print(f"{read_text(True)} words in the wordlist")

    if user_choice == 5:
        print("\nGoodbye")
        quit()


def start_galgje_game():
    print_logo()
    choose_option()
