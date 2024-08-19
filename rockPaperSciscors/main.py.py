import random

print('Welcome to Rock Paper Scissors')

trials = {
    'rock': "🧱",
    'paper': "📜",
    'scissors': "✂️"
}

# Get the corresponding key from a dictionary by its value
def get_key_by_value(dictionary: dict, the_value: str):
    for key, value in dictionary.items():
        if value == the_value:
            return key
    return None

game_is_on: bool = True

while game_is_on:
    computer_choice: str = random.choice(list(trials.values()))
    user_choice: str = input('Rock,Paper, Scissors? ').lower()

    sample_space: list = list(trials.keys())

    if user_choice in sample_space:
        print(f"Player Choice: {trials[user_choice]}")
        print('$' * 10)
        print(f'Computer Choice: {computer_choice}')
        computer_key: str = get_key_by_value(dictionary=trials, the_value=computer_choice)

        if user_choice == computer_key:
            print("It's a draw")
        elif (user_choice == "rock" and computer_key == "scissors") or \
             (user_choice == "paper" and computer_key == "rock") or \
             (user_choice == 'scissors' and computer_key == "paper"):
            print("YOU WIN")
        else:
            print("YOU LOSE")
    else:
        print("Invalid Input. Please choose 'rock', 'paper', or 'scissors'.")

    # Check if the user wants to play another round
    options = ["y", "yes", ""]
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again not in options:
        game_is_on = False

print("Thanks for playing!")
