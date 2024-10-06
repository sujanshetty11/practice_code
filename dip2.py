import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Function to compute histogram of an image (grayscale or a single channel of RGB)
def compute_histogram(image):
    height, width = image.shape
    histogram = np.zeros(256, dtype=int)  # Create an array for pixel intensities (0-255)
    
    # Loop through the image and count the intensity occurrences
    for i in range(height):
        for j in range(width):
            intensity = image[i, j]
            histogram[intensity] += 1
    
    return histogram

# Load the image (RGB) and convert to grayscale
image = np.array(Image.open('images.jpg'))

# Convert to grayscale manually
def rgb_to_grayscale(image):
    height, width = image.shape[0], image.shape[1]
    grayscale_image = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            r, g, b = image[i, j]
            gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            grayscale_image[i, j] = gray
    return grayscale_image

# Convert to grayscale
grayscale_image = rgb_to_grayscale(image)

# Compute the histogram for the grayscale image
grayscale_histogram = compute_histogram(grayscale_image)

# Plot the histogram for grayscale image
plt.figure(figsize=(10, 5))
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity (0-255)')
plt.ylabel('Frequency')
plt.bar(range(256), grayscale_histogram, color='black')
plt.show()

# For RGB Image: Compute and plot histogram for each channel (R, G, B)
def compute_rgb_histogram(image):
    height, width, _ = image.shape
    red_histogram = np.zeros(256, dtype=int)
    green_histogram = np.zeros(256, dtype=int)
    blue_histogram = np.zeros(256, dtype=int)

    # Loop through image and compute histograms for each channel
    for i in range(height):
        for j in range(width):
            r, g, b = image[i, j]
            red_histogram[r] += 1
            green_histogram[g] += 1
            blue_histogram[b] += 1

    return red_histogram, green_histogram, blue_histogram

# Compute RGB histograms
red_histogram, green_histogram, blue_histogram = compute_rgb_histogram(image)

# Plot RGB histograms
plt.figure(figsize=(15, 5))

# Red channel histogram
plt.subplot(1, 3, 1)
plt.title('Red Histogram')
plt.xlabel('Pixel Intensity (0-255)')
plt.ylabel('Frequency')
plt.bar(range(256), red_histogram, color='red')

# Green channel histogram
plt.subplot(1, 3, 2)
plt.title('Green Histogram')
plt.xlabel('Pixel Intensity (0-255)')
plt.ylabel('Frequency')
plt.bar(range(256), green_histogram, color='green')

# Blue channel histogram
plt.subplot(1, 3, 3)
plt.title('Blue Histogram')
plt.xlabel('Pixel Intensity (0-255)')
plt.ylabel('Frequency')
plt.bar(range(256), blue_histogram, color='blue')

plt.tight_layout()
plt.show()
