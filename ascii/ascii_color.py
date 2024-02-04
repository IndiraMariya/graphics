import sys
import numpy as np
from PIL import Image
from colored import stylize, fg, rgb_to_ansi

# Make image into negative
def create_negative_image(img):
    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Calculate the negative image
    negative_img_array = 255 - img_array

    # Convert the NumPy array back to a PIL Image
    negative_img = Image.fromarray(negative_img_array)

    # Return the negative image
    return negative_img

# Contrast on a scale -10 -> 10
contrast = 10
density = (' .-=+:%@#')
density = density[:-11+contrast]
n = len(density)

img_name = sys.argv[1]
try:
    width = int(sys.argv[2])
except IndexError:
    # Default ASCII image width.
    width = 200

# Read in the image, convert to greyscale.
img = Image.open(img_name)
img = img.convert('RGB')
img = create_negative_image(img)

# Resize the image as required.
orig_width, orig_height = img.size
r = orig_height / orig_width

# The ASCII character glyphs are taller than they are wide. Maintain the aspect
# ratio by reducing the image height.
height = int(width * r * 0.5)
img = img.resize((width, height), Image.LANCZOS)

# Now map the pixel brightness to the ASCII density glyphs.
arr = np.array(img)
for i in range(height):
    for j in range(width):
        r, g, b = arr[i, j]
        brightness = (r + g + b) / 3
        k = int(np.floor(brightness / 256 * n))
        # Choose a color based on the pixel value
        color = rgb_to_ansi(r, g, b)
        # Print the colored ASCII art
        print(stylize(density[n - 1 - k], fg(color)), end='')
    print()
