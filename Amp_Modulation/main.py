import numpy as np
import matplotlib.pyplot as plt

# Parameters
duration = 1.0  # Signal duration in seconds
sampling_freq = 500  # Sampling frequency in Hz
carrier_freq = 35  # Carrier frequency in Hz
modulating_freq = 3.5  # Modulating frequency in Hz
amplitude = 6.0  # Amplitude of the carrier signal
modulation_index = 0.9  # Modulation index (change this to see the effect)

# Time values
t = np.linspace(0, duration, int(sampling_freq * duration), endpoint=False)

# Generate the carrier signal
carrier_signal = np.sin(2 * np.pi * carrier_freq * t)

# Generate the modulating signal
modulating_signal = np.sin(2 * np.pi * modulating_freq * t)

# Calculate the AM signal
am_signal = amplitude * (1 + modulation_index * modulating_signal) * carrier_signal

n = len(am_signal)

# Calculate the frequency spectrum using a Fourier series
frequency = np.fft.fftfreq(n, 1 / sampling_freq)

spectrum = np.zeros_like(frequency, dtype=complex)

# Calculate Fourier series coefficients
for k in range(n):
    spectrum[k] = np.sum(am_signal * np.exp(-1j * 2 * np.pi * k * np.arange(n) / n))

# Calculate the amplitude of each frequency component
spectrum_amplitude = np.abs(spectrum) / n

# Calculate the spectrum using FFT algorithm
# spectrum = np.fft.fft(am_signal)

# Plot the AM signal and its spectrum
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, am_signal, label="AM Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(frequency, spectrum_amplitude, label="Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
