#Forbredelse oppgave Lab 2 

#5.1
#Her har vi da grunnideen for å finne en tidsforskyving mellom to signaler: beregn rxy(l), og finn for
#hvilken verdi på l som |rxy(l)| har et maksimum! Tidsforsinkelsen gis da av ∆t = l/fs, hvor fs er
#samplingsfrekvensen.

#Example code to find the time delay between two signals
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

def find_delay(signal1, signal2, fs):
    # Beregn krysskorrelasjonen mellom signal1 og signal2
    correlation = correlate(signal1, signal2, mode='full')
    
    # Finn indeksen til maksimalverdien i den absolutte krysskorrelasjonen
    lag = np.argmax(np.abs(correlation)) - (len(signal1) - 1)
    
    # Beregn forsinkelsen i sekunder
    delay = lag / fs
    
    return delay

# Eksempel på bruk
fs = 44100  # Samplingsfrekvens i Hz
signal1 = np.random.randn(fs)  # Et eksempel signal1
signal2 = np.roll(signal1, 100)  # Et eksempel signal2 forsinket med 100 samples

delay = find_delay(signal1, signal2, fs)
print(f'Effektiv forsinkelse: {delay} sekunder')
