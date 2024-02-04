import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_difference_of_gaussians(image, sigma1, sigma2):
    # Apply Gaussian blur with sigma1
    gaussian1 = cv2.GaussianBlur(image, (0, 0), sigma1)
    # Apply Gaussian blur with sigma2
    gaussian2 = cv2.GaussianBlur(image, (0, 0), sigma2)
    # Compute the difference of the two blurred images
    difference_of_gaussians = cv2.absdiff(gaussian1, gaussian2)
    return difference_of_gaussians

# Example usage
# Assuming 'input_image' is your grayscale image represented as a NumPy array
input_image = cv2.imread('path/to/your/image.jpg', cv2.IMREAD_GRAYSCALE)

# Set the values of sigma for the two Gaussian filters
sigma1 = 1.5
sigma2 = 3.0

# Apply the Difference of Gaussians
result_image = apply_difference_of_gaussians(input_image, sigma1, sigma2)

# Display the original and edge-detected images
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(result_image, cmap='gray')
plt.title('Edge Detection (Difference of Gaussians)')

plt.show()
