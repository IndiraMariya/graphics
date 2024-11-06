from PIL import Image

def weave_images(image1_path, image2_path, output_path, strip_size=10):
    # Open the input images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    
    # Ensure both images are the same size
    if image1.size != image2.size:
        raise ValueError("Input images must be the same size.")
    
    width, height = image1.size
    
    # Create a new blank image to store the output
    output_image = Image.new("RGB", (width, height))
    
    # Loop over each strip location
    for x in range(0, width, strip_size):
        for y in range(0, height, strip_size):
            # Determine which image to use based on strip position
            if (x // strip_size + y // strip_size) % 2 == 0:
                # Use image1's strip
                strip = image1.crop((x, y, x + strip_size, y + strip_size))
            else:
                # Use image2's strip
                strip = image2.crop((x, y, x + strip_size, y + strip_size))
            
            # Paste the strip onto the output image
            output_image.paste(strip, (x, y))
    
    # Save the output image
    output_image.save(output_path)
    print(f"Weaved image saved as {output_path}")

# Example usage
weave_images("./images/img4.jpg", "./images/img1.jpg", "out3.jpg", strip_size=300)
