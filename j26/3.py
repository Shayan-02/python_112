import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Signal settings
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1-second time array
f1, f2, f3 = 50, 150, 250  # Frequencies of input signal components
signal_input = (
    0.5 * np.sin(2 * np.pi * f1 * t)
    + 1.0 * np.sin(2 * np.pi * f2 * t)
    + 0.3 * np.sin(2 * np.pi * f3 * t)
)

# Design Butterworth band-pass filter
lowcut = 100  # Low cutoff frequency
highcut = 200  # High cutoff frequency
order = 4  # Filter order
nyq = 0.5 * fs  # Nyquist frequency
low = lowcut / nyq
high = highcut / nyq
b, a = signal.butter(order, [low, high], btype="band")

# Apply filter to the signal
signal_filtered = signal.filtfilt(b, a, signal_input)

# Calculate filter's frequency response
w, h = signal.freqz(b, a, worN=512)
frequencies = w * fs / (2 * np.pi)

# Plot results
plt.figure(figsize=(12, 8))

# Plot original signal
plt.subplot(3, 1, 1)
plt.plot(t, signal_input, "b-", label="Original Signal")
plt.title("Input Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Plot filter frequency response
plt.subplot(3, 1, 2)
plt.plot(frequencies, 20 * np.log10(np.abs(h)), "r-", label="Frequency Response")
plt.title("Band-pass Filter Frequency Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dB)")
plt.grid(True)
plt.legend()

# Plot filtered signal
plt.subplot(3, 1, 3)
plt.plot(t, signal_filtered, "g-", label="Filtered Signal")
plt.title("Filtered Output Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("bandpass_filter_result.png")
plt.show()
