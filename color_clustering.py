import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def simplify_image(image_path, output_path, num_colors=8):
    # Load the image
    img = Image.open(image_path)

    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Reshape the array to a 2D array of pixels (height * width, RGB channels)
    pixels = img_array.reshape((-1, 3))

    # Use KMeans clustering to find the dominant colors
    kmeans = KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(pixels)

    # Replace each pixel with its cluster center
    simplified_pixels = kmeans.cluster_centers_[kmeans.labels_].astype(np.uint8)

    # Reshape the array back to the original image shape
    simplified_img_array = simplified_pixels.reshape(img_array.shape)

    # Create a simplified image from the array
    simplified_img = Image.fromarray(simplified_img_array)

    # Save the simplified image
    simplified_img.save(output_path)

    # Display the original and simplified images
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(img)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title(f"Simplified Image ({num_colors} colors)")
    plt.imshow(simplified_img)
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    input_path = "flower.png"  # Replace with the path to your input image
    output_path = "output_simplified_image.png"  # Replace with the desired output path
    num_colors = 8  # You can adjust the number of colors

    simplify_image(input_path, output_path, num_colors)
