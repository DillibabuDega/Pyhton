import numpy as np
import matplotlib.pyplot as plt

def discrete_signal(n):
    return np.sin(2 * np.pi * 0.1 * n)  # Example: a sine wave with frequency 0.1

def dtft(X, N):
    omega = np.linspace(-np.pi, np.pi, N)
    X_dtft = np.zeros(N, dtype=complex)
    for k in range(N):
        X_dtft[k] = np.sum(X * np.exp(-1j * omega[k] * np.arange(len(X))))
    return omega, X_dtft
N = 50 
M = 512
n = np.arange(N)
x = discrete_signal(n)
omega, X_dtft = dtft(x, M)

plt.figure(figsize=(10, 6))
plt.plot(omega, np.abs(X_dtft), label='Magnitude Spectrum')
plt.title('Magnitude Spectrum of DTFT')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(omega, np.angle(X_dtft), label='Phase Spectrum', color='r')
plt.title('Phase Spectrum of DTFT')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (radians)')
plt.grid(True)
plt.legend()
plt.show()
