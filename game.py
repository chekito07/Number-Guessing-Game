import json
import time

welcome_message = f"""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
"""

difficulty_option = ["1", "2", "3"]


def game_difficulty(user_input):
    difficulty = ""
    if user_input == difficulty_option[0]:
        difficulty = "Easy"

    if user_input == difficulty_option[1]:
        difficulty = "Medium"

    if user_input == difficulty_option[2]:
        difficulty = "Hard"

    return difficulty


def game_round(nb_chance, nb_to_guess, level_choice, counter=0):
    user_guess = ""
    start_timer = time.perf_counter()

    for i in range(1, nb_chance + 1):
        user_guess = input("Enter your guess: ")
        counter += 1

        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess == nb_to_guess:
                break
            elif user_guess > nb_to_guess:
                print(f"Incorrect! The number is less than {user_guess}.")

            else:
                print(f"Incorrect! The number is greater than {user_guess}.")
        else:
            print("Invalide input! Enter a number please")

        if counter != nb_chance:
            print(f"Remaining attempt: {nb_chance - counter}")

        print("*" * 60)
        print()

    end_timer = time.perf_counter()
    seconds = int((end_timer - start_timer) % 60)
    minutes = int((end_timer - start_timer) / 60) % 60
    hours = int((end_timer - start_timer) / 3600)
    round_time = f'{hours:02}:{minutes:02}:{seconds:02}'

    if user_guess == nb_to_guess:
        print(f"Congratulations! You guessed the correct number in {counter} attempts.")
        save_game(level_choice, nb_to_guess, counter, round_time)

    else:
        print(f"You loose ! The number to guess was {nb_to_guess}")

    print("The round took:", round_time)


def save_game(level, number_to_guess, attempt, round_time):
    with open("records.json", encoding="utf8") as f:
        content = json.load(f)

    if level in content:
        if content[level]["attempt"] > attempt:
            content.update({
                level: {
                    "level": level,
                    "number_to_guess": number_to_guess,
                    "attempt": attempt,
                    "time": round_time
                }
            })
    else:
        content[level] = {
                "level": level,
                "number_to_guess": number_to_guess,
                "attempt": attempt,
                "time": round_time
            }

    with open("records.json", "w", encoding="utf8") as f:
        json.dump(content, f, indent=4)
