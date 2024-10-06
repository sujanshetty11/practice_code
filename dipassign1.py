import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Function to convert RGB image to grayscale without inbuilt functions
def rgb_to_grayscale(image):
    height, width = image.shape[0], image.shape[1]
    grayscale_image = np.zeros((height, width), dtype=np.uint8)
    
    # Apply grayscale formula manually
    for i in range(height):
        for j in range(width):
            r, g, b = image[i, j]
            gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            grayscale_image[i, j] = gray
    
    return grayscale_image

# Function to apply 2x2 filter manually
def apply_filter(image, filter_size):
    height, width = image.shape
    filtered_image = np.zeros((height, width), dtype=np.uint8)

    # Iterate over the image (excluding the border for simplicity)
    for i in range(filter_size // 2, height - filter_size // 2):
        for j in range(filter_size // 2, width - filter_size // 2):
            total_sum = 0
            # Apply the filter (summing the neighboring pixels)
            for k in range(-filter_size // 2, filter_size // 2 + 1):
                for l in range(-filter_size // 2, filter_size // 2 + 1):
                    total_sum += image[i + k, j + l]
            # Calculate the average
            filtered_image[i, j] = total_sum // (filter_size * filter_size)

    return filtered_image

# Load an image (adjust path to your HD image)
image = np.array(Image.open('images.jpg'))

# Convert the RGB image to grayscale
gray_image = rgb_to_grayscale(image)

# Apply 2x2 and 3x3 filters on the grayscale image
gray_filtered_2x2 = apply_filter(gray_image, 2)
gray_filtered_3x3 = apply_filter(gray_image, 3)

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.title("Grayscale Image")
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("2x2 Filter Grayscale")
plt.imshow(gray_filtered_2x2, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("3x3 Filter Grayscale")
plt.imshow(gray_filtered_3x3, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
