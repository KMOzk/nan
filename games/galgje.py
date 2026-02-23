import random

red = "\x1b[1;31m"
white = "\x1b[0m"
word_directory = "wordlist/galgje_words.txt"

def print_name(user_name):
    print("Welcome: " + user_name + "\n")

def print_logo():
    logo = red + r"""      o__ __o                   o                       o                
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
                                        <\__ __/>   <\__ __/>                """ + white
    print(logo)


def add_score_to(name, word, score):
    print()


def read_text():
    with open(word_directory, "r") as file:
        words = file.read().splitlines()

        if words:
            return random.choice(words)
        else:
            print("The word list is empty.")
            return None


def save_word(file_name, words_dict):
    print("")


def try_word_guess():
    word_to_guess = read_text()

    print("word to guess: " + word_to_guess+"\n")

    user_guess = input("")
    user_guess.lower()

    # for every_word in word_to_guess:
    #     print

    if not word_to_guess:
        print("No word")
        return





def choose_option():
    print("1. Speel galgje\n2. Wijzig een woord in de woordenlijst\n3. Voeg woord toe aan de woordenlijst\n4. Toon aantal woorden in de woordenlijst\n5. Stoppen\n")
    user_choice = int(input("User selection: "))

    if user_choice == 1:
        try_word_guess()

    if user_choice == 2:
        print("change wordlist")

    if user_choice == 3:
        print("add word to wordlist")

    if user_choice == 4:
        print("show number of words in wordlist")

    if user_choice == 5:
        print("\nGoodbye")
        quit()


def start_galgje_game():
    print_logo()
    choose_option()
