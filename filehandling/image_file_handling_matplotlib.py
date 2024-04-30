import matplotlib.pyplot as plt  # Import matplotlib for plotting
import matplotlib.image as mpimg  # Import matplotlib's image module

def display_red_channel(image_path):
    """
    Display the red channel of an image.

    Parameters:
    - image_path (str): Path to the image file.
    """
    # Load the image using matplotlib's imread function
    img = mpimg.imread(image_path)

    # Slice only the red channel values (channel 0)
    red_channel = img[:,:,0]

    # Display the shape of the red channel array
    print("Red Channel Shape:", red_channel.shape)

    # Display the red channel as a grayscale image
    plt.imshow(red_channel, cmap='gray')  # Plotting the red channel as a grayscale image
    plt.title('Red Channel')  # Adding a title to the image
    plt.axis('off')  # Turning off axis
    plt.show()  # Display the image

if __name__ == "__main__":
    # Specify the path to the image
    image_path = 'Faizan.jpg'
    display_red_channel(image_path)  # Call the function to display the red channel
