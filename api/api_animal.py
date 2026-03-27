import html
import requests
from extras import logos
from extras.colors import *

def print_logo():
    logos.print_animal_logo()

def start_api_animal(user_name):

    print_logo()
    print(f"Ready to guess {RED}{user_name}{WHITE}?")

    response = requests.get("https://opentdb.com/api.php?amount=10&category=27&type=boolean")
    data = response.json()

    questions = data.get("results", [])
    score = 0

    for item in questions:
        question_text = html.unescape(item["question"])
        correct_answer = item["correct_answer"]

        print(f"\nQuestion: {BLUE}{question_text}{WHITE}")
        user_answer = input(f"{GREEN}True{WHITE} or {RED}False{WHITE}? ").strip().lower()

        if user_answer in ["t", "true"]:
            normalized_answer = "True"
        elif user_answer in ["f", "false"]:
            normalized_answer = "False"
        else:
            print(f"{RED}Invalid choice{WHITE}")
            normalized_answer = "Invalid"

        if normalized_answer == correct_answer:
            print(f"{GREEN}Correct!{WHITE}")
            score += 1
        elif normalized_answer != "Invalid":
            print(f"{RED}Wrong!{WHITE} The answer was {correct_answer}.")

    print(f"\n{MAGENTA}Game Over! Score: {score}/{len(questions)}{WHITE}")
