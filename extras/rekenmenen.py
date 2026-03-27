import random
from extras import logos

FILE_LOCATION = "math_results.txt"


def math_session(operation, num_questions, minimum, maximum):
    correct_count = 0

    for _ in range(int(num_questions)):
        first = random.randint(minimum, maximum)
        second = random.randint(minimum, maximum)

        match operation:
            case "+":
                correct_answer = first + second
            case "-":
                correct_answer = first - second
            case "*":
                correct_answer = first * second
            case _:
                print("Not valid")
                continue

        user_guess = input(f"{first} {operation} {second} (or stop) =  ")

        try:
            given_answer = int(user_guess)
            if given_answer == correct_answer:
                status = "correct"
                correct_count += 1
            else:
                status = "wrong"
        except ValueError:
            given_answer = user_guess
            status = "wrong"

            if user_guess.lower() == "stop":
                break

        with open(FILE_LOCATION, "a") as text_file:
            text_file.write(f"{first};{operation};{second};{correct_answer};{given_answer};{status}\n")

    print(f"{correct_count} out of {num_questions} correct!")


def reset_data():
    with open(FILE_LOCATION, "w"):
        pass
    print("Everything has been deleted.")


def mistake_report():
    mistakes = []
    try:
        with open(FILE_LOCATION, "r") as text_file:
            for line in text_file.readlines():
                data = line.strip('\n').split(";")

                if len(data) == 6:
                    first, operation, second, correct, given, status = data

                    if status == "correct":
                        continue

                    mistakes.append(f"{first} {operation} {second} is unfortunately not {given}")
    except FileNotFoundError:
        return [f"No history found. Play a session first!"]

    return mistakes


def choices():
    logos.print_reken()
    print("1: New math session\n2: Mistake report\n3: Reset")

    try:
        user_input = input("Enter a number: ")
        if user_input.isdigit():
            chosen_number = int(user_input)

            match chosen_number:
                case 1:
                    operation = input("Operation (+,-,*): ")
                    amount = input("Choose the amount of questions (1..50): ")

                    match input("Easy or hard: ").lower().strip():
                        case choice if "e" in choice:
                            minimum, maximum = 0, 10
                        case choice if "d" in choice:
                            minimum, maximum = -10, 100
                        case _:
                            print("Invalid difficulty.")
                            return

                    math_session(operation, amount, minimum, maximum)

                case 2:
                    mistakes = mistake_report()
                    print("-" * 80)
                    for mistake in mistakes:
                        print(mistake)
                    print("-" * 80)

                case 3:
                    user_confirmation = input("Are you sure you want to delete the file? (yes/no): ").lower().strip()

                    if user_confirmation in ["yes", "y"]:
                        reset_data()
                    else:
                        exit()

                case _:
                    print("Out of bounds\n")

        else:
            print("Enter a valid number\n")

    except ValueError:
        print("Enter a number!")