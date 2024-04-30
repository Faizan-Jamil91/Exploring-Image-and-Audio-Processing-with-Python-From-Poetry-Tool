import matplotlib.pyplot as plt  # Import matplotlib for plotting
import numpy as np  # Import numpy for numerical operations
import wave  # Import wave module for reading WAV files

def plot_waveform(file_path):
    """
    Function to plot the waveform of a WAV file.

    Parameters:
    - file_path (str): Path to the WAV file.
    """
    # Open the WAV file
    with wave.open(file_path, "r") as spf:
        # Extract Raw Audio from WAV File
        signal = spf.readframes(-1)  # Read all frames from the WAV file
        signal = np.frombuffer(signal, dtype=np.int16)  # Convert raw audio data to a NumPy array of 16-bit integers

        # Plot the waveform
        plt.figure(1)  # Create a new figure
        plt.title("Signal Waveform")  # Set the title of the plot
        plt.plot(signal)  # Plot the signal
        plt.xlabel("Sample")  # Set the label for the x-axis
        plt.ylabel("Amplitude")  # Set the label for the y-axis
        plt.show()  # Display the plot

if __name__ == "__main__":
    # Provide the path to your WAV file
    file_path = "audio.wav"
    plot_waveform(file_path)
