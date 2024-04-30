import matplotlib.pyplot as plt  # Import matplotlib for plotting
import numpy as np  # Import numpy for numerical operations
import wave  # Import wave module for reading WAV files

# Open the WAV file in read mode using a context manager
with wave.open("audio.wav", "r") as spf:
    # Extract Raw Audio from WAV File
    signal = spf.readframes(-1)  # Read all frames from the WAV file
    signal = np.frombuffer(signal, dtype=np.int16)  # Convert raw audio data to a NumPy array of 16-bit integers

    # Plot the waveform
    plt.figure(1)  # Create a new figure with the number 1
    plt.title("Signal Waveform")  # Set the title of the plot
    plt.plot(signal)  # Plot the signal
    plt.show()  # Display the plot
