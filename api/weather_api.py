import requests
from extras import logos
from extras.colors import *

KEY = "3a82f8cac925f7266f434c23f1e9d8d7"


def print_logo():
    logos.print_weather_logo()


def ask_user_tries():
    user_number = 10

    user_input = input(f"How many tries do you wanna guess? (default number of guesses {user_number}): ")
    if user_input.isdigit():
        user_number = int(user_input)
        return user_number
    else:
        return user_number


def show_weather(user_city, temperature, won):
    if temperature <= 0:
        color = BLUE
    elif 0 < temperature < 15:
        color = BRIGHT_CYAN
    elif 15 <= temperature < 25:
        color = GREEN
    else:
        color = RED

    if not won:
        print(f"The temperature in {BRIGHT_CYAN}{user_city}{WHITE} is:{color} {temperature}{WHITE}")
    else:
        print(f"Number {BLUE}guessed{WHITE}! The weather in {BRIGHT_CYAN}{user_city}{WHITE} is: {color}{temperature}{WHITE}")


def guess_game(user_city, temperature):
    give_up = False
    has_won = False
    user_tries = ask_user_tries()
    number_to_guess = round(temperature)

    while not give_up | user_tries <= 0:
        user_input = input(f"Guess the weather in {BRIGHT_CYAN}{user_city}{WHITE} (round up or down | stop to show the weather ): ")

        if user_input == "stop":
            give_up = True
        else:
            user_guess = int(user_input)
            user_tries -= 1
            print(f"Tries left {RED}{user_tries}{WHITE}")
            if user_guess == number_to_guess:
                has_won = True
                break
            else:
                difference = abs(user_guess - number_to_guess)
                if difference <= 2:
                    print(f"Your {GREEN}close{WHITE}!")

            if user_guess < number_to_guess:
                print(f"{BRIGHT_CYAN}Higher{WHITE}")
            else:
                print(f"{RED}Lower{WHITE}")

    if has_won:
        show_weather(user_city, temperature, True)
    else:
        show_weather(user_city, temperature, False)


def get_city():
    print_logo()

    user_city = input("Enter a city to get the weather: ")

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={KEY}&units=metric")
    data = response.json()

    value_main = data["main"]
    temperature = value_main["temp"]
    ask_user = input(f"Do you want to {BRIGHT_BLUE}guess{WHITE}? or be shown the weather. ({GREEN}Y{WHITE}/{BRIGHT_RED}N{WHITE}): ").lower()

    match ask_user:
        case "y":
            guess_game(user_city, temperature)
        case "n":
            show_weather(user_city, temperature, False)