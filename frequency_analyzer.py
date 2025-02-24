"""
Módulo para el análisis de frecuencias en señales de audio.
"""

import numpy as np
from scipy import fftpack

def detectar_frecuencia(audio, sample_rate):
    """
    Detecta la frecuencia dominante en una señal de audio.
    
    Args:
        audio (numpy.ndarray): Señal de audio
        sample_rate (int): Tasa de muestreo en Hz
    
    Returns:
        float: Frecuencia dominante en Hz
    """
    espectro = np.abs(fftpack.fft(audio))
    freqs = np.fft.fftfreq(len(espectro), 1/sample_rate)
    
    # Filtrar frecuencias negativas
    indices_validos = np.where(freqs > 0)
    freqs = freqs[indices_validos]
    espectro = espectro[indices_validos]
    
    # Encontrar frecuencia con mayor amplitud
    frecuencia_dominante = freqs[np.argmax(espectro)]
    return frecuencia_dominante

def analizar_espectro(audio, sample_rate):
    """
    Analiza el espectro completo de frecuencias de una señal.
    
    Args:
        audio (numpy.ndarray): Señal de audio
        sample_rate (int): Tasa de muestreo en Hz
    
    Returns:
        tuple: (frecuencias, magnitudes) del espectro
    """
    espectro = np.abs(fftpack.fft(audio))
    freqs = np.fft.fftfreq(len(espectro), 1/sample_rate)
    
    # Filtrar frecuencias negativas
    indices_validos = np.where(freqs > 0)
    freqs = freqs[indices_validos]
    espectro = espectro[indices_validos]
    
    return freqs, espectro 