import random  # Import the random module to randomly select a word from a list

# List of words that can be chosen for the Hangman game
words = [
    "python", "algorithm", "hangman", "programming", "variable",
    "function", "debugging", "software", "hardware", "database",
    "developer", "interface", "framework", "module", "syntax",
    "iteration", "recursion", "exception", "compiler", "binary"
]

# Randomly select a word from the list for the player to guess
random_word = random.choice(words)

# Create a display version of the word with underscores representing each letter
display_word = ["_" for l in random_word]

attempts = 7  # Set the number of attempts the player has to guess the word
guessed_letters = set()  # Create a set to track letters that have already been guessed

# Loop until the player either runs out of attempts or guesses the entire word
while attempts > 0 and "_" in display_word:
    print(f"\n {' '.join(display_word)}")  # Display the current state of the word

    # Prompt the player to guess a letter
    user_guess = input("Guess a letter you think is on the word >>:").lower().strip()

    # Check if the input is valid (a single alphabetic character)
    if len(user_guess) == 1 and user_guess.isalpha():
        # Check if the guessed letter has not already been guessed
        if user_guess not in guessed_letters:
            # If the guessed letter is in the word, reveal it in the display
            if user_guess in random_word:
                for index, letter in enumerate(random_word):
                    if letter == user_guess:
                        display_word[index] = letter  # Update the display word
                        guessed_letters.add(user_guess)  # Add the guessed letter to the set
            else:
                # If the guessed letter is not in the word, decrease attempts
                print("❌, not correct. Try again")
                attempts -= 1
        else:
            # If the letter has already been guessed, inform the player
            print(f"Letter {user_guess} has already been guessed. Try another one")
            attempts -= 1
    else:
        # If the input is invalid, inform the player and decrease attempts
        print("Not a valid input, enter a single letter.")
        attempts -= 1

# After the loop, check if the player has guessed the word or run out of attempts
if "_" not in display_word:
    print(f"Congrats, You got the word {"".join(display_word).upper()} correct.\nYOU SURVIVED")
elif attempts <= 0:
    print(f"You ran out of attempts, the word was {random_word.upper()}.REST IN PEACE.")
