import numpy as np
import matplotlib.pyplot as plt

# Define Variables
# Extend frequency range up to 10,000 rad/s for Bode plot
w = np.logspace(0, np.log10(10000), 500)  # Generate frequencies up to 10,000 rad/s
L = 100*10**-3  # 100 mH
C_2 = 470*10**-6  # 470 nF
C_3 = 100e-9  # 100 nF

# Define Transfer Function
H_w = 1 / (1 - w**2 * L * (C_2 + C_3))

# Convert magnitude to dB
H_w_dB = 20 * np.log10(np.abs(H_w))

# Create a figure for subplots
plt.figure(figsize=(10, 8))

# Plot the magnitude response (non-logarithmic)
plt.subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot
plt.plot(w, np.abs(H_w))  # Linear plot for magnitude response
plt.title('Magnitude Response of the Noise Reduction Filter')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude')
plt.grid(which='both', axis='both')
plt.xlim(0, 1000)  # Limit x-axis to 1000 rad/s for magnitude response

# Plot the Bode Plot in dB
plt.subplot(2, 1, 2)  # 2 rows, 1 column, 2nd subplot
plt.semilogx(w, H_w_dB)  # Semilogx for dB scale
plt.title('Bode Plot of the Noise Reduction Filter')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude (dB)')
plt.grid(which='both', axis='both')
plt.xlim(1, 10000)  # Extend x-axis to 10,000 rad/s for Bode plot consistency

# Adjust layout for better readability
plt.tight_layout()

plt.show()
