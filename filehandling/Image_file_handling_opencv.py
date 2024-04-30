import cv2  # Import OpenCV for image processing
import matplotlib.pyplot as plt  # Import matplotlib for plotting

def display_image(image_path):
    """
    Display an image using OpenCV and Matplotlib.

    Parameters:
    - image_path (str): Path to the image file.
    """
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    # Convert color channels from BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display the image using matplotlib
    plt.imshow(img_rgb)  # Plotting the image
    plt.title('Faizan Image')  # Adding a title to the image
    plt.axis('off')  # Turning off axis
    plt.show()  # Display the image

if __name__ == "__main__":
    # Specify the path to the image
    image_path = 'Faizan.jpg'
    display_image(image_path)  # Call the function to display the image
