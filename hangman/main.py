import random

words = [
    "python", "algorithm", "hangman", "programming", "variable",
    "function", "debugging", "software", "hardware", "database",
    "developer", "interface", "framework", "module", "syntax",
    "iteration", "recursion", "exception", "compiler", "binary"
]


random_word = random.choice(words)
display_word = ["_" for l in random_word]
attempts = 7
guessed_letters = set()

while attempts > 0 and "_" in display_word:
    print(f"\n {' '.join(display_word)}")

    user_guess = input("Guess a letter you think is on the word >>:").lower().strip()
    if len(user_guess) == 1 and user_guess.isalpha():
        if user_guess not in guessed_letters:
            if user_guess in random_word:
                for index, letter in enumerate(random_word):
                    if letter == user_guess:
                        display_word[index] = letter
                        guessed_letters.add(user_guess)
            else:
                print("❌, not correct. Try again")
                attempts -= 1

        else:
            print(f"Letter {user_guess} has already been guessed. Try another one")
            attempts -= 1
    else:
        print("Not a valid input, enter a single letter.")
        attempts -= 1

if "_" not in display_word:
    print(f"Congrats, You got the word {"".join(display_word).upper()} correct.\nYOU SURVIVED")
elif attempts <= 0:
    print(f"You ran out of attempts, the word was {random_word.upper()}.REST IN PEACE.")
