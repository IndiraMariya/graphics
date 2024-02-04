from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import imageio
from skimage import color

def bayer_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    level = 256 // (size * size)

    for i in range(size):
        for j in range(size):
            matrix[i][j] = (i * size + j) * level

    return matrix

def bayer_dithering(image_path, output_path, matrix_size):
    input_image = Image.open(image_path)
    width, height = input_image.size

    bayer_matrix_values = bayer_matrix(matrix_size)

    for y in range(height):
        for x in range(width):
            pixel_value = input_image.getpixel((x, y))

            # Apply Bayer dithering independently to each color channel
            new_pixel_value = tuple(
                255 if channel_value > bayer_matrix_values[x % matrix_size][y % matrix_size] else 0
                for channel_value in pixel_value
            )

            input_image.putpixel((x, y), new_pixel_value)

    input_image.save(output_path)

if __name__ == "__main__":
    input_path = "input/cat.png"  # Replace with the path to your input image
    matrix_size = 2  # You can adjust the matrix size for different dithering patterns

    input_image = imageio.imread(input_path)
    height, width, channels = input_image.shape
    bayer_matrix_values = bayer_matrix(matrix_size)

    output_image = np.zeros_like(input_image, dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            pixel_value = input_image[y, x]

            # Apply Bayer dithering independently to each color channel
            new_pixel_value = tuple(
                255 if channel_value > bayer_matrix_values[x % matrix_size][y % matrix_size] else 0
                for channel_value in pixel_value
            )

            output_image[y, x] = new_pixel_value

    output_path = "output/bayer_dithered_image.png"
    imageio.imwrite(output_path, output_image)

    plt.imshow(output_image)
    plt.axis('off')
    plt.show()
