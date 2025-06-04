import numpy as np
import matplotlib.pyplot as plt

# Signal settings
fs = 10000  # High sampling frequency for continuous-time approximation (Hz)
t = np.linspace(-1, 1, fs, endpoint=False)  # Time array (-1 to 1 seconds)
dt = t[1] - t[0]  # Time step

# Signal 1: Rectangular pulse
width1 = 0.2  # Pulse width
signal1 = np.where((t >= -width1 / 2) & (t <= width1 / 2), 1.0, 0.0)

# Signal 2: Triangular pulse
width2 = 0.4  # Triangle width
signal2 = np.where(
    (t >= -width2 / 2) & (t <= width2 / 2), 1 - np.abs(t) / (width2 / 2), 0.0
)

# Compute convolution
conv_result = np.convolve(signal1, signal2, mode="same") * dt

# Plot results
plt.figure(figsize=(12, 8))

# Plot Signal 1
plt.subplot(3, 1, 1)
plt.plot(t, signal1, "b-", label="Rectangular Pulse")
plt.title("Signal 1: Rectangular Pulse")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Plot Signal 2
plt.subplot(3, 1, 2)
plt.plot(t, signal2, "r-", label="Triangular Pulse")
plt.title("Signal 2: Triangular Pulse")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Plot Convolution
plt.subplot(3, 1, 3)
plt.plot(t, conv_result, "g-", label="Convolution")
plt.title("Convolution of Signals")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("continuous_convolution_result.png")
plt.show()
