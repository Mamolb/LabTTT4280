import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import kaiser

# Parameters
N = 512*4  # Number of sample points
T = 1.0 / 800.0  # Sample spacing
f = 50.0  # Frequency of the sine wave (Hz)

# Time array
x = np.linspace(0.0, N*T, N, endpoint=False)

# Sine wave
y = np.sin(2.0 * np.pi * f * x)

# Window functions
windows = {
    'Rectangular': np.ones(N),
    'Hamming': np.hamming(N),
    'Hann': np.hanning(N),
    'Blackman': np.blackman(N),
    'Kaiser': kaiser(N, beta=14),
}

# Prepare the FFT plot
plt.figure(figsize=(10, 6))

# Frequency axis for plotting
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# Loop through each window, apply it, and plot its FFT
for window_name, window in windows.items():
    # Apply window
    yw = y * window
    
    # FFT and normalize
    yf = fft(yw)
    yf_normalized = 2.0/N * np.abs(yf[0:N//2])
    
    # Plot
    plt.plot(xf, yf_normalized, label=f"{window_name} Window")

plt.title('FFT av en sinus med ulike vindusfunksjoner')
plt.xlabel('Frekvens (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.xlim(40, 60)  # Focus on the frequency range of interest
plt.show()
