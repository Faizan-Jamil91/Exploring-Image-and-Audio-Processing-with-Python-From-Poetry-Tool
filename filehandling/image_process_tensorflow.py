from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt  # Import matplotlib for image display

img = image.load_img('Faizan.jpg', target_size=(150, 150), color_mode="rgb")
img = image.img_to_array(img)
print(img.shape)
plt.imshow(img/255)
plt.show()  # Display the image
