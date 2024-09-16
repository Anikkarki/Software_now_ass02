import time
from PIL import Image
import numpy as np

# Generate a number (n) based on the current time
n = (int(time.time()) % 100) + 50
n += 10 if n % 2 == 0 else 0  # Add 10 if the number is even
print("Generated number (n):", n)

# Open the image, modify pixels, and save the output image
image = Image.open('Chapter1.png')
image_array = np.clip(np.array(image) + n, 0, 255)  # Adjust pixels and clip values to 0-255
Image.fromarray(image_array.astype(np.uint8)).save('chapter1out.png')

# Sum all red pixel values in the new image
red_sum = np.sum(image_array[:, :, 0])  # Red channel sum
print("Sum of red pixel values:", red_sum)