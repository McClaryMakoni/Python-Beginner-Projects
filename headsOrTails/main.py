import random

print("Hello, world")

sample_space = ['h', 't']
player_name = input("What is your name?")
game_on = True
while game_on:

    # Get user input for heads or tails, converting it to lowercase and stripping extra spaces
    user_guess = input('Heads(H) or Tails(T)').lower().strip()

    # Map the full word 'heads' or 'tails' to 'h' or 't'
    if user_guess == 'heads':
        user_guess = 'h'
    elif user_guess == 'tails':
        user_guess = "t"

    # Randomly select either 'h' (heads) or 't' (tails) to simulate a coin flip
    computer_choice = random.choice(sample_space)
    print(f'Flip result:{computer_choice}')
    print(f'{player_name}\'s Answer: {user_guess} ')

    # Check if the user's input is valid and process the game logic
    if user_guess in sample_space:
        if user_guess == computer_choice:
            print('You Win'.upper())
        else:
            print('Ouch, it\'s the opposite.')

        # Ask if the user wants to play again
        proceed_ = input('Would you like to play again?').lower()
        if proceed_ == "yes":
            game_on = True
        elif proceed_ == 'no':
            print("Thank You For Playing")
            game_on = False
        else:
            game_on = True  # Default to continuing the game if input is unclear
    else:
        # Notify user of invalid input and prompt for a valid one in the next iteration
        print('Enter a valid input(h or t)'.upper())
        game_on = True
