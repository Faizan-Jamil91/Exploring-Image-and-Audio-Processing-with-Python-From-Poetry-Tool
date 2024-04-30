# Import necessary libraries
import numpy as np  # For numerical operations
from PIL import Image  # For image loading and manipulation
import matplotlib.pyplot as plt  # For image display

# Load the image using PIL (Python Imaging Library) and convert it to grayscale
img = np.array(Image.open('Faizan.jpg').convert("L"))

# Display the grayscale image using matplotlib
plt.imshow(img, cmap='gray')  # Specify the colormap for grayscale
plt.show()  # Show the image
