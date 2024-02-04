import cv2
import numpy as np

def higher_tone_quantization(image, target_bit_depth):
    # Ensure the image is in grayscale
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Original bit depth
    original_bit_depth = image.dtype.itemsize * 8

    # Check if the target bit depth is greater than the original bit depth
    if target_bit_depth <= original_bit_depth:
        print("Target bit depth should be greater than the original bit depth.")
        return None

    # Calculate the number of intensity levels in the target bit depth
    target_levels = 2**target_bit_depth - 1

    # Perform linear scaling to the target bit depth
    scaled_image = (image.astype(np.float32) / 2**(original_bit_depth - 1)) * target_levels
    scaled_image = np.clip(np.round(scaled_image), 0, target_levels).astype(np.uint8)

    return scaled_image

if __name__ == "__main__":
    image = cv2.imread('path/to/your/bw.png', cv2.IMREAD_GRAYSCALE)

    # Set the target bit depth (e.g., 16-bit)
    target_bit_depth = 16

    # Apply higher tone quantization
    quantized_image = higher_tone_quantization(image, target_bit_depth)

    # Display the original and quantized images
    cv2.imshow('Original Image', image)
    cv2.imshow(f'Quantized Image ({target_bit_depth}-bit)', quantized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
