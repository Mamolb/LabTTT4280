import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate



# Generer eksempelsignaler
fs = 44100  # Samplingsfrekvens
t = np.arange(0, 1.0, 1/fs)
signal1 = np.sin(2 * np.pi * 5 * t)  # 5 Hz sinusbølge
signal2 = np.roll(signal1, 100)  # Forsinker signal1 med 100 sampler
signal3 = np.roll(signal1, 200)  # Forsinker signal1 med 200 sampler

# Beregn krysskorrelasjoner
corr12 = correlate(signal1, signal2, mode='full')
corr13 = correlate(signal1, signal3, mode='full')
corr23 = correlate(signal2, signal3, mode='full')

# Finn tidsforsinkelsen fra toppen av krysskorrelasjonen
lag12 = np.argmax(corr12) - (len(signal1) - 1)
lag13 = np.argmax(corr13) - (len(signal1) - 1)
lag23 = np.argmax(corr23) - (len(signal2) - 1)

# Visualiser krysskorrelasjonssignalene
lags = np.arange(-len(signal1) + 1, len(signal1))
plt.figure(figsize=(14, 4))
plt.plot(lags, corr12, label='Krysskorrelasjon mellom Signal 1 og 2')
plt.plot(lags, corr13, label='Krysskorrelasjon mellom Signal 1 og 3')
plt.plot(lags, corr23, label='Krysskorrelasjon mellom Signal 2 og 3')
plt.legend()
plt.xlabel('Forsinkelse (sampler)')
plt.ylabel('Krysskorrelasjon')
plt.title('Krysskorrelasjon mellom signaler')
plt.grid(True)
plt.show()

print(f'Tidsforsinkelse mellom Signal 1 og 2: {lag12} sampler')
print(f'Tidsforsinkelse mellom Signal 1 og 3: {lag13} sampler')
print(f'Tidsforsinkelse mellom Signal 2 og 3: {lag23} sampler')

# Beregn vinkelestimatet
vinkel = -np.arctan(np.sqrt(3)(lag12-lag13)/(lag12-lag13+2*lag23))
print(f'Vinkel: {vinkel} radianer')