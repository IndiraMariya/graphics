import sys
import numpy as np
from PIL import Image

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
density = ('`.-:=+%*@#')
# density = ('ME$sj1|-^` ')
# density = ('  .–~*^srteuqwyoiiyh#+)(/aAX$&%')
# density = (' .–~*^suwih#+AX$&%')
# density = ('█▓▒░  ')
# density = (' ▁ ▂ ▄ ▅ ▆ ▇ █ ▉ ▊ ▋ ▌ ▍ ▎ ▏ ▐ ░ ▒ ▓')
# density = (' .-=+:%@#')
# density = (' .''^,"`:;Il!i<>~+_--?][]{}1()|\//tfjrxnucvzXYUJCQL0OZmwqpdqbkha*#MW&8%B@$')

density = density[:-11+contrast]
n = len(density)

img_name = sys.argv[1]
try:
    width = int(sys.argv[2])
except IndexError:
    # Default ASCII image width.
    width = 75

# Read in the image, convert to greyscale.
img = Image.open(img_name)
img = img.convert('L')

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
        p = arr[i,j]
        k = int(np.floor(p/256 * n))
        print(density[n-1-k], end='')
    print('<br></br>')  # Add <br><br/> at the end of each line
