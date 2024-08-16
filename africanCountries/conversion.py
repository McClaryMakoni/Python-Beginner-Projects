from PIL import Image

# Open the image file
img = Image.open("countries.jpg")

# Convert the image to GIF format
img.save("countries.gif")