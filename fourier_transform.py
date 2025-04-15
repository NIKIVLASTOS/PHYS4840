#!/usr/bin/env python3
"""
Fourier Transform Implementation
-------------------------------
A clean, pedagogical implementation of Fourier Transform for teaching purposes.
This module provides functions to compute DFT, inverse DFT, and spectral analysis.

PHYS 4840 - Mathematical and Computational Methods II
"""

import numpy as np


def dft(x):
    """
    Compute the Discrete Fourier Transform (DFT) of the input signal.
    
    Parameters:
        x (array): Input signal (time domain)
    
    Returns:
        array: Fourier Transform of x (frequency domain, complex values)
    """
    N = len(x)
    X = np.zeros(N, dtype=complex)
    
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    
    return X


def idft(X):
    """
    Compute the Inverse Discrete Fourier Transform (IDFT) of the input spectrum.
    
    Parameters:
        X (array): Input spectrum (frequency domain)
    
    Returns:
        array: Inverse Fourier Transform of X (time domain)
    """
    N = len(X)
    x = np.zeros(N, dtype=complex)
    
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
    
    # Normalize by N
    x = x / N
    
    return x





def fft_bluestein(x):
    N = len(x)
    M = 2**int(np.ceil(np.log2(2*N - 1)))  # Next power of 2 >= 2N - 1
    a = np.array(x, dtype=complex)

    # Chirp signal
    n = np.arange(N)
    chirp = np.exp(1j * np.pi * (n**2) / N)
    
    a_chirp = a * chirp
    b = np.zeros(M, dtype=complex)
    b[:N] = np.exp(-1j * np.pi * (n**2) / N)
    b[-(N-1):] = np.exp(-1j * np.pi * (n[1:][::-1]**2) / N)

    A = np.fft.fft(a_chirp, n=M)
    B = np.fft.fft(b, n=M)
    C = A * B
    c = np.fft.ifft(C)[:N]
    return c * chirp



def fft_zeropad(x):
    N = len(x)
    next_pow2 = 1 << (N - 1).bit_length()
    x_padded = np.pad(x, (0, next_pow2 - N), mode='constant')
    return fft_radix2(x_padded)



def fft_ct(x):
    """
    Compute the Fast Fourier Transform (FFT) using the Cooley-Tukey algorithm.
    This implementation works for signal lengths that are powers of 2.
    
    Parameters:
        x (array): Input signal (time domain)
    
    Returns:
        array: Fourier Transform of x (frequency domain)
    """
    N = len(x)
    
    # Base case: FFT of a single point is the point itself
    if N == 1:
        return x
    
    # Check if N is a power of 2
    if N & (N-1) != 0:
        raise ValueError("Signal length must be a power of 2")
    
    # Split even and odd indices
    even = fft(x[0::2])
    odd = fft(x[1::2])
    
    # Twiddle factors
    twiddle = np.exp(-2j * np.pi * np.arange(N//2) / N)
    
    # Combine using butterfly pattern
    result = np.zeros(N, dtype=complex)
    half_N = N // 2
    
    for k in range(half_N):
        result[k] = even[k] + twiddle[k] * odd[k]
        result[k + half_N] = even[k] - twiddle[k] * odd[k]
    
    return result





def ifft(X):
    """
    Compute the Inverse Fast Fourier Transform (IFFT).
    
    Parameters:
        X (array): Input spectrum (frequency domain)
    
    Returns:
        array: Inverse Fourier Transform of X (time domain)
    """
    N = len(X)
    
    # Compute the FFT of the conjugate, then conjugate the result and scale
    x = np.conj(fft(np.conj(X))) / N
    
    return x






def compress_audio_fft(audio, keep_ratio=0.05):
    """
    Compress audio by keeping only the top `keep_ratio` frequency components (by magnitude).
    
    Parameters:
        audio (np.ndarray): Time-domain audio signal
        keep_ratio (float): Fraction of strongest frequencies to keep (0 < keep_ratio <= 1)
        
    Returns:
        compressed_audio (np.ndarray): Reconstructed audio from compressed frequency domain
        X_compressed (np.ndarray): The compressed spectrum (mostly zero)
    """

    #THIS (below) IS MOST OF WHAT I DID THE REST WAS PRETTY MUCH GIVEN TO US BY DR.MILLER

    N = len(audio)
    
    # Use DFT from this above --not Numpy which i could use  by np.fft.fft:
    X = dft(audio)
    magnitudes = np.abs(X)

    # Determining how many frequencies to keep
    keep_num = int(N * keep_ratio)

    # Get indices of top frequencies (this is done with argsort) and I am doing it by the magnitude (which was done a few lines above)
    indices_to_keep = np.argsort(magnitudes)[::-1][:keep_num]  # Descending sort

    # Create a compressed version of the spectrum
    X_compressed = np.zeros_like(X) #had to look up the zeros_like 
    X_compressed[indices_to_keep] = X[indices_to_keep] #We did something similar to this call for like an 'indices to keep' in PHYS 3000 last semester

    # I am using the inverse of DFT to get time-domain signal
    compressed_audio = idft(X_compressed).real  # the .real makes it so it is keeping the real part of this as almost always that is what is wanted/important

    return compressed_audio, X_compressed