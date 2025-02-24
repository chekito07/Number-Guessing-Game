import random
from game import welcome_message, game_difficulty, game_round, difficulty_option


while True:
    print(welcome_message)
    number_to_guess = random.randint(1, 100)

    user_choice = input("Enter your choice: ")

    if user_choice in difficulty_option:
        choice = game_difficulty(user_choice)
        print(f"Great! You have selected the {choice} difficulty level.\nLet's start the game!")

        if user_choice == difficulty_option[0]:
            game_round(10, number_to_guess, choice)

        elif user_choice == difficulty_option[1]:
            game_round(5, number_to_guess, choice)

        else:
            game_round(3, number_to_guess, choice)

    else:
        print("Invalide choice ! Try again...")
        print("*" * 60)
        continue

    play_round = input("Play again? o/n: ")
    if play_round == "o".lower():
        continue
    else:
        break
