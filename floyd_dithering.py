from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def floyd_steinberg_dithering(image_path, output_path):
    # Load the image
    input_image = Image.open(image_path).convert('L')  # Convert to grayscale
    width, height = input_image.size

    # Convert the image to a NumPy array
    input_array = np.array(input_image)

    for y in range(height - 1):
        for x in range(1, width - 1):
            old_pixel_value = input_array[y, x]

            # Quantize the pixel
            new_pixel_value = 255 if old_pixel_value > 128 else 0
            input_array[y, x] = new_pixel_value

            # Calculate the error
            error = old_pixel_value - new_pixel_value

            # Distribute the error to neighboring pixels
            input_array[y, x + 1] += error * 7 / 16
            input_array[y + 1, x - 1] += error * 3 / 16
            input_array[y + 1, x] += error * 5 / 16
            input_array[y + 1, x + 1] += error * 1 / 16

    # Save the dithered image
    dithered_image = Image.fromarray(input_array)
    dithered_image.save(output_path)

    # Display the original and dithered images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(input_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Dithered Image (Floyd-Steinberg)")
    plt.imshow(dithered_image, cmap='gray')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    input_path = "input/flower.png"  # Replace with the path to your input image
    output_path = "output/floyd_dithered_image.png"  # Replace with the desired output path

    floyd_steinberg_dithering(input_path, output_path)
