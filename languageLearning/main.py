import random

import keyboard

from data import swahili_words  # Importing the list of Swahili words and their English translations


def learn_words(words_list: list):
    """
    A function that helps users learn Swahili words by translating them into English.
    Users input the English translation of a randomly selected Swahili word and get feedback.

    Args:
        words_list (list): A list of dictionaries containing Swahili words and their English translations.
    """
    chosen_items = set()  # Set to keep track of words that have been asked already
    score = 0  # To track the user's score
    count = 0  # To track the number of words attempted

    # to make sure session runs until all words are exhausted
    while len(chosen_items) < len(words_list):
        try:
            # Select a random word from the list that hasn't been used yet
            random_item = random.choice(words_list)
            swahili_word = random_item['Swahili']

            # Ensure the word hasn't been chosen before
            while swahili_word in chosen_items:
                random_item = random.choice(words_list)

            if swahili_word not in chosen_items:
                count += 1
                print(f"TRANSLATE: {swahili_word}")

                # Get user response
                user_response = input(f"What does the word \"{swahili_word}\" mean in English? >> ").lower().strip()
                english_translation = random_item['English']

                # Check if the English translation is correct
                if isinstance(english_translation, list):
                    if user_response in english_translation:
                        print("✅ Correct.")
                        score += 1
                    else:
                        print(f"❌ Incorrect. {swahili_word} means {english_translation}")
                else:
                    if user_response == english_translation:
                        print("✅ Correct.")
                        score += 1
                    else:
                        print(f"❌ Incorrect. {swahili_word} means {english_translation}")

                chosen_items.add(swahili_word)  # Add word to chosen_items set

                # Check if the user wants to continue
                proceed = input("Proceed? (yes/y/enter to continue) >> ").lower()
                if proceed not in ['y', 'yes', '']:
                    print("SESSION OVER")
                    chosen_items.clear()  # Clear chosen items for a new session
                    break  # Exit the loop to end the session

            # Give user an option to exit the game
            if keyboard.is_pressed("esc"):
                break
        except KeyboardInterrupt:
            print(f"\nYOU GOT {score}/{count}")
            break

    print(f"YOU GOT {score}/{count}")  # Final score display


if __name__ == "__main__":
    learn_words(words_list=swahili_words)  # Call the function with the list of Swahili words
