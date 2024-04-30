from scipy.io import wavfile  # Import the wavfile module from scipy.io

# Read the WAV file using scipy's wavfile module
rate1, dat1 = wavfile.read('audio.wav')

# Print the sample rate and data
print("Sample Rate:", rate1)  # Print the sample rate (number of samples per second)
print("Data:", dat1)  # Print the data (audio samples)
