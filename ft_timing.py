#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
"""
Compare Fourier Transform Implementations
PHYS 4840 - Minimal benchmarking
"""

import numpy as np
import time
import matplotlib.pyplot as plt
import fourier_transform as ft

def compare_speeds():
    sizes = [2,4,6,8,16, 32, 64, 128, 256, 512, 1024]
    times_dft = []
    times_radix2 = []
    times_bluestein = []
    times_zeropad = []
    times_numpy = []


    for N in sizes:
        x = np.random.rand(N)

        # Naive DFT
        try:
            start = time.time()
            ft.dft(x)
            end = time.time()
            times_dft.append(end - start)
        except Exception as e:
            times_dft.append(np.nan)

        # Radix-2 FFT (only works for powers of 2)
        try:
            start = time.time()
            ft.fft_radix2(x)
            end = time.time()
            times_radix2.append(end - start)
        except Exception:
            times_radix2.append(np.nan)

        # Bluestein FFT (for any size)
        try:
            start = time.time()
            ft.fft_bluestein(x)
            end = time.time()
            times_bluestein.append(end - start)
        except Exception:
            times_bluestein.append(np.nan)

        # Zero-padded FFT (next power of 2)
        try:
            start = time.time()
            ft.fft_zeropad(x)
            end = time.time()
            times_zeropad.append(end - start)
        except Exception:
            times_zeropad.append(np.nan)

        # Numpy FFT
        try:
            start = time.time()
            np.fft.fft(x)
            end = time.time()
            times_numpy.append(end - start)
        except Exception:
            times_numpy.append(np.nan)

    # Plot the timing results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_dft, label="Naive DFT", marker='o')
    plt.plot(sizes, times_radix2, label="Radix-2 FFT", marker='o')
    plt.plot(sizes, times_bluestein, label="Bluestein FFT", marker='o')
    plt.plot(sizes, times_zeropad, label="Zero-padded FFT", marker='o')
    plt.plot(sizes, times_numpy, label="NumPy FFT", marker='o')

    plt.xlabel("Signal size (N)")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time of Fourier Transform Methods")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    compare_speeds()