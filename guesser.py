import random

def start_guess_game():
    RED = "\x1b[1;31m"
    RESET = "\x1b[0m"

    LOGO = RED + r"""    ___           ___           ___           ___           ___           ___           ___     
     /\__\         /\  \         /\__\         /\__\         /\__\         /\__\         /\  \    
    /:/ _/_        \:\  \       /:/ _/_       /:/ _/_       /:/ _/_       /:/ _/_       /::\  \   
   /:/ /\  \        \:\  \     /:/ /\__\     /:/ /\  \     /:/ /\  \     /:/ /\__\     /:/\:\__\  
  /:/ /::\  \   ___  \:\  \   /:/ /:/ _/_   /:/ /::\  \   /:/ /::\  \   /:/ /:/ _/_   /:/ /:/  /  
 /:/__\/\:\__\ /\  \  \:\__\ /:/_/:/ /\__\ /:/_/:/\:\__\ /:/_/:/\:\__\ /:/_/:/ /\__\ /:/_/:/__/___
 \:\  \ /:/  / \:\  \ /:/  / \:\/:/ /:/  / \:\/:/ /:/  / \:\/:/ /:/  / \:\/:/ /:/  / \:\/:::::/  /
  \:\  /:/  /   \:\  /:/  /   \::/_/:/  /   \::/ /:/  /   \::/ /:/  /   \::/_/:/  /   \::/~~/~~~~ 
   \:\/:/  /     \:\/:/  /     \:\/:/  /     \/_/:/  /     \/_/:/  /     \:\/:/  /     \:\~~\     
    \::/  /       \::/  /       \::/  /        /:/  /        /:/  /       \::/  /       \:\__\    
     \/__/         \/__/         \/__/         \/__/         \/__/         \/__/         \/__/    """ + RESET
    print(LOGO)
    while True:
        selection = (1, 2, 3)
        easy_mode_max_number = 10
        normal_mode_max_number = 50
        hard_mode_max_number = 100
        max_number_of_height = 0
        user_tries = 0
        max_tries = 10
        has_won = False

        user_pick = int(input("\n pick your difficulty \n\x1b[1;32m 1. easy\x1b[0m \n\x1b[1;34m 2. normal\x1b[0m \n\x1b[1;31m 3. hard\x1b[0m \n Which difficulty: ", ))

        if user_pick == 1:
            max_number_of_height = easy_mode_max_number
            print("1 is chosen")
        if user_pick == 2:
            max_number_of_height = normal_mode_max_number
            print("2 is chosen")
        if user_pick == 3:
            max_number_of_height = hard_mode_max_number
        print("3 is chosen")

        number_to_guess = random.randint(1, max_number_of_height)
        print(number_to_guess)
        user_guess = int(input("number guess "))
        max_tries -= 1
        user_tries += 1

        if user_guess == number_to_guess & user_tries != 0:
            has_won = True
        else:
            user_pick = int(input("wrong try again ", ))

        if has_won:
            score = (max_tries - user_tries) * max_number_of_height
            print(score)
            break