from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Define the ImageDataGenerator for preprocessing
training_datagen = ImageDataGenerator(rescale=1.0/255)  # Rescale pixel values to [0, 1]

# Path to the directory containing training images
training_dir = 'training'

# Generate batches of tensor data from the directory
train_generator = training_datagen.flow_from_directory(
    training_dir,
    target_size=(150, 150),  # Resize images to 150x150
    batch_size=16,
    class_mode='binary'  # Because of binary classification (binary labels)
)

# Display a few examples of images and their labels
batch = train_generator.next()  # Generate a batch of data
images = batch[0]  # Extract images from the batch
labels = batch[1]  # Extract labels from the batch

plt.figure(figsize=(10, 10))
for i in range(len(images)):
    plt.subplot(4, 4, i + 1)
    plt.imshow(images[i])
    plt.title("Label: {}".format(labels[i]))
    plt.axis("off")
plt.show()
