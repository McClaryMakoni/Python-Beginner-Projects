import turtle
from coordinates import african_countries_coordinates
from tkinter import messagebox
import random
from colors import text_colors

# Set up the Turtle graphics screen
screen = turtle.Screen()
screen.title("African Countries Map Game")
screen.setup(width=800, height=600)
screen.bgpic("./countries.gif")  # Sets the map image as the background

# Set of correctly guessed countries
correct_guesses = set()


def check_guess(user_guess, words_dict):
    """
    Check if the user's guess is close to any word in the dictionary keys.

    Args:
        user_guess (str): The user's guess.
        words_dict (dict): Dictionary of correct words and their coordinates.

    Returns:
        bool: True if the guess is close to any correct word, False otherwise.
    """
    for correct_word in words_dict.keys():
        if is_close(user_guess, correct_word):
            return True
    return False


def is_close(guess, correct_word):
    """
    Determine if the guess is close to the correct word.
    A guess is considered close if more than half the letters match.

    Args:
        guess (str): The user's guess.
        correct_word (str): The correct word to compare against.

    Returns:
        bool: True if the guess is close to the correct word, False otherwise.
    """
    # Normalize to lowercase
    guess = guess.lower()
    correct_word = correct_word.lower()

    # Handle case where one or both strings are empty
    if not guess or not correct_word:
        return False

    # Calculate the number of matching letters
    matches = sum(1 for a, b in zip(guess, correct_word) if a == b)

    # Check if the guess is close enough
    return matches > len(correct_word) / 2


def check_country(guessed, countries_list):
    """
    Handle user input and place the country name on the map.

    Args:
        guessed (set): Set of correctly guessed countries.
        countries_list (dict): Dictionary of correct words and their coordinates.
    """
    while len(guessed) != len(countries_list):
        try:
            # Get the user's guess
            user_input = screen.textinput("Country Name", "Enter the name of an African country:")

            # Handle case where the user clicks cancel or closes the input box
            if user_input is None:
                break

            country = user_input.title().strip()

            # Process the user's guess
            if country == "Exit":
                messagebox.showinfo(title="Score", message=f"You got {len(guessed)}/{len(countries_list)} correct.")
                turtle.bye()
                break
            elif country in guessed:
                messagebox.showinfo(title="Already Guessed",
                                    message="You already guessed that country. Try another one.")
            elif country in countries_list:
                x, y = countries_list[country]
                place_text(country, x, y)
                guessed.add(country)
            elif check_guess(user_guess=country, words_dict=countries_list):
                messagebox.showinfo(title="Close", message="That was close, try again.")
            else:
                messagebox.showerror(title="Not Found", message="Not an African country, try again.")
        except Exception as e:
            messagebox.showerror(title="Error", message=f"An unexpected error occurred: {e}")


def place_text(country, x, y):
    """
    Place the country name on the map at specified coordinates.

    Args:
        country (str): The name of the country to display.
        x (int): The x-coordinate on the map.
        y (int): The y-coordinate on the map.
    """
    try:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)  # Adjust coordinates based on the screen size
        t.pencolor(random.choice(text_colors))
        t.write(country, align="center", font=("Arial", 9, "bold"))
    except Exception as e:
        print(f"Error placing text: {e}")


if __name__ == "__main__":
    # Start the game
    check_country(guessed=correct_guesses, countries_list=african_countries_coordinates)

    # Keep the screen open
    turtle.done()
