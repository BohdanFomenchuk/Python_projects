import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Задані параметри
amplitude_carrier = 6
frequency_carrier = 35
frequency_modulating = 3.5
frequency_deviation = 1.65

# Часовий діапазон
t = np.linspace(0, 1, 1000, endpoint=False)

# 1. Отримання аналітичного виразу для ЧМ сигналу та побудова графіку
modulated_signal = amplitude_carrier * np.cos(2 * np.pi * frequency_carrier * t +
                                              frequency_deviation * np.sin(2 * np.pi * frequency_modulating * t))

plt.figure(figsize=(10, 4))
plt.plot(t, modulated_signal, label='ЧМ сигнал')
plt.title('ЧМ сигнал в часовій області')
plt.xlabel('Час')
plt.ylabel('Амплітуда')
plt.legend()
plt.show()

# 2. Побудова амплітудного спектру ЧМ сигналу
N = len(t)
signal_fft = fft(modulated_signal)
freq = fftfreq(N, t[1] - t[0])

plt.figure(figsize=(10, 4))
plt.plot(freq, np.abs(signal_fft))
plt.title('Амплітудний спектр ЧМ сигналу')
plt.xlabel('Частота')
plt.ylabel('Амплітуда')
plt.grid(True)
plt.show()

# 3. Визначення практичної ширини спектру ЧМ сигналу
# Для ЧМ сигналу практична ширина спектру зазвичай визначається девіацією частоти
practical_bandwidth = 2 * frequency_deviation
print(f'Практична ширина спектру ЧМ сигналу: {practical_bandwidth} Гц')