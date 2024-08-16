import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Get Coordinates")
screen.setup(width=800, height=600)
screen.bgpic("countries.gif")

# Function to print the coordinates where you click
def get_coordinates(x, y):
    print(f"Clicked at: ({x}, {y})")

# Bind the click event to the function
screen.onscreenclick(get_coordinates)

# Keep the window open
turtle.done()
