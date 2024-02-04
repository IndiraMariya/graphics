import numpy as np
import matplotlib.pyplot as plt

def ordered_dithering(input_image, n, threshold_value):
    height, width = input_image.shape
    output_image = np.zeros((height, width), dtype=np.uint8)

    # Create Bayer matrix
    bayer_matrix = create_bayer_matrix(n)

    # Loop through each pixel in the input image
    for y in range(height):
        for x in range(width):
            # Get the grayscale intensity of the current pixel
            orig_color = input_image[y, x]

            # Calculate the Bayer matrix value for the current pixel
            bayer_value = bayer_matrix[y % n, x % n]

            # Calculate the offset color
            offset_color = orig_color + threshold_value * bayer_value

            # Choose the final output color based on the threshold
            output_color = 0 if offset_color < threshold_value else 255

            # Set the output color for the corresponding pixel in the output image
            output_image[y, x] = output_color

    return output_image

def create_bayer_matrix(n):
    if n == 1:
        return np.array([[0.0]])

    smaller_matrix = create_bayer_matrix(n // 2)
    upper_left = (smaller_matrix + 0.5) / n
    upper_right = smaller_matrix / n
    lower_left = (smaller_matrix + 1.5) / n
    lower_right = (smaller_matrix + 1.0) / n

    return np.block([[upper_left, upper_right], [lower_left, lower_right]])

# Example usage
# Assuming 'input_image' is your grayscale image represented as a NumPy array
input_image = np.random.randint(0, 256, size=(128, 128), dtype=np.uint8)
n_value = 4
threshold_value = 128

output_image = ordered_dithering(input_image, n_value, threshold_value)

# Display the images
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray', vmin=0, vmax=255)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(output_image, cmap='gray', vmin=0, vmax=255)
plt.title('Dithered Image')

plt.show()

