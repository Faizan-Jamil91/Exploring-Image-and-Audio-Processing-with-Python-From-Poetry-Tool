import numpy as np  # Import numpy for numerical operations
from PIL import Image  # Import Image module from PIL for image processing
import matplotlib.pyplot as plt  # Import matplotlib for image display

def display_image(image_path):
    """
    Display an image using PIL and matplotlib.

    Parameters:
    - image_path (str): Path to the image file.
    """
    # Open the image using PIL and convert it to a NumPy array
    img = np.array(Image.open(image_path))

    # Display the image using matplotlib
    plt.imshow(img)  # Plotting the image
    plt.show()  # Display the image

if __name__ == "__main__":
    # Specify the path to the image
    image_path = 'Faizan.jpg'
    display_image(image_path)  # Call the function to display the image
