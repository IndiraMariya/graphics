import cv2
import numpy as np
from PIL import Image

# Function to create a negative image
def create_negative_image(img):
    img_array = np.array(img)
    negative_img_array = 255 - img_array
    negative_img = Image.fromarray(negative_img_array)
    return negative_img

# Function to convert an image to ASCII
def image_to_ascii(img, width, density):
    orig_width, orig_height = img.size
    r = orig_height / orig_width
    height = int(width * r * 0.5)
    img = img.resize((width, height), Image.LANCZOS)

    arr = np.array(img)
    for i in range(height):
        for j in range(width):
            p = arr[i, j]
            k = int(np.floor(p / 256 * len(density)))
            print(density[len(density) - 1 - k], end='')
        print()

# Contrast on a scale -10 -> 10
contrast = 10
density = (' .-:=+%*@#')  # Adjust this according to your preference
density = density[:-11 + contrast]

# Video input
video_path = 'ascii/chi.mov'

cap = cv2.VideoCapture(video_path)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(gray_frame)

    # Optional: Create a negative image
    img = create_negative_image(img)

    # Convert the image to ASCII and display
    image_to_ascii(img, width=200, density=density)

    # Add a delay (in milliseconds) between frames
    cv2.waitKey(30)

cap.release()
cv2.destroyAllWindows()

