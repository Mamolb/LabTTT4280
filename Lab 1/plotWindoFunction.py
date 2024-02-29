import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import kaiser

# Number of sample points
N = 512

# Sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)

# Generate window functions
rectangular_window = np.ones(N)
hamming_window = np.hamming(N)
hann_window = np.hanning(N)
blackman_window = np.blackman(N)
kaiser_window = kaiser(N, beta=14)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(x, rectangular_window, label='Rectangular Window', color='blue')
plt.plot(x, hamming_window, label='Hamming Window', color='green')
plt.plot(x, hann_window, label='Hann Window', color='red')
plt.plot(x, blackman_window, label='Blackman Window', color='cyan')
plt.plot(x, kaiser_window, label='Kaiser Window', color='magenta')

plt.title('Ulike vindusfunksjoner')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.grid(True)
plt.ylim(0, 1.5)
plt.show()
